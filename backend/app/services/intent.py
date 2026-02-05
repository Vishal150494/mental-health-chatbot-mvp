"""
Intent classification service.
Uses scikit-learn for text classification.
"""

from dataclasses import dataclass
from typing import List, Optional
import os
import pickle
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


@dataclass
class IntentResult:
    """Result of intent classification."""
    label: str
    confidence: float
    alternatives: List[tuple]  # [(label, confidence), ...]


# Fallback keyword-based classification until ML model is trained
INTENT_KEYWORDS = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening", "howdy"],
    "goodbye": ["bye", "goodbye", "see you", "take care", "later", "goodnight"],
    "mood_check": ["feeling", "feel", "mood", "today", "doing", "how am i"],
    "crisis": ["help", "emergency", "urgent", "scared", "panic", "can't cope"],
    "resource_request": ["resource", "help me find", "recommend", "suggest", "where can i"],
    "gratitude": ["thank", "thanks", "appreciate", "grateful"],
    "affirmation": ["yes", "okay", "sure", "alright", "sounds good"],
    "negation": ["no", "not really", "don't", "nope", "never mind"],
}


# Global model cache
_model: Optional[Pipeline] = None


def _load_model() -> Optional[Pipeline]:
    """Load the trained intent model if available."""
    global _model
    if _model is not None:
        return _model
    
    model_path = Path(__file__).parent.parent / "ml" / "intent_model.pkl"
    if model_path.exists():
        with open(model_path, "rb") as f:
            _model = pickle.load(f)
        return _model
    
    return None


def classify_intent(text: str) -> IntentResult:
    """
    Classify the intent of user input.
    
    Uses trained ML model if available, falls back to keyword matching.
    """
    # Try ML model first
    model = _load_model()
    if model is not None:
        try:
            probabilities = model.predict_proba([text])[0]
            classes = model.classes_
            
            # Get top prediction
            top_idx = probabilities.argmax()
            label = classes[top_idx]
            confidence = probabilities[top_idx]
            
            # Get alternatives (top 3)
            sorted_indices = probabilities.argsort()[::-1][:3]
            alternatives = [
                (classes[i], probabilities[i])
                for i in sorted_indices[1:]  # Exclude top
            ]
            
            return IntentResult(
                label=label,
                confidence=confidence,
                alternatives=alternatives,
            )
        except Exception:
            pass  # Fall back to keyword matching
    
    # Fallback: keyword-based classification
    text_lower = text.lower()
    
    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text_lower:
                return IntentResult(
                    label=intent,
                    confidence=0.6,  # Lower confidence for keyword match
                    alternatives=[],
                )
    
    # Default to unknown
    return IntentResult(
        label="unknown",
        confidence=0.5,
        alternatives=[],
    )


def train_intent_model(training_data: List[tuple]) -> Pipeline:
    """
    Train a new intent classification model.
    
    Args:
        training_data: List of (text, intent_label) tuples
    
    Returns:
        Trained sklearn Pipeline
    """
    texts, labels = zip(*training_data)
    
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=5000)),
        ("classifier", MultinomialNB()),
    ])
    
    model.fit(texts, labels)
    
    # Save model
    model_path = Path(__file__).parent.parent / "ml" / "intent_model.pkl"
    model_path.parent.mkdir(parents=True, exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    
    # Update global cache
    global _model
    _model = model
    
    return model
