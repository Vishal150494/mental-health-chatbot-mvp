# Quick Start: File Templates & Getting Started

## Files to Create First (Day 1)

### Step 1: Initialize Git & Folders (5 min)

```bash
# Create project
mkdir mental-health-chatbot-mvp
cd mental-health-chatbot-mvp

# Initialize git
git init
echo "node_modules/
.env
*.pyc
__pycache__/
.DS_Store
*.pkl
venv/" > .gitignore

git add .gitignore
git commit -m "Initial commit: .gitignore"

# Create main folders
mkdir backend frontend
cd backend
mkdir app app/routes app/services app/utils app/ml tests
touch app/__init__.py

cd ../frontend
mkdir -p src/{pages,components,services,store,styles}

cd ..
```

### Step 2: Backend Initialization (10 min)

**File: `backend/pyproject.toml`**

```toml
[tool.poetry]
name = "mental-health-chatbot"
version = "0.1.0"
description = "Mental health support chatbot MVP"
authors = ["Your Name <email@example.com>"]

[tool.poetry.dependencies]
python = "^3.10"
fastapi = "^0.104.1"
uvicorn = "^0.24.0"
sqlalchemy = "^2.0"
psycopg2-binary = "^2.9"
pydantic = "^2.0"
python-jose = "^3.3"
bcrypt = "^4.1"
scikit-learn = "^1.3"
nltk = "^3.8"
textblob = "^0.17"
python-dotenv = "^1.0"
langchain = "^0.1"
requests = "^2.31"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

**File: `backend/.env.example`**

```
DATABASE_URL=postgresql://postgres:postgres@localhost/mental_health_mvp
SECRET_KEY=dev-secret-key-change-in-production
OLLAMA_URL=http://localhost:11434
```

**File: `backend/Dockerfile`**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y postgresql-client

# Install Poetry
RUN pip install poetry

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root

# Copy app code
COPY app ./app

# Expose port
EXPOSE 8000

# Run app
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Step 3: Frontend Initialization (5 min)

**File: `frontend/package.json`**

```json
{
  "name": "mental-health-chatbot",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.6.0",
    "zustand": "^4.4.0",
    "react-router-dom": "^6.18.0",
    "recharts": "^2.10.0",
    "tailwindcss": "^3.3.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "react-scripts": "5.0.1"
  }
}
```

**File: `frontend/.env.example`**

```
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_ENV=development
```

---

## Day 1 Complete File List

### Backend Files to Create

**`backend/app/main.py`**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mental Health Chatbot MVP", version="0.1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Mental Health Chatbot MVP"}

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**`backend/app/database.py`**
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost/mental_health_mvp"
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

**`backend/app/models.py`**
```python
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey
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
    sentiment_label = Column(String(20))
    sentiment_score = Column(Float)
    crisis_level = Column(String(50))
    created_at = Column(DateTime, default=datetime.now, index=True)
    
    user = relationship("User", back_populates="chat_messages")

class MoodLog(Base):
    __tablename__ = "mood_logs"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    mood_score = Column(Integer)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now, index=True)
    
    user = relationship("User", back_populates="mood_logs")

class Assessment(Base):
    __tablename__ = "assessments"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    assessment_type = Column(String(50))
    score = Column(Integer)
    severity_level = Column(String(50))
    created_at = Column(DateTime, default=datetime.now, index=True)
    
    user = relationship("User", back_populates="assessments")
```

**`backend/app/schemas.py`**
```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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
```

**`backend/app/utils/__init__.py`**
```python
# Utils module
```

**`backend/app/utils/constants.py`**
```python
# Intent tags for classification
INTENT_TAGS = [
    "greeting",
    "anxiety", 
    "depression",
    "stress",
    "sleep"
]

# Crisis keywords
CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "end my life",
    "hurt myself",
    "self harm"
]

# Crisis hotlines
CRISIS_RESOURCES = {
    "US": {
        "name": "988 Suicide & Crisis Lifeline",
        "number": "988",
        "url": "https://988lifeline.org"
    },
    "UK": {
        "name": "Samaritans",
        "number": "116 123",
        "url": "https://www.samaritans.org.uk"
    }
}
```

---

## Frontend Files to Create

**`frontend/src/index.jsx`**
```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles/globals.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

**`frontend/src/App.jsx`**
```jsx
import React, { useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useStore } from './store/store';
import LoginPage from './pages/LoginPage';
import ChatPage from './pages/ChatPage';
import MoodPage from './pages/MoodPage';

export default function App() {
  const { isAuthenticated } = useStore();

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route
          path="/chat"
          element={isAuthenticated ? <ChatPage /> : <Navigate to="/login" />}
        />
        <Route
          path="/mood"
          element={isAuthenticated ? <MoodPage /> : <Navigate to="/login" />}
        />
        <Route
          path="/"
          element={isAuthenticated ? <Navigate to="/chat" /> : <Navigate to="/login" />}
        />
      </Routes>
    </BrowserRouter>
  );
}
```

**`frontend/src/store/store.js`**
```javascript
import create from 'zustand';

export const useStore = create((set) => ({
  user: null,
  token: localStorage.getItem('token') || null,
  isAuthenticated: !!localStorage.getItem('token'),

  setAuth: (user, token) => {
    localStorage.setItem('token', token);
    set({ user, token, isAuthenticated: true });
  },

  logout: () => {
    localStorage.removeItem('token');
    set({ user: null, token: null, isAuthenticated: false });
  },

  messages: [],
  addMessage: (message) => set((state) => ({
    messages: [...state.messages, message],
  })),

  setMessages: (messages) => set({ messages }),
}));
```

**`frontend/src/services/api.js`**
```javascript
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: { 'Content-Type': 'application/json' },
});

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
};

export const chatAPI = {
  sendMessage: (message) => api.post('/chat/message', { message }),
  getHistory: (limit = 50) => api.get(`/chat/history?limit=${limit}`),
};

export const moodAPI = {
  logMood: (mood_score, notes = '') =>
    api.post('/mood/log', { mood_score, notes }),
};
```

**`frontend/src/pages/LoginPage.jsx`**
```jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useStore } from '../store/store';
import { authAPI } from '../services/api';

export default function LoginPage() {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { setAuth } = useStore();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      if (isLogin) {
        const response = await authAPI.login(email, password);
        setAuth({ email }, response.data.access_token);
      } else {
        await authAPI.register(username, email, password);
        const response = await authAPI.login(email, password);
        setAuth({ username, email }, response.data.access_token);
      }
      navigate('/chat');
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center">
      <div className="bg-white rounded-lg shadow-xl p-8 w-full max-w-md">
        <h1 className="text-3xl font-bold text-center mb-2">
          Mental Health Chat
        </h1>
        <p className="text-gray-600 text-center mb-6">
          {isLogin ? 'Welcome back' : 'Create an account'}
        </p>

        <form onSubmit={handleSubmit} className="space-y-4">
          {!isLogin && (
            <input
              type="text"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500"
              required
            />
          )}
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500"
            required
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-3 border rounded-lg focus:outline-none focus:border-blue-500"
            required
          />

          {error && <div className="p-3 bg-red-100 text-red-700 rounded">{error}</div>}

          <button
            type="submit"
            disabled={loading}
            className="w-full p-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 font-semibold"
          >
            {loading ? 'Loading...' : isLogin ? 'Login' : 'Sign Up'}
          </button>
        </form>

        <div className="mt-4 text-center">
          <button
            onClick={() => setIsLogin(!isLogin)}
            className="text-blue-500 hover:underline"
          >
            {isLogin ? "Don't have an account? Sign up" : 'Already have an account? Login'}
          </button>
        </div>
      </div>
    </div>
  );
}
```

---

## Setup Commands (Copy & Paste)

### Backend Setup
```bash
cd backend
poetry install
cp .env.example .env
# Edit .env: set DATABASE_URL to your PostgreSQL connection
poetry run python -m app.main
```

### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env
npm start
```

### Database Setup
```bash
# macOS
brew install postgresql
createdb mental_health_mvp

# Ubuntu/Linux
sudo apt install postgresql
createdb mental_health_mvp

# Test connection
psql mental_health_mvp -c "SELECT 1"
```

### Docker Setup
```bash
# From root directory
docker-compose up
```

---

## Verification Checklist (Day 1 End)

- [ ] Git repository initialized
- [ ] Backend folder structure created
- [ ] Frontend folder structure created
- [ ] PostgreSQL database created
- [ ] Poetry dependencies installed
- [ ] npm dependencies installed
- [ ] `.env` files created from examples
- [ ] FastAPI app starts without errors
- [ ] React app starts without errors
- [ ] Database tables created successfully
- [ ] First commit made to GitHub

---

## Common Issues & Solutions

**Issue: "connection refused" for PostgreSQL**
```bash
# Start PostgreSQL service
# macOS
brew services start postgresql

# Ubuntu
sudo service postgresql start

# Verify
psql -U postgres -d template1 -c "SELECT 1"
```

**Issue: "Poetry not found"**
```bash
pip install poetry
poetry --version
```

**Issue: Port 8000 already in use**
```bash
# Find process on port 8000
lsof -i :8000

# Kill process
kill -9 <PID>
```

**Issue: npm install fails**
```bash
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

---

## Next: Day 2 Quick Start

When ready to start Day 2, run:
```bash
# Terminal 1: Backend
cd backend
poetry run python -m app.main

# Terminal 2: Frontend
cd frontend
npm start

# Terminal 3: Development watch
cd backend
poetry run pytest --watch
```

---

## Resources

- FastAPI Docs: http://localhost:8000/docs
- React DevTools: https://chrome.google.com/webstore/detail/react-developer-tools
- Postman: https://www.postman.com/downloads/
- PostgreSQL Docs: https://www.postgresql.org/docs/
