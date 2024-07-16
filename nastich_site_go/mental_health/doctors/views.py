from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Questionnaire, Review, Recommendation
from .forms import QuestionnaireForm, ReviewForm, RecommendationForm, DoctorFilterForm, DoctorForm
from django.db.models import Q

# def home(request):
#     return render(request, 'home.html')

def home(request):
    doctors = Doctor.objects.filter(approved=True)
    form = DoctorFilterForm(request.GET)

    if form.is_valid():
        if form.cleaned_data.get('specialty'):
            doctors = doctors.filter(specialty__icontains=form.cleaned_data['specialty'])
        if form.cleaned_data.get('city'):
            doctors = doctors.filter(city__icontains=form.cleaned_data['city'])
        if form.cleaned_data.get('experience_years') is not None:
            doctors = doctors.filter(experience_years__gte=form.cleaned_data['experience_years'])

    return render(request, 'home.html', {'form': form, 'doctors': doctors})

def recommend_doctor(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Adjust this redirect as needed
    else:
        form = RecommendationForm()
    return render(request, 'recommend_doctor.html', {'form': form})

def leave_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'leave_review.html', {'form': form})

def create_questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionnaireForm()
    return render(request, 'create_questionnaire.html', {'form': form})

def doctor_list(request):
    form = DoctorFilterForm(request.GET or None)
    doctors = Doctor.objects.all()

    if form.is_valid():
        if form.cleaned_data.get('name'):
            doctors = doctors.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data.get('specialty'):
            doctors = doctors.filter(specialty=form.cleaned_data['specialty'])
        if form.cleaned_data.get('city'):
            doctors = doctors.filter(city__icontains=form.cleaned_data['city'])
        if form.cleaned_data.get('reception_type'):
            doctors = doctors.filter(reception_type=form.cleaned_data['reception_type'])
        if form.cleaned_data.get('is_diagnostics') is not None:
            doctors = doctors.filter(is_diagnostics=form.cleaned_data['is_diagnostics'])
        if form.cleaned_data.get('is_icd_diagnosis') is not None:
            doctors = doctors.filter(is_icd_diagnosis=form.cleaned_data['is_icd_diagnosis'])
        if form.cleaned_data.get('medical_conclusion') is not None:
            doctors = doctors.filter(medical_conclusion=form.cleaned_data['medical_conclusion'])
        if form.cleaned_data.get('recipe'):
            doctors = doctors.filter(recipe=form.cleaned_data['recipe'])
        if form.cleaned_data.get('price_min') is not None:
            doctors = doctors.filter(price__gte=form.cleaned_data['price_min'])
        if form.cleaned_data.get('price_max') is not None:
            doctors = doctors.filter(price__lte=form.cleaned_data['price_max'])

    return render(request, 'doctor_list.html', {'doctors': doctors, 'form': form})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.approved = False  # Ensure the new doctor is not approved
            doctor.save()
            return redirect('doctor_list')  # Redirect to the doctor list after saving
    else:
        form = DoctorForm()
    return render(request, 'create_doctor.html', {'form': form})

