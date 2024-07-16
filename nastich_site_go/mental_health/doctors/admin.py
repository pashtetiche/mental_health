from django.contrib import admin
from .models import Doctor, Questionnaire, Review, Recommendation

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'experience_years', 'approved',
        'reception_type', 'specialty', 'city', 'is_diagnostics', 'is_icd_diagnosis', 'medical_conclusion',
        'recipe', 'price',
    )
    list_filter = ('approved',)
    actions = ['approve_doctors']

    def approve_doctors(self, request, queryset):
        queryset.update(approved=True)
    approve_doctors.short_description = "Approve selected doctors"

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'created_at', 'approved')
    list_filter = ('approved',)
    actions = ['approve_questionnaires']

    def approve_questionnaires(self, request, queryset):
        queryset.update(approved=True)
    approve_questionnaires.short_description = "Approve selected questionnaires"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'rating', 'created_at', 'approved')
    list_filter = ('approved',)
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
    approve_reviews.short_description = "Approve selected reviews"

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'created_at', 'approved')
    list_filter = ('approved',)
    actions = ['approve_recommendations']

    def approve_recommendations(self, request, queryset):
        queryset.update(approved=True)
    approve_recommendations.short_description = "Approve selected recommendations"
