from django.contrib import admin
from django.urls import path, include
from resumes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Set the home view as the root URL
]
