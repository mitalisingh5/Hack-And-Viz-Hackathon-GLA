import streamlit as st
from career_predictor import run_career_predictor
from resume_analyzer import run_resume_analyzer
from job_match_finder import run_job_match
from interview_qa import run_interview_qa

# Sidebar navigation
st.sidebar.title("🚀 Hack-Viz Dashboard")
choice = st.sidebar.radio("Select a Feature", [
    "🏠 Home",
    "📈 Career Path Predictor",
    "📄 Resume Analyzer",
    "🔎 Job Match Finder",
    "🤖 Interview Q&A"
])

# Feature routing
if choice == "🏠 Home":
    st.title("Hack-Viz – GLA Hackathon App 🚀")
    st.markdown("""
    Welcome to Hack-Viz — your AI Career Companion!
    
    Use the sidebar to explore:
    - 📈 Career Path Prediction  
    - 📄 Resume Analyzer  
    - 🔎 Job Matching  
    - 🤖 Interview Prep
    """)

elif choice == "📈 Career Path Predictor":
    run_career_predictor()

elif choice == "📄 Resume Analyzer":
    run_resume_analyzer()

elif choice == "🔎 Job Match Finder":
    run_job_match()

elif choice == "🤖 Interview Q&A":
    run_interview_qa()
