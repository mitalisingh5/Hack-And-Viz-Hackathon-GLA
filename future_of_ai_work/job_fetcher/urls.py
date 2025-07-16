# job_fetcher/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('job_list/', views.job_list, name='job_list'),  # Ensure this line is present
]
