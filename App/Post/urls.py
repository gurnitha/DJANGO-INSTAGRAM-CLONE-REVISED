# App/Post/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from App.Post import views

app_name = 'Post'

urlpatterns = [
    path('', views.index, name='home'),
]
