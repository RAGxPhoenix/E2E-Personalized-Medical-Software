from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import PatientSignUpForm, DoctorSignUpForm

from .models import Feedback

def signup(request):
    return render(request, 'authentication/signup.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print("Email:", email)  # Debugging
        print("Password:", password)  # Debugging
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None and user.is_patient:
            print("User authenticated as patient")  # Debugging
            login(request, user)
            return redirect('home:home')
        else:
            print("Authentication failed or user is not a patient")  # Debugging
    return render(request, 'authentication/login_user.html')

def login_doctor(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print("Email:", email)  # Debugging
        print("Password:", password)  # Debugging
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None and user.is_doctor:
            print("User authenticated as doctor")  # Debugging
            login(request, user)
            return redirect('home:home')
        else:
            print("Authentication failed or user is not a doctor")  # Debugging
    return render(request, 'authentication/login_doctor.html')



def signup_user(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home')
    else:
        form = PatientSignUpForm()
    return render(request, 'authentication/signup_user.html', {'form': form})

def signup_doctor(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home')
    else:
        form = DoctorSignUpForm()
    return render(request, 'authentication/signup_doctor.html', {'form': form})

def profile(request):
    return render(request, 'authentication/profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect

def patient_info(request):
    return render(request, 'authentication/patient_info.html')

def save_patient_info(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        
        patient_info = [first_name, last_name, email, phone, age, weight, height]
        
        # Store the patient_info list in session
        request.session['patient_info'] = patient_info

        return redirect('symptom_check') 


def submit_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        Feedback.objects.create(user=request.user, feedback_text=feedback_text)
        return redirect('profile')
