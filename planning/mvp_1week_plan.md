# Mental Health Chatbot - 1 Week MVP Plan

**Scope:** Rapid prototype with core features (not production-ready)  
**Duration:** 7 Days  
**Tech Stack:** Python (FastAPI) + React + PostgreSQL + Ollama  
**Status:** Exploration/Validation Phase

---

## Project Timeline & Milestones

```
WEEK 1: Mental Health Chatbot MVP

DAY 1 (Monday)
├─ Setup & Infrastructure
│  ├─ 09:00-10:00: Project initialization & environments
│  ├─ 10:00-12:00: Database setup & schema creation
│  └─ 13:00-17:00: Backend skeleton (FastAPI + Pydantic models)
│
├─ Deliverables:
│  ├─ ✓ Git repository with folder structure
│  ├─ ✓ PostgreSQL database initialized
│  └─ ✓ FastAPI app running locally (http://localhost:8000)

---

DAY 2 (Tuesday)
├─ Core Backend Features
│  ├─ 09:00-12:00: Authentication (JWT + login/register)
│  ├─ 13:00-15:00: Chat message endpoint (POST /chat/message)
│  └─ 15:00-17:00: Chat history endpoint (GET /chat/history)
│
├─ Deliverables:
│  ├─ ✓ User registration & login working
│  ├─ ✓ Token-based auth with JWT
│  └─ ✓ Message persistence to database

---

DAY 3 (Wednesday)
├─ NLP & Intent Classification
│  ├─ 09:00-11:00: Sentiment analysis (TextBlob/VADER)
│  ├─ 11:00-14:00: Intent classifier (Scikit-learn training)
│  ├─ 14:00-16:00: Crisis detection (keyword + rule-based)
│  └─ 16:00-17:00: Integrate into chat pipeline
│
├─ Deliverables:
│  ├─ ✓ Sentiment scores attached to messages
│  ├─ ✓ Intent classification working (>85% accuracy)
│  └─ ✓ Crisis detection triggered correctly

---

DAY 4 (Thursday)
├─ LLM Integration & Response Generation
│  ├─ 09:00-10:00: Ollama setup & model pull (Llama 3.2)
│  ├─ 10:00-12:00: LangChain integration for prompt management
│  ├─ 13:00-15:00: Template-based responses (intents.json)
│  └─ 15:00-17:00: LLM-generated responses for complex queries
│
├─ Deliverables:
│  ├─ ✓ Ollama running locally with model
│  ├─ ✓ Two-tier response system (templates + LLM)
│  └─ ✓ Chat endpoint returns smart responses

---

DAY 5 (Friday)
├─ Frontend & UI
│  ├─ 09:00-11:00: React setup + authentication UI (login/register)
│  ├─ 11:00-13:00: Chat interface (message input, history display)
│  ├─ 14:00-16:00: Mood tracker (simple 1-10 scale)
│  └─ 16:00-17:00: Styling with Tailwind CSS
│
├─ Deliverables:
│  ├─ ✓ User can login/register
│  ├─ ✓ Chat window with real-time messaging
│  ├─ ✓ Mood logging UI
│  └─ ✓ Clean, responsive design

---

DAY 6 (Saturday)
├─ Assessment Module & Resources
│  ├─ 09:00-11:00: PHQ-9 assessment form & scoring
│  ├─ 11:00-13:00: Resource recommendation engine (simple keyword match)
│  ├─ 14:00-16:00: Resources library UI (crisis hotlines, coping tools)
│  └─ 16:00-17:00: Hook resources to chatbot responses
│
├─ Deliverables:
│  ├─ ✓ PHQ-9 questionnaire with scoring
│  ├─ ✓ Resource recommendations displayed
│  └─ ✓ Crisis hotlines shown for critical messages

---

DAY 7 (Sunday)
├─ Testing, Documentation & Deployment
│  ├─ 09:00-11:00: Manual testing (E2E scenarios)
│  ├─ 11:00-12:00: Bug fixes & polish
│  ├─ 13:00-15:00: README & setup documentation
│  ├─ 15:00-16:00: Local Docker setup (docker-compose.yml)
│  └─ 16:00-17:00: Demo recording & final touches
│
├─ Deliverables:
│  ├─ ✓ All features tested end-to-end
│  ├─ ✓ README with quick start guide
│  ├─ ✓ Docker Compose for reproducible setup
│  └─ ✓ Demo-ready application

---

FEATURE BREAKDOWN (by priority):
┌────────────────────────────────────────┐
│ MVP SCOPE (1 Week)                     │
├────────────────────────────────────────┤
│ ✓ User Auth (Register/Login)           │
│ ✓ Chat Interface (Send/Receive msgs)   │
│ ✓ Sentiment Analysis (Basic)           │
│ ✓ Intent Classification (5 intents)    │
│ ✓ Crisis Detection (Keywords)          │
│ ✓ Response Generation (Templates + LLM)│
│ ✓ Mood Tracking (1-10 scale)           │
│ ✓ PHQ-9 Assessment                     │
│ ✓ Resource Recommendations (Simple)    │
│ ✓ Basic UI (Responsive)                │
├────────────────────────────────────────┤
│ ✗ Vector embeddings/semantic search    │
│ ✗ Multi-language support               │
│ ✗ Advanced analytics                   │
│ ✗ Mobile app                           │
│ ✗ AWS deployment (local only)          │
│ ✗ WebSocket real-time (use polling)    │
└────────────────────────────────────────┘
```

---

## Project Structure (Simplified)

```
mental-health-chatbot-mvp/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                      # FastAPI app
│   │   ├── database.py                  # SQLAlchemy setup
│   │   │
│   │   ├── models.py                    # ORM models (User, Chat, Mood, Assessment)
│   │   ├── schemas.py                   # Pydantic schemas
│   │   │
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py                  # Login, register
│   │   │   ├── chat.py                  # Chat endpoints
│   │   │   ├── mood.py                  # Mood tracking
│   │   │   └── assessment.py            # PHQ-9, resources
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── chatbot.py               # Main chatbot logic
│   │   │   ├── sentiment.py             # TextBlob/VADER
│   │   │   ├── intent.py                # Intent classifier
│   │   │   ├── crisis.py                # Crisis detection
│   │   │   ├── llm.py                   # Ollama integration
│   │   │   └── resources.py             # Resource matching
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py                  # JWT helpers
│   │   │   └── constants.py             # Intents, resources, etc.
│   │   │
│   │   └── ml/
│   │       ├── __init__.py
│   │       ├── intents.json             # Intent definitions
│   │       ├── resources.json           # Crisis hotlines, coping tools
│   │       ├── intent_model.pkl         # Trained classifier (after training)
│   │       └── training_data.csv        # Small training dataset
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_auth.py
│   │   └── test_chatbot.py
│   │
│   ├── pyproject.toml                   # Poetry dependencies
│   ├── .env.example
│   ├── Dockerfile
│   └── README.md
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── index.jsx
│   │   ├── App.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── LoginPage.jsx
│   │   │   ├── ChatPage.jsx
│   │   │   ├── MoodPage.jsx
│   │   │   ├── AssessmentPage.jsx
│   │   │   └── ResourcesPage.jsx
│   │   │
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── MoodLogger.jsx
│   │   │   ├── AssessmentForm.jsx
│   │   │   ├── ResourceCard.jsx
│   │   │   └── Navbar.jsx
│   │   │
│   │   ├── services/
│   │   │   ├── api.js                   # Axios instance
│   │   │   └── auth.js                  # Auth helpers
│   │   │
│   │   ├── store/
│   │   │   └── store.js                 # Zustand state
│   │   │
│   │   └── styles/
│   │       └── globals.css              # Tailwind
│   │
│   ├── package.json
│   ├── .env.example
│   └── README.md
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Getting Started (Day 1)

### 1. Initialize Project

```bash
# Create project directory
mkdir mental-health-chatbot-mvp
cd mental-health-chatbot-mvp

# Initialize Git
git init
git add .
git commit -m "Initial commit: Project structure"

# Create backend & frontend folders
mkdir backend frontend
```

### 2. Backend Setup

```bash
cd backend

# Initialize Poetry
poetry init

# Install core dependencies
poetry add fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-jose bcrypt \
           nltk textblob scikit-learn numpy pandas python-dotenv \
           langchain ollama requests

# Create app folder
mkdir app app/routes app/services app/utils app/ml tests

# Create Python files
touch app/__init__.py app/main.py app/database.py app/models.py app/schemas.py \
      app/routes/__init__.py app/routes/auth.py app/routes/chat.py app/routes/mood.py app/routes/assessment.py \
      app/services/__init__.py app/services/chatbot.py app/services/sentiment.py app/services/intent.py \
      app/services/crisis.py app/services/llm.py app/services/resources.py \
      app/utils/__init__.py app/utils/auth.py app/utils/constants.py \
      app/ml/__init__.py

# Create config files
touch .env.example Dockerfile .dockerignore

cd ..
```

### 3. Frontend Setup

```bash
cd frontend

# Create React app
npx create-react-app . --template cra-template

# Install additional dependencies
npm install zustand axios tailwindcss react-router-dom recharts

# Create folders
mkdir src/pages src/components src/services src/store src/styles

# Create component files
touch src/pages/{LoginPage,ChatPage,MoodPage,AssessmentPage,ResourcesPage}.jsx \
      src/components/{ChatWindow,MoodLogger,AssessmentForm,ResourceCard,Navbar}.jsx \
      src/services/{api,auth}.js \
      src/store/store.js \
      src/styles/globals.css

cd ..
```

### 4. Database Setup

```bash
# Install PostgreSQL (macOS: brew install postgresql)
# Create database
createdb mental_health_mvp

# Verify connection
psql mental_health_mvp -c "SELECT 1"
```

---

## Day 1 Backend Boilerplate

### `backend/app/main.py`

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import auth, chat, mood, assessment

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mental Health Chatbot MVP", version="0.1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(mood.router, prefix="/api/mood", tags=["mood"])
app.include_router(assessment.router, prefix="/api/assessment", tags=["assessment"])

@app.get("/")
def read_root():
    return {"message": "Mental Health Chatbot MVP"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### `backend/app/database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost/mental_health_mvp"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### `backend/app/models.py`

```python
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import uuid

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationships
    chat_messages = relationship("ChatMessage", back_populates="user")
    mood_logs = relationship("MoodLog", back_populates="user")
    assessments = relationship("Assessment", back_populates="user")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    user_message = Column(Text)
    bot_response = Column(Text)
    intent = Column(String(100))
    sentiment_label = Column(String(20))  # POSITIVE, NEGATIVE, NEUTRAL
    sentiment_score = Column(Float)  # -1.0 to 1.0
    crisis_level = Column(String(50))  # SAFE, LOW_RISK, MODERATE_RISK, CRITICAL
    created_at = Column(DateTime, default=datetime.now, index=True)
    
    # Relationships
    user = relationship("User", back_populates="chat_messages")

class MoodLog(Base):
    __tablename__ = "mood_logs"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    mood_score = Column(Integer)  # 1-10
    notes = Column(Text, nullable=True)
    sleep_quality = Column(Integer, nullable=True)  # 1-10
    energy_level = Column(Integer, nullable=True)  # 1-10
    stress_level = Column(Integer, nullable=True)  # 1-10
    created_at = Column(DateTime, default=datetime.now, index=True)
    
    # Relationships
    user = relationship("User", back_populates="mood_logs")

class Assessment(Base):
    __tablename__ = "assessments"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    assessment_type = Column(String(50))  # PHQ-9, GAD-7
    score = Column(Integer)  # 0-27 for PHQ-9
    severity_level = Column(String(50))  # Minimal, Mild, Moderate, etc.
    created_at = Column(DateTime, default=datetime.now, index=True)
    
    # Relationships
    user = relationship("User", back_populates="assessments")
```

### `backend/app/schemas.py`

```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Auth Schemas
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

# Chat Schemas
class ChatMessageCreate(BaseModel):
    message: str

class ChatMessageResponse(BaseModel):
    id: str
    user_message: str
    bot_response: str
    intent: Optional[str]
    sentiment_label: Optional[str]
    sentiment_score: Optional[float]
    crisis_level: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

# Mood Schemas
class MoodLogCreate(BaseModel):
    mood_score: int  # 1-10
    notes: Optional[str] = None
    sleep_quality: Optional[int] = None
    energy_level: Optional[int] = None
    stress_level: Optional[int] = None

class MoodLogResponse(BaseModel):
    id: str
    mood_score: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Assessment Schemas
class PHQ9Response(BaseModel):
    responses: list[int]  # 9 responses (0-3 each)

class AssessmentResponse(BaseModel):
    id: str
    assessment_type: str
    score: int
    severity_level: str
    created_at: datetime
    
    class Config:
        from_attributes = True
```

### `backend/app/utils/auth.py`

```python
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
```

---

## Day 2 Authentication Routes

### `backend/app/routes/auth.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserLogin, UserResponse, Token
from app.utils.auth import hash_password, verify_password, create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    
    # Check if user exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create user
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """Login user and return access token"""
    
    # Find user
    db_user = db.query(User).filter(User.email == credentials.email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Verify password
    if not verify_password(credentials.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Create token
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": db_user.id},
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def get_current_user(token: str, db: Session = Depends(get_db)):
    """Get current user from token"""
    
    from app.utils.auth import decode_token
    
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user_id = payload.get("sub")
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user
```

---

## Day 3 Sentiment & Intent

### `backend/app/services/sentiment.py`

```python
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download required NLTK data
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
    
    def analyze(self, text: str) -> dict:
        """Analyze sentiment of text"""
        
        # VADER analysis
        vader_scores = self.vader.polarity_scores(text)
        compound = vader_scores['compound']
        
        # Classify
        if compound >= 0.05:
            label = "POSITIVE"
        elif compound <= -0.05:
            label = "NEGATIVE"
        else:
            label = "NEUTRAL"
        
        return {
            "label": label,
            "score": compound,  # -1.0 to 1.0
            "intensity": abs(compound)
        }
```

### `backend/app/services/intent.py`

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import json
import os

class IntentClassifier:
    def __init__(self):
        self.model_path = "app/ml/intent_model.pkl"
        self.vectorizer_path = "app/ml/vectorizer.pkl"
        self.intents = self.load_intents()
        self.pipeline = None
        self.load_or_train_model()
    
    def load_intents(self):
        """Load intents from JSON"""
        with open("app/ml/intents.json", "r") as f:
            return json.load(f)
    
    def load_or_train_model(self):
        """Load trained model or train new one"""
        if os.path.exists(self.model_path):
            with open(self.model_path, "rb") as f:
                self.pipeline = pickle.load(f)
        else:
            self.train_model()
    
    def train_model(self):
        """Train intent classifier"""
        from sklearn.pipeline import Pipeline
        
        # Prepare training data
        messages = []
        labels = []
        
        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                messages.append(pattern)
                labels.append(intent["tag"])
        
        # Create pipeline
        self.pipeline = Pipeline([
            ("tfidf", TfidfVectorizer(max_features=1000, stop_words="english")),
            ("clf", LogisticRegression(max_iter=200, random_state=42))
        ])
        
        # Train
        self.pipeline.fit(messages, labels)
        
        # Save
        with open(self.model_path, "wb") as f:
            pickle.dump(self.pipeline, f)
    
    def predict(self, text: str) -> tuple:
        """Predict intent"""
        intent = self.pipeline.predict([text])[0]
        confidence = max(self.pipeline.predict_proba([text])[0])
        return intent, confidence
```

### `backend/app/ml/intents.json`

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["hello", "hi", "hey", "good morning", "hello there", "greetings"],
      "responses": ["Hello! How are you feeling today?", "Hi there! What brings you here?"],
      "resources": []
    },
    {
      "tag": "anxiety",
      "patterns": ["anxious", "nervous", "worried", "panic", "anxious attack", "panic attack"],
      "responses": ["I understand anxiety can be overwhelming. Let's work through this together."],
      "resources": ["breathing_exercise", "grounding"]
    },
    {
      "tag": "depression",
      "patterns": ["sad", "depressed", "hopeless", "worthless", "no point"],
      "responses": ["I hear you. These feelings are valid. Would you like to try some coping strategies?"],
      "resources": ["crisis_hotline", "depression_resources"]
    },
    {
      "tag": "stress",
      "patterns": ["stressed", "overwhelmed", "burnout", "pressure", "stressed out"],
      "responses": ["Stress is challenging. Let's identify some ways to manage it."],
      "resources": ["stress_management", "breathing_exercise"]
    },
    {
      "tag": "sleep",
      "patterns": ["insomnia", "sleep", "tired", "exhausted", "can't sleep"],
      "responses": ["Sleep issues can affect everything. Let's work on this together."],
      "resources": ["sleep_hygiene"]
    }
  ]
}
```

---

## Day 4 Chat Endpoint

### `backend/app/routes/chat.py`

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ChatMessage, User
from app.schemas import ChatMessageCreate, ChatMessageResponse
from app.services.chatbot import ChatbotEngine
from app.utils.auth import decode_token
from fastapi import Header
from typing import Optional

router = APIRouter()
chatbot = ChatbotEngine()

def get_user_from_token(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    """Extract user from bearer token"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")
    
    token = authorization.replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user_id = payload.get("sub")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.post("/message", response_model=ChatMessageResponse)
def send_message(
    chat: ChatMessageCreate,
    user: User = Depends(get_user_from_token),
    db: Session = Depends(get_db)
):
    """Send message and get bot response"""
    
    # Process message
    result = chatbot.process_message(chat.message)
    
    # Save to database
    db_message = ChatMessage(
        user_id=user.id,
        user_message=chat.message,
        bot_response=result["response"],
        intent=result["intent"],
        sentiment_label=result["sentiment"]["label"],
        sentiment_score=result["sentiment"]["score"],
        crisis_level=result["crisis_level"]
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    
    return db_message

@router.get("/history", response_model=list[ChatMessageResponse])
def get_chat_history(
    user: User = Depends(get_user_from_token),
    db: Session = Depends(get_db),
    limit: int = 50
):
    """Get user's chat history"""
    
    messages = db.query(ChatMessage).filter(
        ChatMessage.user_id == user.id
    ).order_by(ChatMessage.created_at.desc()).limit(limit).all()
    
    return messages[::-1]  # Reverse to show oldest first
```

### `backend/app/services/chatbot.py`

```python
from app.services.sentiment import SentimentAnalyzer
from app.services.intent import IntentClassifier
from app.services.crisis import CrisisDetector
import json
import random

class ChatbotEngine:
    def __init__(self):
        self.sentiment_analyzer = SentimentAnalyzer()
        self.intent_classifier = IntentClassifier()
        self.crisis_detector = CrisisDetector()
        self.intents = self.load_intents()
    
    def load_intents(self):
        """Load intent templates"""
        with open("app/ml/intents.json", "r") as f:
            return json.load(f)
    
    def process_message(self, message: str) -> dict:
        """Process user message and generate response"""
        
        # Sentiment analysis
        sentiment = self.sentiment_analyzer.analyze(message)
        
        # Intent classification
        intent, confidence = self.intent_classifier.predict(message)
        
        # Crisis detection
        crisis_level = self.crisis_detector.assess(message, sentiment)
        
        # Generate response
        response = self.generate_response(intent, sentiment, crisis_level)
        
        return {
            "response": response,
            "intent": intent,
            "sentiment": sentiment,
            "crisis_level": crisis_level
        }
    
    def generate_response(self, intent: str, sentiment: dict, crisis_level: str) -> str:
        """Generate appropriate response"""
        
        # Crisis escalation
        if crisis_level == "CRITICAL":
            return "I'm concerned about what you shared. Please reach out to 988 (Suicide & Crisis Lifeline) immediately. You're not alone. 💙"
        
        # Find intent template
        intent_data = next(
            (i for i in self.intents["intents"] if i["tag"] == intent),
            None
        )
        
        if intent_data:
            return random.choice(intent_data["responses"])
        
        return "I understand. Can you tell me more about how you're feeling?"
```

### `backend/app/services/crisis.py`

```python
class CrisisDetector:
    def __init__(self):
        self.crisis_keywords = [
            "suicide", "kill myself", "end my life", "hurt myself",
            "no point living", "self harm", "cut myself"
        ]
    
    def assess(self, text: str, sentiment: dict) -> str:
        """Assess crisis level"""
        
        lower_text = text.lower()
        
        # Check for crisis keywords
        has_crisis_keywords = any(kw in lower_text for kw in self.crisis_keywords)
        
        # Very negative sentiment + keywords = critical
        if has_crisis_keywords or (sentiment["score"] < -0.8):
            return "CRITICAL"
        
        # Very negative sentiment
        if sentiment["score"] < -0.6:
            return "HIGH"
        
        # Somewhat negative
        if sentiment["score"] < -0.2:
            return "MODERATE"
        
        return "SAFE"
```

---

## Day 5 Frontend Boilerplate

### `frontend/src/services/api.js`

```javascript
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authAPI = {
  register: (username, email, password) =>
    api.post('/auth/register', { username, email, password }),
  login: (email, password) =>
    api.post('/auth/login', { email, password }),
  me: () => api.get('/auth/me'),
};

export const chatAPI = {
  sendMessage: (message) =>
    api.post('/chat/message', { message }),
  getHistory: (limit = 50) =>
    api.get(`/chat/history?limit=${limit}`),
};

export const moodAPI = {
  logMood: (mood_score, notes = '') =>
    api.post('/mood/log', { mood_score, notes }),
  getHistory: (days = 30) =>
    api.get(`/mood/history?days=${days}`),
};

export const assessmentAPI = {
  startPHQ9: () => api.get('/assessment/phq9'),
  submitPHQ9: (responses) =>
    api.post('/assessment/phq9', { responses }),
  getResources: () => api.get('/assessment/resources'),
};
```

### `frontend/src/store/store.js`

```javascript
import create from 'zustand';

export const useStore = create((set) => ({
  // Auth state
  user: null,
  token: localStorage.getItem('token') || null,
  isAuthenticated: !!localStorage.getItem('token'),

  setAuth: (user, token) =>
    set({
      user,
      token,
      isAuthenticated: true,
    }),

  logout: () => {
    localStorage.removeItem('token');
    set({
      user: null,
      token: null,
      isAuthenticated: false,
    });
  },

  // Chat state
  messages: [],
  addMessage: (message) =>
    set((state) => ({
      messages: [...state.messages, message],
    })),

  setMessages: (messages) =>
    set({ messages }),

  // Mood state
  moodLogs: [],
  addMoodLog: (log) =>
    set((state) => ({
      moodLogs: [...state.moodLogs, log],
    })),

  setMoodLogs: (logs) =>
    set({ moodLogs: logs }),
}));
```

### `frontend/src/pages/ChatPage.jsx`

```jsx
import React, { useState, useEffect } from 'react';
import { useStore } from '../store/store';
import { chatAPI } from '../services/api';
import ChatWindow from '../components/ChatWindow';

export default function ChatPage() {
  const { messages, addMessage, setMessages } = useStore();
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadChatHistory();
  }, []);

  const loadChatHistory = async () => {
    try {
      const response = await chatAPI.getHistory();
      setMessages(response.data);
    } catch (error) {
      console.error('Error loading chat history:', error);
    }
  };

  const handleSendMessage = async () => {
    if (!input.trim()) return;

    setLoading(true);
    try {
      const response = await chatAPI.sendMessage(input);
      addMessage(response.data);
      setInput('');
    } catch (error) {
      console.error('Error sending message:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <ChatWindow messages={messages} loading={loading} />
      
      <div className="p-4 bg-white border-t">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
            placeholder="Type your message..."
            className="flex-1 p-2 border rounded"
            disabled={loading}
          />
          <button
            onClick={handleSendMessage}
            disabled={loading}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:opacity-50"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
```

### `frontend/src/components/ChatWindow.jsx`

```jsx
import React, { useEffect, useRef } from 'react';

export default function ChatWindow({ messages, loading }) {
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4">
      {messages.map((msg) => (
        <div key={msg.id}>
          {/* User message */}
          <div className="flex justify-end mb-2">
            <div className="bg-blue-500 text-white p-3 rounded-lg max-w-xs">
              {msg.user_message}
            </div>
          </div>

          {/* Bot response */}
          <div className="flex justify-start mb-4">
            <div className="bg-gray-300 text-gray-900 p-3 rounded-lg max-w-xs">
              {msg.bot_response}
            </div>
          </div>

          {/* Sentiment & intent info */}
          <div className="text-xs text-gray-500 mb-2">
            Intent: {msg.intent} | Sentiment: {msg.sentiment_label} ({msg.sentiment_score.toFixed(2)})
          </div>

          {/* Crisis indicator */}
          {msg.crisis_level !== 'SAFE' && (
            <div className={`p-2 rounded text-xs mb-2 ${
              msg.crisis_level === 'CRITICAL' ? 'bg-red-200' : 'bg-yellow-200'
            }`}>
              ⚠️ {msg.crisis_level}
            </div>
          )}
        </div>
      ))}

      {loading && (
        <div className="flex justify-start">
          <div className="bg-gray-300 p-3 rounded-lg">Typing...</div>
        </div>
      )}

      <div ref={messagesEndRef} />
    </div>
  );
}
```

---

## Docker Compose Setup

### `docker-compose.yml` (root)

```yaml
version: '3.8'

services:
  # PostgreSQL Database
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: mental_health_mvp
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Backend API
  backend:
    build: ./backend
    command: poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:postgres@db:5432/mental_health_mvp
      SECRET_KEY: dev-secret-key
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./backend:/app

  # Frontend
  frontend:
    build: ./frontend
    command: npm start
    ports:
      - "3000:3000"
    environment:
      REACT_APP_API_URL: http://localhost:8000/api
    volumes:
      - ./frontend/src:/app/src

volumes:
  postgres_data:
```

---

## Quick Start Script

### `setup.sh` (root)

```bash
#!/bin/bash

echo "🚀 Mental Health Chatbot MVP - Setup"

# Create .env files
echo "Creating .env files..."
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Update .env with defaults
sed -i 's|DATABASE_URL=.*|DATABASE_URL=postgresql://postgres:postgres@localhost/mental_health_mvp|' backend/.env
sed -i 's|REACT_APP_API_URL=.*|REACT_APP_API_URL=http://localhost:8000/api|' frontend/.env

echo "✓ .env files created"

echo ""
echo "📦 Option 1: Using Docker Compose"
echo "  Run: docker-compose up"
echo ""

echo "📦 Option 2: Local Setup"
echo ""
echo "  Backend:"
echo "    cd backend"
echo "    poetry install"
echo "    poetry run python -m app.main"
echo ""
echo "  Frontend (new terminal):"
echo "    cd frontend"
echo "    npm install"
echo "    npm start"
echo ""

echo "💾 Database Setup (if local):"
echo "  createdb mental_health_mvp"
echo ""

echo "🎯 Access:"
echo "  Frontend: http://localhost:3000"
echo "  Backend:  http://localhost:8000"
echo "  Docs:     http://localhost:8000/docs"
```

---

## README.md

```markdown
# Mental Health Chatbot MVP

**1-Week Rapid Prototype** | Python + React + FastAPI + PostgreSQL

## Quick Start

### Option 1: Docker Compose (Recommended)

```bash
bash setup.sh
docker-compose up
```

Access: `http://localhost:3000`

### Option 2: Local Development

```bash
# Backend
cd backend
poetry install
poetry run python -m app.main

# Frontend (new terminal)
cd frontend
npm install
npm start
```

## Features (MVP)

- ✓ User authentication (register/login)
- ✓ Chat interface with bot responses
- ✓ Sentiment analysis (VADER)
- ✓ Intent classification (5 intents)
- ✓ Crisis detection (keyword-based)
- ✓ Mood tracking (1-10 scale)
- ✓ PHQ-9 assessment
- ✓ Basic resource recommendations

## API Endpoints

- `POST /api/auth/register` - Register user
- `POST /api/auth/login` - Login user
- `POST /api/chat/message` - Send message
- `GET /api/chat/history` - Get chat history
- `POST /api/mood/log` - Log mood
- `POST /api/assessment/phq9` - Submit PHQ-9

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, PostgreSQL
- **Frontend:** React, Zustand, Tailwind CSS
- **NLP:** TextBlob, VADER, Scikit-learn
- **LLM:** Ollama (optional, Day 4+)

## Next Steps (After MVP)

- [ ] Vector embeddings for semantic search
- [ ] WebSocket for real-time chat
- [ ] AWS deployment
- [ ] Mobile app
- [ ] Advanced ML models
```

---

## Daily Commit Checklist

```bash
# Day 1
git add .
git commit -m "Day 1: Project setup, models, database schema"

# Day 2
git commit -m "Day 2: User authentication (register/login)"

# Day 3
git commit -m "Day 3: Sentiment analysis, intent classification, crisis detection"

# Day 4
git commit -m "Day 4: Chat endpoint, template responses"

# Day 5
git commit -m "Day 5: React UI, authentication, chat interface"

# Day 6
git commit -m "Day 6: Mood tracking, PHQ-9 assessment, resources"

# Day 7
git commit -m "Day 7: Testing, documentation, Docker setup"
```

---

## Timeline Visual

```
WEEK 1 PROGRESS
┌──────────────────────────────────────────────────────────────┐
│ Day 1 │ Day 2 │ Day 3 │ Day 4 │ Day 5 │ Day 6 │ Day 7        │
│ 14%   │ 28%   │ 42%   │ 57%   │ 71%   │ 85%   │ 100% ✓       │
└──────────────────────────────────────────────────────────────┘

FEATURE IMPLEMENTATION
┌────────────────────────────────────┐
│ Auth (Day 1-2)       ████████░░░░░ │
│ NLP (Day 3-4)        ░░░░████████░ │
│ Frontend (Day 5)     ░░░░░░░████░░ │
│ Assessments (Day 6)  ░░░░░░░░░████ │
│ Testing (Day 7)      ░░░░░░░░░░░░░ │
└────────────────────────────────────┘
```
