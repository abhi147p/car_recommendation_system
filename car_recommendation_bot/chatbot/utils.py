# chatbot/utils.py
import openai
import requests

openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_recommendations(user_input):
    # GPT-3 API call to generate recommendation
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Suggest a car based on the following preferences: {user_input}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def fetch_car_data(preferences):
    # Replace with your car API endpoint and parameters
    url = "https://api.example.com/get_cars"
    params = preferences
    response = requests.get(url, params=params)
    return response.json()

