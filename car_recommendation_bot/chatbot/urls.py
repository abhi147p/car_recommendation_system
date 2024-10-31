# chatbot/urls.py
from django.urls import path
from . import views

# chatbot/urls.py
urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('webhook/', views.dialogflow_webhook, name='dialogflow_webhook'),
]

