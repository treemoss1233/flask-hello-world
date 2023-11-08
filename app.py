from flask import Flask
from kerykeion import AstrologicalSubject

app = Flask(__name__)

@app.route('/')
def hello_world():
    from openai import OpenAI
    client = OpenAI()
    
    empty_thread = openai.beta.threads.create()
    print(empty_thread)

    
    return "Sun Sign: " + astroInfo
