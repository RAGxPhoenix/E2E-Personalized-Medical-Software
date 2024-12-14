from django.urls import path
from . import views
from django.urls import path
from home import views as home_views  # Importing views from the home app


urlpatterns = [
    path('', home_views.home, name='home'),
    path('symptom_check/', views.symptom_check, name='symptom_check'),
    path('body_check/', views.body_check, name='body_check'),
    path('save-symptoms/', views.save_symptoms, name='save_symptoms'),
 
    # Other URL patterns...
]