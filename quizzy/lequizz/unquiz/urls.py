from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.join_quiz, name='join_quiz'),
    path('quiz', views.quiz_start, name='quiz_start'),
    path('logout', views.quiz_logout, name='quiz_logout'),
    path('ws/<str:room_name>/', views.room, name='room'),
]