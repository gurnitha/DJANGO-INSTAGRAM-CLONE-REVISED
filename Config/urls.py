# Config/urls.py

# Django and third parties modules
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # App
    path('', include('App.Post.urls', namespace='Post')),

    # Admin
    path('admin/', admin.site.urls),
]
