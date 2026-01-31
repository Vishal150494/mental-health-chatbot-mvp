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
    username : str = Field(min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$", description="Username must be 3-50 characters long and contain alphanumeric characters and underscores")
    password: str = Field(min_length=8, max_length=128, description="Password must be at least 8 characters long")
    full_name: Optional[str] = Field(None, max_length=100, description="User'S full name")


class UserLogin(BaseModel):
    """Schema for user login."""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Schema for user info response."""
    id: str # UUID as string
    email: EmailStr
    username: str
    full_name: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {"from_attributes": True}


class Token(BaseModel):
    """JWT token response."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int # Seconds until expiration


class TokenData(BaseModel):
    """Decoded JWT token data."""
    user_id: Optional[str] = None # UUID as string
    email: Optional[str] = None
    exp: Optional[datetime] = None # Expiration time


# ============== Chat Schemas ==============

class MessageCreate(BaseModel):
    """Schema for sending a chat message."""
    content: str = Field(min_length=1, max_length=5000)
    conversation_id: Optional[str] = None  # None = start new conversation (UUID as string)


class MessageResponse(BaseModel):
    """Schema for message response."""
    id: str  # UUID as string
    role: str  # "user" or "assistant"
    content: str
    detected_intent: Optional[str]
    sentiment_score: Optional[float]
    sentiment_label: Optional[str]  # "positive", "negative", "neutral"
    crisis_severity: Optional[int]  # 0-10 scale
    created_at: datetime

    model_config = {"from_attributes": True}


class ChatResponse(BaseModel):
    """Schema for chatbot response."""
    message: MessageResponse
    bot_response: MessageResponse
    conversation_id: str  # UUID as string
    crisis_alert: Optional[dict] = None  # Included if crisis detected


class ConversationResponse(BaseModel):
    """Schema for conversation with messages."""
    id: str  # UUID as string
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
    id: str  # UUID as string
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
    id: str  # UUID as string
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
    id: str  # UUID as string
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
