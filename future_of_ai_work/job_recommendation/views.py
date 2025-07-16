from django.shortcuts import render
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# from django.shortcuts import render

job_data = {
    'Job': [
        'Software Developer', 'Data Scientist', 'Machine Learning Engineer', 'AI Specialist', 'Web Developer',
        'Frontend Developer', 'Backend Developer', 'DevOps Engineer', 'Database Administrator', 'Cybersecurity Analyst',
        'Cloud Architect', 'Mobile App Developer', 'Game Developer', 'System Analyst', 'Technical Support Engineer'
    ],
    'Skills': [
        'Python, Java, C++, Algorithms, Git, Data Structures',
        'Python, R, SQL, Statistics, Data Analysis, Pandas, NumPy',
        'Python, TensorFlow, PyTorch, Machine Learning, Scikit-learn, NumPy',
        'Artificial Intelligence, Machine Learning, Deep Learning, NLP, Computer Vision',
        'HTML, CSS, JavaScript, React, Node.js, Git, Responsive Design',
        'HTML, CSS, JavaScript, React, Redux, Bootstrap, UI/UX Design',
        'Java, Spring Boot, Node.js, Express.js, REST APIs, MongoDB',
        'AWS, Docker, Kubernetes, CI/CD, Linux, Jenkins',
        'SQL, MySQL, PostgreSQL, Database Design, Backup, Optimization',
        'Network Security, Ethical Hacking, Penetration Testing, Firewalls, Python, Encryption',
        'AWS, Azure, GCP, Cloud Infrastructure, DevOps, Microservices',
        'Java, Kotlin, Android Studio, Swift, iOS Development, React Native',
        'C++, Unity, Unreal Engine, Game Design, Graphics Programming',
        'Systems Analysis, Business Analysis, Documentation, UML, SQL',
        'Troubleshooting, Hardware Support, Networking, Windows, Linux, Communication'
    ]
}

df = pd.DataFrame(job_data)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['Skills'])

def recommend_jobs(user_skills, top_n=5):
    user_vector = vectorizer.transform([user_skills])
    cosine_sim = cosine_similarity(user_vector, tfidf_matrix).flatten()
    
    top_indices = cosine_sim.argsort()[::-1][:top_n]
    
    recommendations = []
    for i in top_indices:
        job_title = df['Job'][i]
        score = round(cosine_sim[i] * 100, 2)
        recommendations.append((job_title, score))
    
    return recommendations

def job_recommendation(request):
    if request.method == 'POST':
        user_input = request.POST.get('skills_input') 
        recommended_jobs = recommend_jobs(user_input)
        return render(request, 'job_recommendation/job_recommendation.html', {'recommended_jobs': recommended_jobs})
    return render(request, 'job_recommendation/job_recommendation.html')
