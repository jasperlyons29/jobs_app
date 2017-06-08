from django.shortcuts import render
from .models import JobPosting


def home(request):
    job_posts = JobPosting.objects.all()
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        jp_obj = JobPosting.objects.create(
            title=title,
            description=description
        )
        jp_obj.save()
    return render(request, 'jobs_app/index.html', {'job_posts': job_posts})