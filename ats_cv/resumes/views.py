from django.shortcuts import render, redirect
from .forms import ResumeForm, JobDescriptionForm
from .models import Resume, JobDescription
from .utils import process_resume

# Home view to handle email, job description, and resume upload
def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        job_description = request.POST.get('job_description')
        resume_form = ResumeForm(request.POST, request.FILES)

        if resume_form.is_valid():
            resume = resume_form.save()

            # Save job description
            JobDescription.objects.create(title='Uploaded Job', description=job_description)

            # Process the resume against the job description
            similarity_score = process_resume(resume.file.path, job_description)

            # Optionally, handle the email (send confirmation, etc.)

            return render(request, 'resumes/match_results.html', {
                'matches': [{'resume': resume, 'job': 'Uploaded Job', 'score': similarity_score}]
            })

    else:
        resume_form = ResumeForm()

    return render(request, 'resumes/home.html', {'resume_form': resume_form})

# View for uploading resumes (if you want a separate upload page)
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after successful upload
    else:
        form = ResumeForm()
    return render(request, 'resumes/upload_resume.html', {'form': form})

# View for uploading job descriptions (if you want a separate page for it)
def upload_job_description(request):
    if request.method == 'POST':
        form = JobDescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload_job_description')  # Redirect after successful upload
    else:
        form = JobDescriptionForm()
    return render(request, 'resumes/upload_job_description.html', {'form': form})

# View for matching resumes with job descriptions
def match_resumes(request):
    resumes = Resume.objects.all()
    job_descriptions = JobDescription.objects.all()
    matches = []

    # Iterate over job descriptions and resumes to find matches
    for job in job_descriptions:
        for resume in resumes:
            similarity_score = process_resume(resume.file.path, job.description)
            matches.append({'resume': resume, 'job': job, 'score': similarity_score})

    return render(request, 'resumes/match_results.html', {'matches': matches})
