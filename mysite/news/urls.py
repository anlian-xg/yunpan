from django.urls import path

from . import views

urlpatterns = [
    path('hw/create/', views.HomeworkCreate.as_view()),
]