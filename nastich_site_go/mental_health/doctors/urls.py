from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommend_doctor/', views.recommend_doctor, name='recommend_doctor'),
    path('leave_review/', views.leave_review, name='leave_review'),
    path('create_questionnaire/', views.create_questionnaire, name='create_questionnaire'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/new/', views.create_doctor, name='create_doctor'),
    #path('recommend/', views.recommend_doctor, name='recommend_doctor'),
]