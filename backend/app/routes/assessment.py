"""
Assessment routes - PHQ-9 and other mental health assessments.
"""

from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User, Assessment
from app.schemas import PHQ9Submit, AssessmentResult
from app.utils.security import get_current_user

router = APIRouter()

# PHQ-9 Questions for reference
PHQ9_QUESTIONS = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself - or that you are a failure",
    "Trouble concentrating on things, such as reading or watching TV",
    "Moving or speaking slowly, or being fidgety/restless",
    "Thoughts that you would be better off dead, or of hurting yourself",
]

# Severity levels based on total score
PHQ9_SEVERITY = [
    (0, 4, "minimal", "Your responses suggest minimal depression symptoms."),
    (5, 9, "mild", "Your responses suggest mild depression symptoms."),
    (10, 14, "moderate", "Your responses suggest moderate depression symptoms."),
    (15, 19, "moderately severe", "Your responses suggest moderately severe depression."),
    (20, 27, "severe", "Your responses suggest severe depression symptoms."),
]


def get_phq9_severity(score: int) -> tuple[str, str]:
    """Get severity level and interpretation for PHQ-9 score."""
    for min_score, max_score, level, interpretation in PHQ9_SEVERITY:
        if min_score <= score <= max_score:
            return level, interpretation
    return "unknown", "Unable to determine severity."


def get_phq9_recommendations(severity: str, has_suicidal_ideation: bool) -> List[str]:
    """Generate recommendations based on PHQ-9 results."""
    recommendations = []

    if has_suicidal_ideation:
        recommendations.append(
            "⚠️ If you're having thoughts of self-harm, please reach out immediately: "
            "988 Suicide & Crisis Lifeline (call/text 988)"
        )

    if severity in ["minimal", "mild"]:
        recommendations.extend([
            "Continue monitoring your mood regularly",
            "Practice self-care activities like exercise, sleep hygiene, and social connection",
            "Consider stress-reduction techniques like mindfulness or deep breathing",
        ])
    elif severity == "moderate":
        recommendations.extend([
            "Consider speaking with a mental health professional",
            "Your primary care doctor can be a good first step",
            "Continue tracking your mood to monitor changes",
        ])
    elif severity in ["moderately severe", "severe"]:
        recommendations.extend([
            "We strongly recommend speaking with a mental health professional",
            "Contact your doctor or a therapist as soon as possible",
            "If symptoms worsen, don't hesitate to seek immediate help",
        ])

    return recommendations


@router.post("/phq9", response_model=AssessmentResult, status_code=201)
async def submit_phq9(
    submission: PHQ9Submit,
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
):
    """
    Submit PHQ-9 assessment responses.
    Each response is 0-3 for each of the 9 questions.
    """
    # Calculate total score
    responses_dict = {r.question_id: r.score for r in submission.responses}
    total_score = sum(responses_dict.values())

    # Check for suicidal ideation (question 9)
    has_suicidal_ideation = responses_dict.get(9, 0) > 0

    # Get severity and interpretation
    severity_level, interpretation = get_phq9_severity(total_score)
    recommendations = get_phq9_recommendations(severity_level, has_suicidal_ideation)

    # Save assessment
    assessment = Assessment(
        user_id=current_user.id,
        assessment_type="phq9",
        responses=responses_dict,
        total_score=total_score,
        severity_level=severity_level,
    )
    db.add(assessment)
    await db.commit()
    await db.refresh(assessment)

    return AssessmentResult(
        id=assessment.id,
        assessment_type="phq9",
        total_score=total_score,
        severity_level=severity_level,
        interpretation=interpretation,
        recommendations=recommendations,
        created_at=assessment.created_at,
    )


@router.get("/history", response_model=List[AssessmentResult])
async def get_assessment_history(
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
    limit: int = 10,
):
    """Get user's assessment history."""
    result = await db.execute(
        select(Assessment)
        .where(Assessment.user_id == current_user.id)
        .order_by(Assessment.created_at.desc())
        .limit(limit)
    )
    assessments = result.scalars().all()

    # Convert to response format with interpretations
    results = []
    for a in assessments:
        if a.assessment_type == "phq9":
            severity_level, interpretation = get_phq9_severity(a.total_score)
            has_suicidal = a.responses.get("9", 0) > 0 if a.responses else False
            recommendations = get_phq9_recommendations(severity_level, has_suicidal)
        else:
            interpretation = ""
            recommendations = []

        results.append(AssessmentResult(
            id=a.id,
            assessment_type=a.assessment_type,
            total_score=a.total_score,
            severity_level=a.severity_level,
            interpretation=interpretation,
            recommendations=recommendations,
            created_at=a.created_at,
        ))

    return results
