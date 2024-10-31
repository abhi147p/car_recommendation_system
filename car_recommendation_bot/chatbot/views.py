# chatbot/views.py
from django.http import JsonResponse
import openai
import json
from .utils import get_recommendations

def dialogflow_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_query = data.get('queryResult', {}).get('queryText', '')

        # Use the recommendation function to process the query
        recommendation = get_recommendations(user_query)
        return JsonResponse({'fulfillmentText': recommendation})
    
# chatbot/views.py
from django.shortcuts import render

def chat(request):
    return render(request, 'chatbot/chat.html')

