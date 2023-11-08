from flask import Flask
from kerykeion import AstrologicalSubject
from openai import OpenAI
openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    client = OpenAI()
    
    empty_thread = openai.beta.threads.create()
    print(empty_thread)

    
    return "Sun Sign: " + astroInfo
