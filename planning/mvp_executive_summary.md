# 1-Week MVP: Executive Summary & Action Plan

**Created:** January 26, 2026  
**Scope:** Reduced from full production architecture to 1-week exploration  
**Status:** Ready to implement

---

## What Changed from Full Architecture?

| Aspect | Full Architecture | 1-Week MVP |
|--------|-------------------|-----------|
| **Duration** | 12+ weeks | 7 days |
| **Code Lines** | 10,000+ | ~2,000 |
| **Features** | All 12+ features | Core 9 features |
| **NLP Models** | Advanced ML + LLM | TextBlob + Scikit-learn |
| **Database** | Complex schema | Simplified (4 tables) |
| **Deployment** | AWS EC2/RDS | Local Docker Compose |
| **Testing** | Full test suite | Manual E2E only |
| **Documentation** | 80+ pages | Focused guides |
| **Performance** | Optimized | Functional only |

---

## Why This Works for Week 1

✅ **Achievable:** Each day has 4-6 hours of focused work  
✅ **Modular:** Can be extended after Day 7  
✅ **Testing:** Manual but thorough  
✅ **Learning:** Understand each component deeply  
✅ **Portfolio:** Demo-ready prototype  
✅ **Foundation:** Base for future expansion  

---

## Daily Breakdown

### Day 1: Foundation (Project + Database)
- Initialize Git repository
- Create folder structure
- Setup PostgreSQL database
- Create SQLAlchemy models & schemas
- Get FastAPI running locally
- **Time:** 6-8 hours
- **Outcome:** Backend skeleton + DB ready

### Day 2: Authentication (Login System)
- Implement JWT token generation
- Create registration endpoint
- Create login endpoint
- Add password hashing (bcrypt)
- Frontend login/register UI
- **Time:** 5-7 hours
- **Outcome:** Users can register & login

### Day 3: NLP Pipeline (Intelligence)
- Sentiment analysis (VADER)
- Intent classification (Scikit-learn)
- Crisis detection (keyword-based)
- Train intent classifier
- Integrate all into chat endpoint
- **Time:** 7-8 hours
- **Outcome:** Smart message analysis

### Day 4: Response Generation (Conversation)
- Template-based responses (intents.json)
- Optional: Ollama + LLM setup
- LangChain prompt management
- Save messages to database
- Test end-to-end flow
- **Time:** 6-7 hours
- **Outcome:** Bot can respond intelligently

### Day 5: Frontend UI (User Interface)
- React authentication pages
- Chat window component
- Message history display
- Mood logger form (1-10 scale)
- Tailwind CSS styling
- **Time:** 7-8 hours
- **Outcome:** Fully functional UI

### Day 6: Assessments & Resources (Features)
- PHQ-9 questionnaire form
- Scoring & interpretation
- Resource recommendations
- Crisis hotline display
- Resource-response linking
- **Time:** 6-7 hours
- **Outcome:** Complete feature set

### Day 7: Testing & Polish (Quality)
- Manual end-to-end testing
- Bug fixes & refinements
- Docker Compose setup
- README documentation
- Demo preparation
- **Time:** 5-6 hours
- **Outcome:** Demo-ready product

---

## File Count by Day

```
DAY 1: 12 files created
├─ backend/app/main.py
├─ backend/app/database.py
├─ backend/app/models.py
├─ backend/app/schemas.py
├─ backend/pyproject.toml
├─ backend/.env.example
├─ backend/Dockerfile
├─ frontend/package.json
├─ frontend/.env.example
├─ docker-compose.yml
├─ .gitignore
└─ README.md

DAY 2: +5 files
├─ backend/app/utils/auth.py
├─ backend/app/routes/auth.py
├─ frontend/src/services/api.js
├─ frontend/src/pages/LoginPage.jsx
└─ frontend/src/store/store.js

DAY 3: +4 files
├─ backend/app/services/sentiment.py
├─ backend/app/services/intent.py
├─ backend/app/ml/intents.json
└─ backend/app/ml/training_data.csv

DAY 4: +3 files
├─ backend/app/services/chatbot.py
├─ backend/app/services/crisis.py
└─ backend/app/services/llm.py (optional)

DAY 5: +6 files
├─ frontend/src/pages/ChatPage.jsx
├─ frontend/src/components/ChatWindow.jsx
├─ frontend/src/pages/MoodPage.jsx
├─ frontend/src/components/MoodLogger.jsx
├─ frontend/src/App.jsx
└─ frontend/src/index.jsx

DAY 6: +4 files
├─ backend/app/routes/mood.py
├─ backend/app/routes/assessment.py
├─ frontend/src/pages/AssessmentPage.jsx
└─ frontend/src/pages/ResourcesPage.jsx

DAY 7: +3 files
├─ backend/tests/test_auth.py
├─ TESTING_GUIDE.md
└─ DEPLOYMENT_GUIDE.md

TOTAL: 37 files (vs 80+ in full architecture)
```

---

## GitHub Commits Template

```bash
# Day 1
git commit -m "Day 1: Project setup, models, database schema"

# Day 2
git commit -m "Day 2: User authentication (register/login)"

# Day 3
git commit -m "Day 3: NLP pipeline (sentiment, intent, crisis detection)"

# Day 4
git commit -m "Day 4: Chatbot engine with response generation"

# Day 5
git commit -m "Day 5: React frontend (auth, chat, mood)"

# Day 6
git commit -m "Day 6: Assessment module and resources"

# Day 7
git commit -m "Day 7: Testing, documentation, and Docker setup"
```

---

## Environment Variables Needed

### Backend (`.env`)
```
DATABASE_URL=postgresql://postgres:postgres@localhost/mental_health_mvp
SECRET_KEY=dev-secret-key-change-in-production
OLLAMA_URL=http://localhost:11434 (optional)
```

### Frontend (`.env`)
```
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_ENV=development
```

---

## Dependencies Summary

### Backend (8 main packages)
- **Web:** FastAPI, Uvicorn
- **Database:** SQLAlchemy, psycopg2
- **Auth:** python-jose, bcrypt
- **NLP:** scikit-learn, nltk, textblob
- **Utilities:** pydantic, python-dotenv

### Frontend (6 main packages)
- **Framework:** React 18
- **State:** Zustand
- **HTTP:** Axios
- **Routing:** React Router
- **Charts:** Recharts
- **Styling:** Tailwind CSS

### Database
- PostgreSQL 14+

### Optional (for Day 4+)
- Ollama (local LLM)
- LangChain (prompt management)

---

## Success Metrics

### End of MVP
- ✓ User can register & login
- ✓ Chat window sends/receives messages
- ✓ Sentiment detected on all messages
- ✓ Intent classification >85% accurate
- ✓ Crisis keywords trigger alerts
- ✓ Mood tracked 1-10 scale
- ✓ PHQ-9 scoring works
- ✓ Resources recommended
- ✓ Runs on Docker locally
- ✓ Demo-ready

### Performance Targets (MVP, not optimized)
- Response time: <3 seconds/message
- Intent accuracy: >85%
- Sentiment accuracy: >80%
- Concurrent users: 10+ locally
- Uptime: Always (local)

---

## After Day 7: What's Next?

### Immediate Improvements (Days 8-10)
- [ ] WebSocket for real-time chat
- [ ] Vector embeddings for better resource matching
- [ ] Advanced crisis response flow
- [ ] User mood analytics dashboard
- [ ] More assessment types (GAD-7, PSQI)

### Medium Term (Weeks 2-4)
- [ ] AWS deployment (EC2 + RDS)
- [ ] Advanced ML (emotion recognition)
- [ ] Mobile app wrapper
- [ ] Email notifications
- [ ] Admin dashboard

### Long Term (Months 2-3)
- [ ] Therapist integration
- [ ] Peer support groups
- [ ] Advanced personalization
- [ ] Multi-language support
- [ ] Voice interaction

---

## Tools You'll Need

### Required
- Python 3.10+ (with Poetry)
- Node.js 18+ (with npm)
- PostgreSQL 14+
- Git
- Code editor (VS Code recommended)

### Optional but Recommended
- Postman (API testing)
- DBeaver (database GUI)
- React DevTools (browser extension)
- Docker Desktop (container management)

### Time Estimate by Day

```
Day 1: 8 hours (high setup work)
Day 2: 6 hours (straightforward auth)
Day 3: 8 hours (ML/NLP complexity)
Day 4: 7 hours (LLM optional)
Day 5: 8 hours (frontend build)
Day 6: 7 hours (features + integration)
Day 7: 6 hours (testing + docs)

TOTAL: ~50 hours (6-8 hours/day)
```

---

## Cost Breakdown

### Infrastructure Costs
| Resource | Cost |
|----------|------|
| PostgreSQL (local) | FREE |
| FastAPI (open-source) | FREE |
| React (open-source) | FREE |
| Ollama (open-source) | FREE |
| Docker (free tier) | FREE |
| GitHub (public repo) | FREE |
| **TOTAL** | **$0** |

### Time Value
- 50 hours of development
- Professional rate: ~$75-150/hour
- **Equivalent value: $3,750 - $7,500**

---

## Key Decisions Made

1. **Local-first approach** - Everything runs locally, no AWS Day 1
2. **Scikit-learn over Deep Learning** - Faster training, interpretable results
3. **Template + LLM hybrid** - Safe defaults with smart fallbacks
4. **PostgreSQL over NoSQL** - Better for relational data
5. **Zustand over Redux** - Simpler state management
6. **SQLAlchemy ORM** - Type-safe, flexible, migrations built-in
7. **Sentiment first, LLM second** - Core NLP before advanced features
8. **Manual testing** - Focus on functionality over unit tests

---

## Communication Plan

### Daily Status
```
Day 1: ✅ Backend skeleton ready
Day 2: ✅ Users can login
Day 3: ✅ Messages analyzed
Day 4: ✅ Bot responds intelligently
Day 5: ✅ UI complete
Day 6: ✅ All features working
Day 7: ✅ Demo ready
```

### Sharing Progress
- Push to GitHub daily
- Record 2-min demo clips
- Document blockers/solutions
- Keep README updated

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| PostgreSQL setup fails | Use Docker Compose (pre-configured) |
| Poetry install issues | Use pip + venv as fallback |
| Intent classifier low accuracy | Pre-train on larger dataset |
| LLM runs too slow | Keep templates as fast path |
| React build errors | Use CRA, known-good deps |
| Time overruns | Cut WebSocket (Day 5+) |
| Database schema mistakes | Use migrations, test locally first |

---

## Deliverables Checklist

### Code
- [ ] GitHub repository with 7 days of commits
- [ ] All source files organized
- [ ] .env.example files ready
- [ ] Dockerfile + docker-compose.yml working
- [ ] No hardcoded secrets

### Documentation
- [ ] README with quick start
- [ ] API documentation (Swagger)
- [ ] Setup guide (database, dependencies)
- [ ] Feature documentation
- [ ] Known limitations listed

### Testing
- [ ] Manual E2E scenarios tested
- [ ] All pages accessible
- [ ] Error handling working
- [ ] Database persistence verified
- [ ] Auth flow tested

### Demo
- [ ] Record 5-min demo video
- [ ] Create test user account
- [ ] Sample conversation prepared
- [ ] Mood tracking demo ready
- [ ] Assessment scored + displayed

---

## FAQ

**Q: Can I use different tech stack?**  
A: Yes, but Day 1-2 will take longer. The chosen stack has minimal setup.

**Q: What if I get stuck?**  
A: Refer to the boilerplate files provided. They're copy-paste ready.

**Q: Can I skip Ollama (LLM)?**  
A: Yes! Templates alone work fine. LLM is Day 4 bonus.

**Q: How production-ready is this?**  
A: Not at all. It's a prototype. Security, error handling, and tests are minimal.

**Q: Can I deploy to AWS after Day 7?**  
A: Yes! Use the full architecture guide. Day 7 code is 80% compatible.

**Q: What's the hardest part?**  
A: Day 3 (NLP) and Day 5 (React) typically. Plan extra time.

**Q: Can I work part-time?**  
A: Yes, stretch to 2 weeks at 3-4 hours/day.

---

## Final Checklist Before Starting

- [ ] Installed Python 3.10+
- [ ] Installed Node.js 18+
- [ ] Installed PostgreSQL
- [ ] Downloaded VS Code
- [ ] Initialized GitHub account
- [ ] Created empty repository
- [ ] Read this entire document
- [ ] Printed out daily schedule
- [ ] Set up time blocking (8am-5pm)
- [ ] Identified help resources

---

## You're Ready! 🚀

**Start with:** `mkdir mental-health-chatbot-mvp && cd mental-health-chatbot-mvp && git init`

**Questions?** Refer to:
- Day 1-7 detailed guides
- Boilerplate templates
- Quick start guide
- Full architecture document

Good luck! 💙
