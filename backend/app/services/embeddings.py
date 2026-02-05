"""
Embeddings service.
Uses Sentence-Transformers for text embeddings.
"""

from typing import List, Optional
import os

# Model configuration
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

# Global model cache
_model = None


def _load_model():
    """Load the sentence transformer model."""
    global _model
    if _model is None:
        try:
            from sentence_transformers import SentenceTransformer
            _model = SentenceTransformer(EMBEDDING_MODEL)
        except ImportError:
            print("sentence-transformers not installed. Embeddings unavailable.")
            return None
    return _model


def generate_embedding(text: str) -> Optional[List[float]]:
    """
    Generate an embedding vector for the given text.
    
    Returns None if sentence-transformers is not available.
    """
    model = _load_model()
    if model is None:
        return None
    
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding.tolist()


def generate_embeddings_batch(texts: List[str]) -> Optional[List[List[float]]]:
    """
    Generate embeddings for multiple texts.
    
    More efficient than calling generate_embedding multiple times.
    """
    model = _load_model()
    if model is None:
        return None
    
    embeddings = model.encode(texts, convert_to_numpy=True)
    return [emb.tolist() for emb in embeddings]


def calculate_similarity(embedding1: List[float], embedding2: List[float]) -> float:
    """
    Calculate cosine similarity between two embeddings.
    """
    import math
    
    dot_product = sum(a * b for a, b in zip(embedding1, embedding2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in embedding1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in embedding2))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)


def find_most_similar(
    query_embedding: List[float],
    candidate_embeddings: List[List[float]],
    top_k: int = 5,
) -> List[tuple]:
    """
    Find the most similar embeddings to the query.
    
    Returns list of (index, similarity_score) tuples, sorted by similarity.
    """
    similarities = [
        (i, calculate_similarity(query_embedding, emb))
        for i, emb in enumerate(candidate_embeddings)
    ]
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_k]
