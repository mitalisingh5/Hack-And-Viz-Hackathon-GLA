# Hack‑Viz — GLA Hackathon Project 🚀

An end‑to‑end, AI‑powered **Career & Job‑Market Intelligence platform** that helps students, freshers, and working professionals discover the right skills, visualize career paths, and match with real‑time opportunities.


---

## Table&nbsp;of&nbsp;Contents
1. [Why Hack‑Viz?](#why-hack-viz)
2. [Core Features](#core-features)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Getting Started](#getting-started)
6. [Usage Guide](#usage-guide)
7. [Data Sources](#data-sources)
8. [Contributing](#contributing)
9. [License](#license)

---

## Why Hack‑Viz?

> **Problem:** Students and early‑career professionals struggle to **identify skill gaps, craft job‑ready resumes, and track fast‑evolving roles** in AI & tech.  
> **Solution:** Hack‑Viz combines **machine learning, NLP, and data‑viz** to deliver actionable insights, dynamic career road‑maps, and live job recommendations — all from a single dashboard.

---

## Core Features

| # | Feature | What it does |
|---|---------|--------------|
| 1 | **AI Career Path Predictor** | Recommends next‑step roles & skills (e.g., *Junior → Senior → Tech Lead*) |
| 2 | **AI‑Powered Resume Customizer** | Auto‑tailors a CV to any job description (ATS‑ready keywords) |
| 3 | **Live Job Matchmaking** | Streams jobs in real time and ranks them by profile fit |
| 4 | **AI Mock‑Interview Mentor** | Runs interactive interview sessions & gives feedback |
| 5 | **Skill‑Gap Analyzer** | Maps current vs. required skills and suggests learning tracks |
| 6 | **Personality‑Based Recommendations** | Aligns careers with MBTI / Big‑Five personality traits |
| 7 | **Blockchain Credential Vault** | Verifies certificates & badges on‑chain for authenticity |
| 8 | **Remote‑Friendly Job Search** | Filters global roles by location, visa & pay benchmarks |
| 9 | **Skill‑Based Volunteering** | Finds non‑profit projects that match a student’s abilities |
|10 | **EQ Training Coach** | Personalized modules to boost soft‑skills & empathy |
|11 | **Curated Podcasts & Articles** | Suggests content to stay ahead of industry trends |
|12 | **Life‑Goal Compatibility Score** | Rates jobs on salary, work‑life balance & personal values |

---

## Tech Stack

- **Backend:** Django 5 · Django REST Framework · Python 3.12  
- **AI / ML:** Pandas · scikit‑learn · OpenAI API · HuggingFace Transformers  
- **Data‑Viz:** Plotly · Matplotlib  
- **Frontend:** HTML · Jinja2 templates · Bootstrap 5  
- **Database:** SQLite (dev) · PostgreSQL (prod)  
- **DevOps:** GitHub Actions · Docker · Ngrok (local tunneling)  
- **Others:** `pandas‑ai`, `python‑docx`, `reportlab`, `xlsxwriter`

---

## Project Structure

> **Note**: A lightweight `venv/` is excluded via `.gitignore`. Create your own local virtual environment before running.

---

## Getting Started

```bash
# 1) Clone & create venv
git clone https://github.com/varungupta132/Hack-Viz-Hackathon-GLA.git
cd Hack-Viz-Hackathon-GLA
python -m venv venv
source venv/Scripts/activate   # Windows PowerShell: .\venv\Scripts\Activate

# 2) Install Python deps
pip install -r requirements.txt

# 3) Apply DB migrations (Django)
python manage.py migrate

# 4) Run the dev server
python manage.py runserver
# OR, if using Streamlit:
# streamlit run app.py


