import streamlit as st
import pandas as pd

# Sidebar menu
st.sidebar.title("Hack-Viz Dashboard 🚀")
menu = st.sidebar.radio(
    "Choose a Module:",
    ["Home", "📈 Career Path Predictor", "📄 Resume Analyzer", "🔎 Job Match Finder", "🤖 Interview Q&A"]
)

# Home page
if menu == "Home":
    st.title("Hack-Viz – GLA Hackathon App 🚀")
    st.markdown("Welcome to the all-in-one career intelligence platform!")

# Career Path Predictor
elif menu == "📈 Career Path Predictor":
    st.title("📈 AI Career Path Predictor")
    st.write("Upload student profile data to predict future roles.")
    
    file = st.file_uploader("Upload student data (CSV/XLSX)", type=['csv', 'xlsx'])
    if file:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        st.dataframe(df.head())
        st.success("Data loaded successfully!")
        # Add mock predictions or model integration here

# Resume Analyzer
elif menu == "📄 Resume Analyzer":
    st.title("📄 Resume Analyzer")
    uploaded_file = st.file_uploader("Upload your resume (docx/pdf not yet supported)", type=['csv', 'txt'])
    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        st.text_area("Resume Content", content, height=300)
        st.info("Feature: Add NLP scoring or keyword matcher here")

# Job Match Finder
elif menu == "🔎 Job Match Finder":
    st.title("🔎 Job Match Finder")
    st.write("Explore job-market data and find matching roles.")
    file = st.file_uploader("Upload job market data (CSV)", type=['csv'])
    if file:
        df = pd.read_csv(file)
        st.dataframe(df.head())
        st.success("Job market data loaded!")
        # Add filters or profile-matching logic here

# Interview Q&A
elif menu == "🤖 Interview Q&A":
    st.title("🤖 AI Interview Mentor")
    st.write("Practice interviews with AI-generated questions.")
    
    question_df = pd.read_csv("Questions.csv")
    if not question_df.empty:
        st.write("Random Interview Question:")
        st.info(question_df.sample(1).iloc[0][0])
