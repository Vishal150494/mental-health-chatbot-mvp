"""
SQLAlchemy ORM models for Mental Health Chatbot.
Uses UUID for all primary keys.
"""

import uuid
from datetime import datetime
from typing import Optional, List

from sqlalchemy import String, Text, Integer, Float, Boolean, ForeignKey, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    """User account model."""
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[Optional[str]] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships (One-to-Many)
    conversations: Mapped[List["Conversation"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    mood_entries: Mapped[List["MoodEntry"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    assessments: Mapped[List["Assessment"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Conversation(Base):
    """Chat conversation session."""
    __tablename__ = "conversations"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    title: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships (One-to-Many)
    user: Mapped["User"] = relationship(back_populates="conversations")
    messages: Mapped[List["Message"]] = relationship(back_populates="conversation", cascade="all, delete-orphan")


class Message(Base):
    """Individual chat message."""
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("conversations.id"), index=True)
    role: Mapped[str] = mapped_column(String(20))  # "user" or "assistant"
    content: Mapped[str] = mapped_column(Text)
    
    # NLP analysis results (stored for analytics, not PII)
    detected_intent: Mapped[Optional[str]] = mapped_column(String(50))
    sentiment_score: Mapped[Optional[float]] = mapped_column(Float)
    sentiment_label: Mapped[Optional[str]] = mapped_column(String(20))  # "positive", "negative", "neutral"
    crisis_severity: Mapped[Optional[int]] = mapped_column(Integer, default=0)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    conversation: Mapped["Conversation"] = relationship(back_populates="messages")


class MoodEntry(Base):
    """Daily mood tracking entry."""
    __tablename__ = "mood_entries"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    score: Mapped[int] = mapped_column(Integer)  # 1-10 scale
    notes: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="mood_entries")


class Assessment(Base):
    """PHQ-9 or other assessment results."""
    __tablename__ = "assessments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    assessment_type: Mapped[str] = mapped_column(String(50))  # "phq9", "gad7", etc.
    responses: Mapped[dict] = mapped_column(JSON)  # Question responses
    total_score: Mapped[int] = mapped_column(Integer)
    severity_level: Mapped[str] = mapped_column(String(50))  # "minimal", "mild", "moderate", "severe"
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="assessments")


class Resource(Base):
    """Mental health resource catalog."""
    __tablename__ = "resources"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(100))  # "hotline", "technique", "article", "app"
    url: Mapped[Optional[str]] = mapped_column(String(500))
    phone: Mapped[Optional[str]] = mapped_column(String(50))
    tags: Mapped[List[str]] = mapped_column(JSON, default=list)
    
    # For semantic search
    embedding: Mapped[Optional[List[float]]] = mapped_column(JSON)
    
    is_crisis_resource: Mapped[bool] = mapped_column(Boolean, default=False)
    priority: Mapped[int] = mapped_column(Integer, default=0)  # Higher = show first
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
