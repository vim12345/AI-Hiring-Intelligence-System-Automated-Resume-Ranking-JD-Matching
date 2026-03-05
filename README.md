# 🚀 AI Talent Intelligence Platform

AI-powered resume screening and job matching system using semantic embeddings and vector search.

This platform automatically ranks candidate resumes against a Job Description (JD) using AI-driven semantic similarity and keyword matching.

---

## Live Demo

https://ai-hiring-intelligence-system-automated-resume-ranking-jd-matc.streamlit.app/

## 🔍 Overview

Traditional resume screening relies on keyword filtering.  
This system uses:

- Semantic embeddings
- Vector similarity search
- Hybrid scoring (semantic + keyword overlap)

to provide intelligent candidate ranking.

---

## 🧠 How It Works

1. Upload multiple candidate resumes (PDF)
2. Paste a Job Description
3. System generates embeddings using SentenceTransformers
4. FAISS performs vector similarity search
5. Hybrid scoring calculates JD Match Score (0–10)
6. Candidates are ranked by match strength

---

## ⭐ Features

- Universal job matching (any domain)
- Semantic resume–JD similarity
- Hybrid AI scoring system
- JD Match Score (0–10 scale)
- Match strength classification
- Resume preview
- Duplicate prevention
- Reset database option
- Fully local (no OpenAI API required)

---

## 🏗 Tech Stack

- Python
- Streamlit
- SentenceTransformers
- FAISS (vector database)
- NumPy
- PyPDF

---

## 📊 Scoring System

Final score is computed using:


Final Score =
0.7 × Semantic Similarity

0.3 × Keyword Overlap

JD Match Score = Final Score × 10


### Score Interpretation

| Score | Meaning |
|-------|----------|
| 9–10  | Excellent Match |
| 7–8   | Strong Match |
| 5–6   | Moderate Match |
| 3–4   | Weak Match |
| 0–2   | Poor Match |

---

## 🖥 Installation (Local)

### 1️⃣ Clone Repository


git clone https://github.com/YOUR_USERNAME/ai-talent-intelligence-platform.git

cd ai-talent-intelligence-platform


### 2️⃣ Create Virtual Environment


python -m venv venv
venv\Scripts\activate


### 3️⃣ Install Dependencies


pip install -r requirements.txt


### 4️⃣ Run Application


streamlit run app.py


Open:


http://localhost:8501


---

## 🌍 Deployment

Recommended: **Streamlit Cloud**

1. Push project to GitHub
2. Go to https://share.streamlit.io
3. Connect repository
4. Deploy
5. Share live link

---

## 📂 Project Structure


ai-talent-intelligence-platform/
│
├── app.py
├── requirements.txt
│
├── ingestion/
│ ├── resume_parser.py
│ └── embedding_service.py
│
├── vector_store/
│ └── faiss_index.py
│
└── matching/
└── candidate_matcher.py


---

## 🚀 Example Use Cases

- Resume screening automation
- Campus placement filtering
- Recruiter shortlisting tool
- Talent intelligence analytics
- HR tech experimentation
- AI-powered hiring platforms

---

## 🎯 Why This Project Matters

This project demonstrates:

- Applied NLP
- Semantic embeddings
- Vector databases (FAISS)
- Hybrid ranking systems
- AI product design thinking
- End-to-end ML application deployment

---

## 📌 Future Improvements

- Resume summarization
- Experience detection
- Skill extraction using LLM
- Candidate leaderboard
- Analytics dashboard
- Multi-user support
- Database persistence
- SaaS production deployment

---

## 👨‍💻 Author

**Vimal Kumar**  
AI / ML Engineer  
Built as a real-world AI hiring intelligence system.

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub!
