import streamlit as st
import numpy as np
import re

from ingestion.resume_parser import parse_resume
from ingestion.embedding_service import create_embedding
from vector_store.faiss_index import TalentVectorDB


st.set_page_config(page_title="AI Talent Intelligence Platform", layout="wide")

st.title("🚀 AI Talent Intelligence Platform (Universal AI Version)")
st.write("Upload resumes and match candidates for ANY job role using AI-powered semantic matching.")


# Initialize vector DB once
if "vector_db" not in st.session_state:
    st.session_state.vector_db = TalentVectorDB()
    st.session_state.indexed_files = set()

vector_db = st.session_state.vector_db


# Extract keywords dynamically from job description
def extract_job_keywords(job_description):
    words = re.findall(r'\b[a-zA-Z]{3,}\b', job_description.lower())

    stop_words = {
        "with","and","for","the","are","you","will","from",
        "our","this","that","have","has","should","looking",
        "who","what","when","where","how","why","years",
        "experience","required","preferred"
    }

    keywords = [w for w in words if w not in stop_words]

    return list(set(keywords))


# Upload resumes
uploaded_files = st.file_uploader(
    "Upload Candidate Resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for file in uploaded_files:

        # Prevent duplicate indexing
        if file.name in st.session_state.indexed_files:
            continue

        resume_text = parse_resume(file)
        embedding = create_embedding(resume_text[:4000])  # limit size for stability

        candidate = {
            "name": file.name,
            "resume": resume_text,
            "embedding": embedding
        }

        vector_db.add_candidate(embedding, candidate)
        st.session_state.indexed_files.add(file.name)

    st.success("Resumes indexed successfully")


# Reset DB
if st.button("Reset Database"):
    st.session_state.vector_db = TalentVectorDB()
    st.session_state.indexed_files = set()
    st.success("Database cleared")


# Job description input
st.subheader("Paste Job Description")

job_description = st.text_area(
    "Example: Looking for Java Backend Developer with Spring Boot and MySQL"
)


# Find candidates
if st.button("Find Best Candidates"):

    if job_description.strip() == "":
        st.warning("Please enter a job description")

    else:

        job_embedding = create_embedding(job_description)
        job_keywords = extract_job_keywords(job_description)

        results = vector_db.search(job_embedding)

        # Remove duplicates safely
        unique_results = {}
        for r in results:
            unique_results[r["name"]] = r

        final_results = list(unique_results.values())

        st.subheader("Top Matching Candidates")

        for rank, candidate in enumerate(final_results):

            resume_text = candidate["resume"]

            # Cosine similarity
            similarity = np.dot(job_embedding, candidate["embedding"]) / (
                np.linalg.norm(job_embedding) * np.linalg.norm(candidate["embedding"])
            )

            # Keyword match score
            matched_skills = [
                keyword for keyword in job_keywords
                if keyword in resume_text.lower()
            ]

            keyword_score = len(matched_skills) / (len(job_keywords) + 1e-5)

            # Final weighted score
            final_score = (0.7 * similarity) + (0.3 * keyword_score)

            # Convert to 0–10 scale
            jd_score = round(final_score * 10)
            jd_score = max(0, min(10, jd_score))

            # Display
            st.markdown(f"### 🏆 Rank {rank+1}: {candidate['name']}")
            st.markdown(f"## ⭐ JD Match Score: {jd_score}/10")

            # Match strength label
            if jd_score >= 8:
                st.success("Strong Match")
            elif jd_score >= 6:
                st.info("Moderate Match")
            elif jd_score >= 4:
                st.warning("Weak Match")
            else:
                st.error("Poor Match")

            if matched_skills:
                st.write("Matched Keywords:", ", ".join(matched_skills))
            else:
                st.write("Matched Keywords: None")

            with st.expander("Preview Resume"):
                st.write(resume_text[:1000])