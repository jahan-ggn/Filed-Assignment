from django.urls import path
from . import views

urlpatterns = [
    path("", views.AudioApi.as_view()),
    path("<str:audio_type>/", views.AudioApi.as_view()),
    path("<str:audio_type>/<int:pk>", views.AudioApi.as_view()),
]
