from django.db import models

class JobDescription(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    job_file = models.FileField(upload_to='Jobs/', default='file.txt')

    def __str__(self):
        return self.title

class Resume(models.Model):
    user_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='CV/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
