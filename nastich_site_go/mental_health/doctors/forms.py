from django import forms
from .models import Questionnaire, Review, Recommendation, Doctor

class DoctorFilterForm(forms.Form):
    name = forms.CharField(required=False)
    specialty = forms.ChoiceField(choices=Doctor.SPECIALIST_TYPE_CHOICES, required=False)
    city = forms.CharField(required=False)
    reception_type = forms.ChoiceField(choices=Doctor.RECEPTION_TYPE_CHOICES, required=False)
    is_diagnostics = forms.BooleanField(required=False)
    is_icd_diagnosis = forms.BooleanField(required=False)
    medical_conclusion = forms.BooleanField(required=False)
    recipe = forms.ChoiceField(choices=Doctor.RECIPE_CHOICES, required=False)
    price_min = forms.FloatField(required=False)
    price_max = forms.FloatField(required=False)

# class DoctorFilterForm(forms.Form):
#     specialty = forms.CharField(required=False, max_length=100)
#     city = forms.CharField(required=False, max_length=100)
#     experience_years = forms.IntegerField(required=False, min_value=0)

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['doctor', 'content']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['doctor', 'content', 'rating']

class RecommendationForm(forms.ModelForm):
    doctor_name = forms.CharField(max_length=100)
    doctor_specialty = forms.ChoiceField(choices=Doctor.SPECIALIST_TYPE_CHOICES)
    doctor_city = forms.CharField(max_length=255)
    doctor_experience_years = forms.IntegerField()
    doctor_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Recommendation
        fields = ['content']

    def save(self, commit=True):
        recommendation = super().save(commit=False)
        doctor, created = Doctor.objects.get_or_create(
            name=self.cleaned_data['doctor_name'],
            defaults={
                'specialty': self.cleaned_data['doctor_specialty'],
                'city': self.cleaned_data['doctor_city'],
                'experience_years': self.cleaned_data['doctor_experience_years'],
                'description': self.cleaned_data['doctor_description'],
                'approved': False,
            }
        )
        recommendation.doctor = doctor
        if commit:
            recommendation.save()
        return recommendation

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'name', 'experience_years', 'description', 'specialty',
            'city', 'reception_type', 'is_diagnostics', 'is_icd_diagnosis',
            'medical_conclusion', 'recipe', 'price'
        ]