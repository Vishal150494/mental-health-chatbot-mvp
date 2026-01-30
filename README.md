# Mental Health Chatbot MVP

An AI-powered mental health check-in chatbot providing supportive conversations, mood tracking, and resource recommendations.

> ⚠️ **Disclaimer**: This chatbot is not a replacement for professional mental health care. If you're in crisis, please call 988 (Suicide & Crisis Lifeline) or text HOME to 741741 (Crisis Text Line).

## Features

- 💬 **Supportive Chat** - NLP-powered conversations with intent classification and sentiment analysis
- 🚨 **Crisis Detection** - Automatic detection of crisis keywords with immediate resource display
- 📊 **Mood Tracking** - Daily mood logging (1-10 scale) with trend analysis
- 📋 **PHQ-9 Assessment** - Validated depression screening with scoring and recommendations
- 📚 **Resource Matching** - Semantic search for relevant mental health resources
- 🤖 **Hybrid Responses** - Template-based + LLM (Ollama) for natural conversations

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.13, FastAPI, SQLAlchemy, Pydantic |
| Database | PostgreSQL 18 |
| NLP/ML | scikit-learn, TextBlob, Sentence-Transformers |
| LLM | Ollama (Llama 3.2 / Mistral) |
| Deployment | Docker Compose |

## Quick Start

### 1. Clone & Setup

```bash
git clone <repo-url>
cd mental-health-chatbot-mvp
cp backend/.env.example backend/.env
```

### 2. Start with Docker Compose

```bash
docker-compose up -d
```

This starts:
- PostgreSQL on port 5432
- Backend API on port 8000
- Ollama LLM on port 11434

### 3. Pull LLM Model

```bash
docker exec -it mh-ollama ollama pull llama3.2
```

### 4. Verify

Open http://localhost:8000/docs to see Swagger UI.

## Local Development

### Prerequisites
- Python 3.13+
- Poetry
- PostgreSQL 15+

### Setup

```bash
# Install dependencies
poetry install

# Start PostgreSQL (or use Docker)
docker run -d --name mh-postgres \
  -e POSTGRES_USER=mh_user \
  -e POSTGRES_PASSWORD=mh_password \
  -e POSTGRES_DB=mental_health_db \
  -p 5432:5432 postgres:15

# Run backend
cd backend
poetry run uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login, get JWT token |
| GET | `/auth/me` | Get current user |
| POST | `/chat/send` | Send message, get response |
| GET | `/chat/history` | Get conversation history |
| POST | `/mood/log` | Log mood (1-10) |
| GET | `/mood/history` | Get mood history + trends |
| POST | `/assessment/phq9` | Submit PHQ-9 assessment |
| GET | `/health` | Health check |

## Project Structure

```
mental-health-chatbot-mvp/
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI app
│   │   ├── database.py       # SQLAlchemy setup
│   │   ├── models.py         # ORM models
│   │   ├── schemas.py        # Pydantic schemas
│   │   ├── routes/           # API endpoints
│   │   └── services/         # Business logic (NLP, LLM)
│   └── Dockerfile
├── directives/               # SOPs for AI agent
├── execution/                # Deterministic scripts
├── docker-compose.yml
└── README.md
```

## Safety Features

- ✅ Crisis keyword detection with severity scoring
- ✅ Immediate crisis resource display for high-risk content
- ✅ LLM constrained to supportive, non-diagnostic responses
- ✅ PHQ-9 question 9 flagged for suicidal ideation
- ✅ No sensitive conversation content logged

## License

MIT
