import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import random

# ---- Sidebar Menu ----
st.sidebar.title("🚀 Hack-Viz Dashboard")
menu = st.sidebar.radio("Select a Feature", [
    "🏠 Home",
    "📈 Career Path Predictor",
    "📄 Resume Analyzer",
    "🔎 Job Match Finder",
    "🤖 Interview Q&A",
    "🌐 Custom Dashboard View"
])

# ---- Home Page ----
if menu == "🏠 Home":
    st.title("Hack-Viz – GLA Hackathon App 🚀")
    st.markdown("""
    Welcome to the all-in-one AI-powered Career Dashboard!
    
    🔍 Explore career paths  
    🧠 Customize your resume  
    💼 Match with live jobs  
    🎤 Practice interviews  
    """)

# ---- 📈 Career Path Predictor ----
elif menu == "📈 Career Path Predictor":
    st.title("📈 AI Career Path Predictor")
    uploaded_file = st.file_uploader("Upload student data (CSV/XLSX)", type=["csv", "xlsx"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
        st.subheader("Student Data Preview")
        st.dataframe(df.head())

        # Simple skill-to-role mapping logic
        def predict_role(skills):
            skills = str(skills).lower()
            if 'python' in skills and 'ml' in skills:
                return 'Data Scientist'
            elif 'java' in skills and 'spring' in skills:
                return 'Backend Developer'
            elif 'figma' in skills or 'ui' in skills:
                return 'UI/UX Designer'
            elif 'excel' in skills or 'tableau' in skills:
                return 'Data Analyst'
            else:
                return 'General Tech Associate'

        st.subheader("Predicted Next Roles:")
        if 'Skills' in df.columns and 'Name' in df.columns:
            df['Predicted Role'] = df['Skills'].apply(predict_role)
            st.dataframe(df[['Name', 'Skills', 'Predicted Role']])
        else:
            st.error("Please make sure the file includes 'Name' and 'Skills' columns.")

# ---- 📄 Resume Analyzer ----
elif menu == "📄 Resume Analyzer":
    st.title("📄 Resume Analyzer")
    uploaded_resume = st.file_uploader("Upload your resume (TXT/CSV)", type=["txt", "csv"])
    if uploaded_resume:
        content = uploaded_resume.read().decode("utf-8")
        st.text_area("Resume Content", content, height=300)
        st.info("🔍 Feature coming soon: Keyword analysis, scoring, and feedback.")

# ---- 🔎 Job Match Finder ----
elif menu == "🔎 Job Match Finder":
    st.title("🔎 Job Match Finder")
    uploaded_jobs = st.file_uploader("Upload job market data (CSV)", type=["csv"])
    if uploaded_jobs:
        df_jobs = pd.read_csv(uploaded_jobs)
        st.subheader("Job Listings Preview")
        st.dataframe(df_jobs.head())
        st.success("✨ Try adding filters like skill match or salary range for smarter job search.")

# ---- 🤖 Interview Q&A ----
elif menu == "🤖 Interview Q&A":
    st.title("🤖 AI Interview Mentor")
    try:
        questions_df = pd.read_csv("Questions.csv")
        question = questions_df.sample(1).iloc[0, 0]
        st.write("🎯 Interview Question:")
        st.warning(question)
        st.text_input("Your Answer")
        st.info("🧠 Feedback logic to be implemented — you can integrate OpenAI API here.")
    except Exception as e:
        st.error(f"Could not load questions: {e}")

# ---- 🌐 Custom Dashboard View ----
elif menu == "🌐 Custom Dashboard View":
    st.title("🌐 HTML Dashboard View")
    try:
        with open("dashboard/index.html", 'r', encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=800, scrolling=True)
    except FileNotFoundError:
        st.error("Dashboard HTML not found! Please place your HTML file at: `dashboard/index.html`")

