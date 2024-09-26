from django.contrib import admin
from django.urls import path, include
from resumes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home view
    path('resumes/upload/', views.upload_resume, name='upload_resume'),  # Resume upload view
]
