
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from flask import Flask

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Hello World route
@app.route("/")
def hello():
    return "Hello World! Flask app is running successfully."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
