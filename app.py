from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    person = AstrologicalSubject("Person", 1977, 6, 8, 8, 45, "Atlanta")

    #Get the information about the person
    astroInfo = person.sun
    
    return "Sun Sign: " + astroInfo
