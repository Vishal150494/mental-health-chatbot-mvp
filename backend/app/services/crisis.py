"""
Crisis detection service.
Keyword-based detection with severity scoring.
"""

from dataclasses import dataclass
from typing import List, Optional
import re


@dataclass
class CrisisResult:
    """Result of crisis detection analysis."""
    severity: int  # 0-10 scale
    matched_keywords: List[str]
    recommended_action: str
    is_immediate_danger: bool = False


# Crisis keyword categories with severity weights
CRISIS_KEYWORDS = {
    # CRITICAL - Immediate danger (severity 9-10)
    "critical": {
        "keywords": [
            "kill myself", "end my life", "suicide", "suicidal",
            "want to die", "better off dead", "take my life",
            "end it all", "no reason to live", "overdose",
        ],
        "base_severity": 9,
    },
    # HIGH - Self-harm or severe distress (severity 7-8)
    "high": {
        "keywords": [
            "self-harm", "cutting myself", "hurt myself", "harming myself",
            "can't go on", "give up", "nothing matters anymore",
            "everyone would be better without me",
        ],
        "base_severity": 7,
    },
    # MODERATE - Significant distress (severity 4-6)
    "moderate": {
        "keywords": [
            "hopeless", "worthless", "burden", "trapped",
            "can't take it anymore", "breaking down", "falling apart",
            "panic attack", "can't breathe", "losing control",
        ],
        "base_severity": 5,
    },
    # LOW - Mild distress indicators (severity 2-3)
    "low": {
        "keywords": [
            "depressed", "anxious", "stressed", "overwhelmed",
            "lonely", "sad", "scared", "worried", "exhausted",
        ],
        "base_severity": 2,
    },
}

# Negation patterns that reduce severity
NEGATION_PATTERNS = [
    r"not\s+(?:feeling\s+)?(?:suicidal|like\s+dying)",
    r"don't\s+want\s+to\s+(?:die|hurt)",
    r"no\s+(?:suicidal|harmful)\s+thoughts",
    r"never\s+(?:suicidal|self-harm)",
]

# Context patterns that indicate third-party or educational mentions
CONTEXT_PATTERNS = [
    r"friend\s+(?:mentioned|said|told)",
    r"(?:movie|book|article|documentary)\s+about",
    r"(?:read|heard|learned)\s+about",
    r"someone\s+(?:I know|else)",
]


def detect_crisis(text: str) -> CrisisResult:
    """
    Analyze text for crisis indicators.
    
    Returns CrisisResult with severity score (0-10) and matched keywords.
    Higher scores indicate more urgent need for intervention.
    """
    text_lower = text.lower()
    matched_keywords = []
    max_severity = 0
    
    # Check for negation patterns first
    is_negated = any(re.search(pattern, text_lower) for pattern in NEGATION_PATTERNS)
    
    # Check for third-party/educational context
    is_context_mention = any(re.search(pattern, text_lower) for pattern in CONTEXT_PATTERNS)
    
    # Scan for crisis keywords
    for category, config in CRISIS_KEYWORDS.items():
        for keyword in config["keywords"]:
            if keyword in text_lower:
                matched_keywords.append(keyword)
                severity = config["base_severity"]
                
                # Adjust for context
                if is_negated and category in ["critical", "high"]:
                    severity = min(severity, 3)  # Cap at low severity
                elif is_context_mention:
                    severity = max(1, severity - 3)  # Reduce but don't eliminate
                
                max_severity = max(max_severity, severity)
    
    # Compound effect: multiple keywords increase severity
    if len(matched_keywords) > 2:
        max_severity = min(10, max_severity + 1)
    
    # Determine recommended action
    if max_severity >= 8:
        action = "Immediate crisis intervention required. Show crisis resources prominently."
        is_immediate = True
    elif max_severity >= 5:
        action = "Elevated concern. Include crisis resources in response."
        is_immediate = False
    elif max_severity >= 2:
        action = "Monitor for escalation. Offer supportive response."
        is_immediate = False
    else:
        action = "Normal response flow."
        is_immediate = False
    
    return CrisisResult(
        severity=max_severity,
        matched_keywords=matched_keywords,
        recommended_action=action,
        is_immediate_danger=is_immediate,
    )
