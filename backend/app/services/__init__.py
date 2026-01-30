"""
Services package - exports all services.
"""

from app.services.chatbot import process_message
from app.services.crisis import detect_crisis, CrisisResult
from app.services.sentiment import analyze_sentiment, SentimentResult
from app.services.intent import classify_intent, IntentResult
from app.services.llm import generate_response
from app.services.embeddings import generate_embedding
from app.services.resource_matcher import get_relevant_resources

__all__ = [
    "process_message",
    "detect_crisis",
    "CrisisResult",
    "analyze_sentiment",
    "SentimentResult",
    "classify_intent",
    "IntentResult",
    "generate_response",
    "generate_embedding",
    "get_relevant_resources",
]
