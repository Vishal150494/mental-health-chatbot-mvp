"""
Resource matching service.
Semantic search for mental health resources.
"""

from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Resource
from app.schemas import ResourceResponse


# Crisis resources (always available even without DB)
CRISIS_RESOURCES = [
    ResourceResponse(
        id=0,
        title="988 Suicide & Crisis Lifeline",
        description="Free, confidential support 24/7. Call or text 988.",
        category="hotline",
        url="https://988lifeline.org",
        phone="988",
        tags=["crisis", "suicide", "24/7"],
        is_crisis_resource=True,
    ),
    ResourceResponse(
        id=0,
        title="Crisis Text Line",
        description="Text HOME to 741741 to connect with a counselor.",
        category="hotline",
        url="https://www.crisistextline.org",
        phone=None,
        tags=["crisis", "text", "24/7"],
        is_crisis_resource=True,
    ),
    ResourceResponse(
        id=0,
        title="SAMHSA National Helpline",
        description="Treatment referrals and information 24/7. Call 1-800-662-4357.",
        category="hotline",
        url="https://www.samhsa.gov/find-help/national-helpline",
        phone="1-800-662-4357",
        tags=["treatment", "referral", "24/7"],
        is_crisis_resource=True,
    ),
]


async def get_relevant_resources(
    query: str,
    is_crisis: bool = False,
    db: Optional[AsyncSession] = None,
    limit: int = 5,
) -> List[ResourceResponse]:
    """
    Get resources relevant to the query.
    
    For crisis situations, always returns crisis resources first.
    Uses semantic search when embeddings are available.
    """
    results = []
    
    # Always include crisis resources for crisis queries
    if is_crisis:
        results.extend(CRISIS_RESOURCES)
    
    # Try to get additional resources from database
    if db is not None:
        try:
            # Simple keyword matching for now
            # TODO: Implement semantic search with embeddings
            stmt = select(Resource).where(
                Resource.is_crisis_resource == is_crisis
            ).order_by(
                Resource.priority.desc()
            ).limit(limit)
            
            db_results = await db.execute(stmt)
            for resource in db_results.scalars():
                results.append(ResourceResponse.model_validate(resource))
        except Exception:
            pass  # Fall back to hardcoded resources
    
    return results[:limit]


async def search_resources_semantic(
    query: str,
    query_embedding: List[float],
    db: AsyncSession,
    limit: int = 5,
) -> List[ResourceResponse]:
    """
    Search resources using semantic similarity.
    
    Requires resources to have pre-computed embeddings.
    Uses cosine similarity for matching.
    """
    # TODO: Implement once sentence-transformers embeddings are set up
    # For now, fall back to keyword search
    return await get_relevant_resources(query, is_crisis=False, db=db, limit=limit)


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    import math
    
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vec2))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)
