"""
Pydantic schemas for request/response validation.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field


# ============== Auth Schemas ==============

class UserCreate(BaseModel):
    """Schema for user registration."""
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)
    display_name: Optional[str] = Field(None, max_length=100)


class UserLogin(BaseModel):
    """Schema for user login."""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Schema for user info response."""
    id: int
    email: str
    display_name: Optional[str]
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class Token(BaseModel):
    """JWT token response."""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Decoded JWT token data."""
    user_id: Optional[int] = None


# ============== Chat Schemas ==============

class MessageCreate(BaseModel):
    """Schema for sending a chat message."""
    content: str = Field(min_length=1, max_length=5000)
    conversation_id: Optional[int] = None  # None = start new conversation


class MessageResponse(BaseModel):
    """Schema for message response."""
    id: int
    role: str
    content: str
    detected_intent: Optional[str]
    sentiment_score: Optional[float]
    crisis_severity: Optional[int]
    created_at: datetime

    model_config = {"from_attributes": True}


class ChatResponse(BaseModel):
    """Schema for chatbot response."""
    message: MessageResponse
    bot_response: MessageResponse
    conversation_id: int
    crisis_alert: Optional[dict] = None  # Included if crisis detected


class ConversationResponse(BaseModel):
    """Schema for conversation with messages."""
    id: int
    title: Optional[str]
    created_at: datetime
    messages: List[MessageResponse] = []

    model_config = {"from_attributes": True}


# ============== Mood Schemas ==============

class MoodCreate(BaseModel):
    """Schema for logging mood."""
    score: int = Field(ge=1, le=10)  # 1-10 scale
    notes: Optional[str] = Field(None, max_length=1000)


class MoodResponse(BaseModel):
    """Schema for mood entry response."""
    id: int
    score: int
    notes: Optional[str]
    created_at: datetime

    model_config = {"from_attributes": True}


class MoodHistoryResponse(BaseModel):
    """Schema for mood history."""
    entries: List[MoodResponse]
    average_score: Optional[float]
    trend: Optional[str]  # "improving", "stable", "declining"


# ============== Assessment Schemas ==============

class PHQ9Response(BaseModel):
    """PHQ-9 question response (0-3 scale)."""
    question_id: int = Field(ge=1, le=9)
    score: int = Field(ge=0, le=3)


class PHQ9Submit(BaseModel):
    """Schema for submitting PHQ-9 assessment."""
    responses: List[PHQ9Response] = Field(min_length=9, max_length=9)


class AssessmentResult(BaseModel):
    """Schema for assessment result."""
    id: int
    assessment_type: str
    total_score: int
    severity_level: str
    interpretation: str
    recommendations: List[str]
    created_at: datetime

    model_config = {"from_attributes": True}


# ============== Resource Schemas ==============

class ResourceResponse(BaseModel):
    """Schema for resource response."""
    id: int
    title: str
    description: str
    category: str
    url: Optional[str]
    phone: Optional[str]
    tags: List[str]
    is_crisis_resource: bool

    model_config = {"from_attributes": True}


# ============== Crisis Schemas ==============

class CrisisAlert(BaseModel):
    """Schema for crisis detection alert."""
    severity: int = Field(ge=0, le=10)
    message: str
    resources: List[ResourceResponse]
