"""
Mood tracking routes - log mood, view history.
"""

from datetime import datetime, timedelta
from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User, MoodEntry
from app.schemas import MoodCreate, MoodResponse, MoodHistoryResponse
from app.utils.security import get_current_user

router = APIRouter()


@router.post("/log", response_model=MoodResponse, status_code=201)
async def log_mood(
    mood: MoodCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
):
    """Log a mood entry (1-10 scale)."""
    entry = MoodEntry(
        user_id=current_user.id,
        score=mood.score,
        notes=mood.notes,
    )
    db.add(entry)
    await db.commit()
    await db.refresh(entry)
    return entry


@router.get("/history", response_model=MoodHistoryResponse)
async def get_mood_history(
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
    days: int = 30,
):
    """Get mood history for the past N days with trend analysis."""
    since = datetime.utcnow() - timedelta(days=days)

    result = await db.execute(
        select(MoodEntry)
        .where(
            MoodEntry.user_id == current_user.id,
            MoodEntry.created_at >= since,
        )
        .order_by(MoodEntry.created_at.desc())
    )
    entries = result.scalars().all()

    # Calculate average
    avg_result = await db.execute(
        select(func.avg(MoodEntry.score))
        .where(
            MoodEntry.user_id == current_user.id,
            MoodEntry.created_at >= since,
        )
    )
    average_score = avg_result.scalar()

    # Determine trend (compare first half to second half)
    trend = None
    if len(entries) >= 4:
        mid = len(entries) // 2
        recent_avg = sum(e.score for e in entries[:mid]) / mid
        older_avg = sum(e.score for e in entries[mid:]) / (len(entries) - mid)

        if recent_avg > older_avg + 0.5:
            trend = "improving"
        elif recent_avg < older_avg - 0.5:
            trend = "declining"
        else:
            trend = "stable"

    return MoodHistoryResponse(
        entries=entries,
        average_score=round(average_score, 1) if average_score else None,
        trend=trend,
    )


@router.get("/today", response_model=List[MoodResponse])
async def get_today_mood(
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
):
    """Get today's mood entries."""
    today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)

    result = await db.execute(
        select(MoodEntry)
        .where(
            MoodEntry.user_id == current_user.id,
            MoodEntry.created_at >= today_start,
        )
        .order_by(MoodEntry.created_at.desc())
    )
    return result.scalars().all()
