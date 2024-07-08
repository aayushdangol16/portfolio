from django.db import models

# Create your models here.
class Yourself(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    degree=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    about_you=models.TextField()
    address=models.CharField(max_length=50)
    facebook=models.CharField(max_length=300,default='default_facebook_value')
    twitter=models.CharField(max_length=300,default='default_facebook_value')
    linkedin=models.CharField(max_length=300,default='default_facebook_value')
    github=models.CharField(max_length=300,default='default_facebook_value')

    def __str__(self):
        return self.name
    
class Resume(models.Model):
    resume_file=models.FileField(upload_to='uploads/')

    def __str__(self):
        return 'resume'
    
class Article(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def show(self):
        return (self.content[:300]+' ...')
