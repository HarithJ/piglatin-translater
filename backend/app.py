from flask import Flask, request
from flask_cors import CORS

from translater.pig_latin import translateStringToPigLatin

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def hello_world():
        return {"Greetings": "Hello, World!"}

    @app.route('/translate', methods=['POST'])
    def translate():
        if request.method == 'POST':
            textToBeTranslated = request.get_json(force=True)
            textToBeTranslated = textToBeTranslated["engText"]

            translation = translateStringToPigLatin(textToBeTranslated)

            return {"translation": translation}

    return app