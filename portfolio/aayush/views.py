from django.shortcuts import render
from .models import Yourself,Resume,Article

# Create your views here.
def home(request):
    context=Yourself.objects.all()
    resumes=Resume.objects.all()
    names = [contexts.name for contexts in context]
    facebook=[contexts.facebook for contexts in context]
    twitter=[contexts.twitter for contexts in context]
    linkedin=[contexts.linkedin for contexts in context]
    github=[contexts.github for contexts in context]
    resume=[resume.resume_file.url for resume in resumes]
    contexts={
        'names':names[0],
        'facebook':facebook[0],
        'twitter':twitter[0],
        'linkedin':linkedin[0],
        'resume':resume[0],
        'github':github[0]
    }
    return render(request,'index.html',contexts)

def about(request):
    context=Yourself.objects.all()
    resumes=Resume.objects.all()
    names = [contexts.name for contexts in context]
    phone=[contexts.phone for contexts in context]
    address=[contexts.address for contexts in context]
    email=[contexts.email for contexts in context]
    degree=[contexts.degree for contexts in context]
    about_you=[contexts.about_you for contexts in context]
    resume=[resume.resume_file.url for resume in resumes]
    contexts={
        'names':names[0],
        'phone':phone[0],
        'address':address[0],
        'email':email[0],
        'names':names[0],
        'degree':degree[0],
        'about_you':about_you[0],
        'resume':resume[0]
    }
    return render(request,'about.html',contexts)

def contact(request):
    context=Yourself.objects.all()
    resumes=Resume.objects.all()
    names = [contexts.name for contexts in context]
    phone=[contexts.phone for contexts in context]
    address=[contexts.address for contexts in context]
    email=[contexts.email for contexts in context]
    facebook=[contexts.facebook for contexts in context]
    twitter=[contexts.twitter for contexts in context]
    linkedin=[contexts.linkedin for contexts in context]
    github=[contexts.github for contexts in context]
    resume=[resume.resume_file.url for resume in resumes]
    contexts={
        'names':names[0],
        'phone':phone[0],
        'address':address[0],
        'email':email[0],
        'names':names[0],
        'facebook':facebook[0],
        'twitter':twitter[0],
        'linkedin':linkedin[0],
        'resume':resume[0],
        'github':github[0]
    }
    return render(request,'contact.html',contexts)

def blog(request):
    context=Yourself.objects.all()
    resumes=Resume.objects.all()
    articles=Article.objects.all().order_by('-created_at')
    names = [contexts.name for contexts in context]
    resume=[resume.resume_file.url for resume in resumes]
    contexts={
        'names':names[0],
        'resume':resume[0],
        'articles':articles
    }
    return render(request,'blog.html',contexts)