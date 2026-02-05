"""
Sentiment analysis service.
Uses TextBlob for polarity and subjectivity analysis.
"""

from dataclasses import dataclass
from textblob import TextBlob


@dataclass
class SentimentResult:
    """Result of sentiment analysis."""
    compound_score: float  # -1 to 1 (negative to positive)
    polarity: float  # -1 to 1
    subjectivity: float  # 0 to 1 (objective to subjective)
    label: str  # "positive", "negative", "neutral"


def analyze_sentiment(text: str) -> SentimentResult:
    """
    Analyze the sentiment of text using TextBlob.
    
    Returns SentimentResult with polarity, subjectivity, and label.
    """
    blob = TextBlob(text)
    
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determine label based on polarity
    if polarity > 0.1:
        label = "positive"
    elif polarity < -0.1:
        label = "negative"
    else:
        label = "neutral"
    
    return SentimentResult(
        compound_score=polarity,
        polarity=polarity,
        subjectivity=subjectivity,
        label=label,
    )


def get_emotional_tone(text: str) -> dict:
    """
    Get a more detailed emotional analysis.
    
    Returns dict with various emotional indicators.
    """
    sentiment = analyze_sentiment(text)
    
    # Simple heuristic-based emotional indicators
    text_lower = text.lower()
    
    indicators = {
        "sentiment": sentiment.label,
        "intensity": abs(sentiment.polarity),
        "is_emotional": sentiment.subjectivity > 0.5,
        "needs_support": sentiment.polarity < -0.3 or any(
            word in text_lower for word in ["help", "struggling", "hard", "difficult"]
        ),
    }
    
    return indicators
