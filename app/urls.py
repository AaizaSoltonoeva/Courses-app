from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.CourseList.as_view()),
    path('course/<int:pk>/', views.CourseDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('branch/', views.BranchList.as_view()),
    path('branch/<int:pk>/', views.BranchDetail.as_view()),
    path('contacts/', views.ContactsList.as_view()),
    path('contacts/<int:pk>/', views.ContactsDetail.as_view()),
]