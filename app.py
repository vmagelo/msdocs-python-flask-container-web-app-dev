import os
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)

# Flask detects that python-dotenv is installed and loads .env file if it exists
# Django, invoke the load explicitly
load_dotenv() 

answer = "No environment variables used."
if 'TEST_VAR' in os.environ:
    print('Load environment variables from .env')
    print('TEST_VAR:', os.environ['TEST_VAR'])
    answer = "Using environment variable TEST_VAR with value = " + os.environ['TEST_VAR']
else:
    print('No environment variables found.')


@app.route("/")
def home():
    return "Hello, Flask from docker-container-test1!! " + answer
    