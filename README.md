# Pig Latin Translater

This repository holds three parts to the Pig Latin Translater:
- Backend API
- Frontend Client
- Python Client

# Backend API

Backend API holds two routes:
- `index route (/)`; It accepts a `GET` request and returns a JSON: {"Greetings": "Hello, World!"}
- `/translate route`; It accepts a `POST` request with a **JSON object**. The object should have a key of `engText` with a value containing English text which is supposed to be translated to Pig Latin, and it returns a JSON object which contains a `translation` key with a value of Pig Latin translation.

## Dependencies

The Backend API has the following dependencies:
1. Python 3.x
2. Flask
3. flask_cors

## Running the backend API locally

To run the backend API locally first `cd` into backend folder and execute the following commands:
1. Create a virtual environment: 
```
python3 -m venv venv
```
2. Activate the environment:
```
. venv/bin/activate
```
3. Install the dependencies:
```
pip install flask
pip install flask_cors
```
4. Run the application:
```
flask run
```
This will start the application on port `5000`.

### Running the backend via docker-compose

There is a `help.sh` script on the root folder that will help you start the application using docker-compose. In order to start the backend using docker-compose make sure you are on the root directory of this repository and execute the following:
```
./help.sh start-backend
```
This will start the application on port `8080`.

# Frontend Client

Frontend client is built using HTML, Bootstrap and JavaScript. It has a simple text area on the left-side, where a user is able to input English text s/he will love to translate it to Pig Latin, and it has a text area on the right-side of the screen where the user will see the translation of the text upon hitting the submit button.

## Environment Variable

The Frontend needs one environment variable: `TRANS_URL`. This is the Backend API's `/translate` route where the client will send the data to get it translated to Pig Latin.

## Running the frontend locally

You just need to open up the index.html file in order to run the frontend client. But before you do, please note that you will need to turn translateToPigLatin.js.tpl file into an actual .js file. In order to do this, make sure you have set `TRANS_URL` to appropriate value and execute:
```
./help.sh buildJsFile
```
By default, the `TRANS_URL` value will be set to `http://127.0.0.1:8080/translate` (it assumes the you have started the Backend API via docker-compose).

### Running the frontend via docker-compose

There is a `help.sh` script on the root folder that will help you start the application using docker-compose. In order to start the frontend using docker-compose make sure you are on the root directory of this repository and execute the following:
```
./help.sh start-frontend
```

# Easily run the frontend and backend
There is a command in `help.sh` file which will start the frontend and the backend simultaneously, you don't have to set anything, just run this command:
```
./help.sh start
```

After running this command you will be able to access the frontend on port `5000` and the backend on port `8080`

# Python Client

Under the `pythonClient` folder, there is a python file which interacts with the user via their terminal. It seeks user input and makes a `POST` request to the backend using `TRANS_URL` environment variable, if the environment variable is not found, then it defaults to `http://127.0.0.1:8080/translate` (it assumes that backend is running via docker-compose). After receiving the JSON object from the API, it prints out the Pig Latin translation.

## Dependencies

In order to run the python client, you need the the following dependencies:
1. Python 3.x
2. requests

## Environment Variables

The python client expects one environment variable: `TRANS_URL`, which is the URL to the backend's `/translate` route. If the environment variable is not provided, it defaults to `http://127.0.0.1:8080/translate` (it assumes that backend is running via docker-compose).

## Running the Python Client

In order to run the the Python Client, `cd` in to `pythonClient` folder and follow these steps:

1. Create a virtual environment: 
```
python3 -m venv venv
```
2. Activate the environment:
```
. venv/bin/activate
```
3. Install the dependencies:
```
pip install requests
```
4. Run the application:
```
python piglatin.py
```
