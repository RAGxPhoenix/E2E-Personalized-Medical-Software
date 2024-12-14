from django.urls import path
from . import views
from django.urls import path
from home import views as home_views  # Importing views from the home app


urlpatterns = [
    path('', home_views.home, name='home'),  # Define the URL pattern for the home page
    path('signup/', views.signup, name='signup'),
    path('signup/user/', views.signup_user, name='signup_user'),
    path('signup/doctor/', views.signup_doctor, name='signup_doctor'),
    path('login/user/', views.login_user, name='login_user'),
    path('login/doctor/', views.login_doctor, name='login_doctor'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('patient-info/', views.patient_info, name='patient_info'),
    path('save-patient-info/', views.save_patient_info, name='save_patient_info'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    # Other URL patterns...
]
