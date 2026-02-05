"""
FastAPI application entry point.
Mental Health Chatbot MVP - Backend API
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth  # chat, mood, assessment temporarily commented out
from app.database import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    # Startup: Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown: cleanup if needed
    await engine.dispose()


app = FastAPI(
    title="Mental Health Chatbot API",
    description="AI-powered mental health check-in chatbot with NLP pipeline",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
#app.include_router(chat.router, prefix="/chat", tags=["Chat"])
#app.include_router(mood.router, prefix="/mood", tags=["Mood Tracking"])
#app.include_router(assessment.router, prefix="/assessment", tags=["Assessments"])


@app.get("/", tags=["Health"])
async def root():
    """API root - basic info."""
    return {
        "name": "Mental Health Chatbot API",
        "version": "0.1.0",
        "status": "healthy",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy"}
