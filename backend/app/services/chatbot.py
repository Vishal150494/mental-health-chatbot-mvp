"""
Main chatbot orchestration service.
Coordinates NLP pipeline: intent → sentiment → crisis → response generation.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Message, Conversation
from app.schemas import ChatResponse, MessageResponse, CrisisAlert
from app.services.intent import classify_intent
from app.services.sentiment import analyze_sentiment
from app.services.crisis import detect_crisis
from app.services.llm import generate_response
from app.services.resource_matcher import get_relevant_resources


async def process_message(
    user_message: str,
    conversation_id: int,
    user_id: int,
    db: AsyncSession,
) -> ChatResponse:
    """
    Process a user message through the NLP pipeline and generate a response.
    
    Pipeline:
    1. Intent classification
    2. Sentiment analysis
    3. Crisis detection
    4. Response generation (template or LLM)
    5. Resource matching (if needed)
    """
    # Step 1: Classify intent
    intent = classify_intent(user_message)
    
    # Step 2: Analyze sentiment
    sentiment_result = analyze_sentiment(user_message)
    
    # Step 3: Crisis detection
    crisis_result = detect_crisis(user_message)
    
    # Save user message
    user_msg = Message(
        conversation_id=conversation_id,
        role="user",
        content=user_message,
        detected_intent=intent.label,
        sentiment_score=sentiment_result.compound_score,
        crisis_severity=crisis_result.severity,
    )
    db.add(user_msg)
    await db.flush()
    
    # Step 4: Generate response
    if crisis_result.severity >= 8:
        # High crisis - use crisis response template
        bot_content = _get_crisis_response(crisis_result)
    elif intent.label in TEMPLATE_RESPONSES:
        # Known intent - use template with personalization
        bot_content = _get_template_response(intent.label, sentiment_result)
    else:
        # Unknown/complex - use LLM
        bot_content = await generate_response(
            user_message=user_message,
            intent=intent.label,
            sentiment=sentiment_result,
            conversation_id=conversation_id,
        )
    
    # Save bot response
    bot_msg = Message(
        conversation_id=conversation_id,
        role="assistant",
        content=bot_content,
    )
    db.add(bot_msg)
    await db.flush()
    
    # Update conversation timestamp
    await db.execute(
        Conversation.__table__.update()
        .where(Conversation.id == conversation_id)
        .values(updated_at=user_msg.created_at)
    )
    
    # Build response
    crisis_alert = None
    if crisis_result.severity >= 5:
        resources = await get_relevant_resources(
            query="crisis support",
            is_crisis=True,
            db=db,
        )
        crisis_alert = CrisisAlert(
            severity=crisis_result.severity,
            message=crisis_result.recommended_action,
            resources=resources,
        )
    
    return ChatResponse(
        message=MessageResponse.model_validate(user_msg),
        bot_response=MessageResponse.model_validate(bot_msg),
        conversation_id=conversation_id,
        crisis_alert=crisis_alert.model_dump() if crisis_alert else None,
    )


# Template responses for common intents
TEMPLATE_RESPONSES = {
    "greeting": [
        "Hello! I'm here to chat and support you. How are you feeling today?",
        "Hi there! It's good to hear from you. What's on your mind?",
    ],
    "goodbye": [
        "Take care of yourself! Remember, I'm here whenever you need to talk.",
        "Goodbye for now. Be kind to yourself today.",
    ],
    "mood_check": [
        "I hear you. Would you like to tell me more about how you're feeling?",
        "Thank you for sharing. It takes courage to express how we feel.",
    ],
    "resource_request": [
        "I'd be happy to help you find some resources. What area would you like support with?",
    ],
}


def _get_template_response(intent: str, sentiment) -> str:
    """Get a template response based on intent and sentiment."""
    import random
    templates = TEMPLATE_RESPONSES.get(intent, [])
    if templates:
        return random.choice(templates)
    return "I'm here to listen. Tell me more about what's going on."


def _get_crisis_response(crisis_result) -> str:
    """Generate an immediate crisis response."""
    return (
        "I'm really glad you reached out. What you're feeling sounds really difficult, "
        "and I want you to know that help is available right now.\n\n"
        "**Please reach out immediately:**\n"
        "📞 **988 Suicide & Crisis Lifeline** - Call or text 988\n"
        "💬 **Crisis Text Line** - Text HOME to 741741\n\n"
        "You don't have to face this alone. These services are free, confidential, "
        "and available 24/7. Would you like to talk about what's happening?"
    )
