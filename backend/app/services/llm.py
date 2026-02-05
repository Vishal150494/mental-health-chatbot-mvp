"""
LLM integration service.
Uses Ollama for local LLM inference.
"""

import os
import httpx
from typing import Optional

# Ollama configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

# System prompt for mental health chatbot
SYSTEM_PROMPT = """You are a compassionate mental health support companion. You must:

1. NEVER provide medical diagnoses or recommend specific medications
2. ALWAYS suggest professional help for serious concerns
3. Include crisis resources (988, Crisis Text Line) if you detect distress
4. Use empathetic, non-judgmental, supportive language
5. Ask open-ended questions to encourage the user to share
6. Validate feelings before offering suggestions
7. Keep responses concise but warm (2-4 sentences typically)

You are NOT a replacement for professional mental health care. You are a supportive companion for daily check-ins and emotional support."""


async def generate_response(
    user_message: str,
    intent: str,
    sentiment,
    conversation_id: int,
    max_tokens: int = 256,
) -> str:
    """
    Generate a response using Ollama LLM.
    
    Falls back to a template response if Ollama is unavailable.
    """
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": OLLAMA_MODEL,
                    "prompt": _build_prompt(user_message, intent, sentiment),
                    "system": SYSTEM_PROMPT,
                    "stream": False,
                    "options": {
                        "num_predict": max_tokens,
                        "temperature": 0.7,
                    },
                },
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get("response", _get_fallback_response(intent))
            
    except Exception as e:
        # Log error but don't expose to user
        print(f"Ollama error: {e}")
    
    return _get_fallback_response(intent)


def _build_prompt(user_message: str, intent: str, sentiment) -> str:
    """Build the prompt for the LLM."""
    context = f"""User intent: {intent}
Emotional tone: {sentiment.label} (score: {sentiment.compound_score:.2f})

User message: {user_message}

Respond with empathy and support. Keep your response concise (2-4 sentences)."""
    
    return context


def _get_fallback_response(intent: str) -> str:
    """Get a fallback response when LLM is unavailable."""
    fallbacks = {
        "greeting": "Hello! I'm here to listen and support you. How are you feeling today?",
        "goodbye": "Take care of yourself. Remember, I'm here whenever you need to talk.",
        "mood_check": "Thank you for sharing that with me. It takes courage to express how we feel. Would you like to tell me more?",
        "crisis": (
            "I'm really concerned about what you're sharing. Please know that help is available. "
            "You can call or text 988 to reach the Suicide & Crisis Lifeline anytime."
        ),
        "resource_request": "I'd be happy to help you find some resources. What type of support are you looking for?",
        "unknown": "I hear you. Thank you for sharing that with me. Would you like to tell me more about what's going on?",
    }
    return fallbacks.get(intent, fallbacks["unknown"])


async def check_ollama_health() -> bool:
    """Check if Ollama is available and the model is loaded."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            if response.status_code == 200:
                data = response.json()
                models = [m["name"] for m in data.get("models", [])]
                return OLLAMA_MODEL in models or f"{OLLAMA_MODEL}:latest" in models
    except Exception:
        pass
    return False
