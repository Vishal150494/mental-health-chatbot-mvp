"""
Chat routes - send messages, get conversation history.
"""

from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models import User, Conversation, Message
from app.schemas import MessageCreate, ChatResponse, ConversationResponse, MessageResponse
from app.utils.security import get_current_user
from app.services.chatbot import process_message

router = APIRouter()


@router.post("/send", response_model=ChatResponse)
async def send_message(
    message: MessageCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
):
    """
    Send a message and get chatbot response.
    Creates a new conversation if conversation_id is not provided.
    """
    # Get or create conversation
    if message.conversation_id:
        result = await db.execute(
            select(Conversation).where(
                Conversation.id == message.conversation_id,
                Conversation.user_id == current_user.id,
            )
        )
        conversation = result.scalar_one_or_none()
        if not conversation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Conversation not found",
            )
    else:
        conversation = Conversation(user_id=current_user.id)
        db.add(conversation)
        await db.flush()

    # Process message through NLP pipeline
    response = await process_message(
        user_message=message.content,
        conversation_id=conversation.id,
        user_id=current_user.id,
        db=db,
    )

    return response


@router.get("/history", response_model=List[ConversationResponse])
async def get_conversations(
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
    limit: int = 20,
):
    """Get user's conversation history."""
    result = await db.execute(
        select(Conversation)
        .where(Conversation.user_id == current_user.id)
        .options(selectinload(Conversation.messages))
        .order_by(Conversation.updated_at.desc())
        .limit(limit)
    )
    conversations = result.scalars().all()
    return conversations


@router.get("/conversation/{conversation_id}", response_model=ConversationResponse)
async def get_conversation(
    conversation_id: UUID,
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
):
    """Get a specific conversation with all messages."""
    result = await db.execute(
        select(Conversation)
        .where(
            Conversation.id == conversation_id,
            Conversation.user_id == current_user.id,
        )
        .options(selectinload(Conversation.messages))
    )
    conversation = result.scalar_one_or_none()

    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found",
        )

    return conversation
