# In your app's urls.py file
from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('', views.home, name='home'),  # Your home page URL pattern
    path('features/', views.features, name='features'),  # Features page URL pattern
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('searching/', views.searching, name='searching'),
    path('get-info/', views.get_info, name='get_info')
    # Add more URL patterns as needed
]

