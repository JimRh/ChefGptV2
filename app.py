from flask import Flask,jsonify,request
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import requests
import os

app=Flask(__name__)

CORS(app)
load_dotenv()

@app.post('/getrecipe')



def getrecipe():
    URL = "https://api.openai.com/v1/chat/completions"
    key= os.environ.get('apikey')

    data=request.json
    ingredients=data['ingredients']
    prompt = "In this chat you will act as a AI for providing food recipe only. Nothing more.Now please provide me a recipe with the list items."+" "+ingredients



    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],

    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    response=requests.post(URL, headers=headers, json=payload, stream=False)

    return response.content
