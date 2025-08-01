from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Get the greeting from an environment variable, with a default value
    greeting = os.environ.get("GREETING", "Hello")
    return f"{greeting}, my pipeline ran corrctlty!"

if __name__ == "__main__":
    # The host '0.0.0.0' makes the server publicly available
    # This is essential for it to work inside a Docker container
    app.run(host='0.0.0.0', port=5000)