from django.contrib import admin
from django.urls import path, include  # include import karna hoga
from homepage import views  # Home page views import karenge
from job_recommendation import views as job_views  # Job recommendation views import karenge

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page link
    path('job_recommendation/', job_views.job_recommendation, name='job_recommendation'), 
     
     
      # New job recommendation link
    path('job-fetcher/', include('job_fetcher.urls')),  # Include job-fetcher URLs
# path('', include('interview_mentor.urls')),    
]
