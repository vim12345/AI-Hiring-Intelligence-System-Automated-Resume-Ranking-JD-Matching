import os
import logging
import streamlit as st
from sentence_transformers import SentenceTransformer
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

# Completely silence transformers + sentence_transformers logs
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("torch").setLevel(logging.ERROR)

@st.cache_resource(show_spinner=False)
def load_model():
    return SentenceTransformer(
        "all-MiniLM-L6-v2",
        device="cpu"
    )

model = load_model()

def create_embedding(text):
    return model.encode(text)