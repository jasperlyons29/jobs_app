from django.shortcuts import render
from .models import JobPosting


def home(request):
    job_posts = JobPosting.objects.all()
    return render(request, 'jobs_app/index.html', {'job_posts': job_posts})