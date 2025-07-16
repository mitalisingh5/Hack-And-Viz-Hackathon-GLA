# job_fetcher/views.py
import requests
from django.shortcuts import render

def job_list(request):
    
    response = requests.get("https://remoteok.com/api")
    jobs = response.json()[1:]  
    job_details = []
    for job in jobs:
        job_details.append({
            'company': job.get('company', 'N/A'),
            'position': job.get('position', 'N/A'),
            'location': job.get('location', '🌍 Remote / Not specified'),
            'salary': job.get('salary', '💸 Not listed'),
            'url': job.get('url', 'No URL')
        })

    return render(request, 'job_fetcher/job_list.html', {'job_details': job_details})

def home(request):
    return render(request, 'your_template.html')
