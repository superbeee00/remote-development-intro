# Follow each of the TODO COMMENTs in this file.

# TODO: Fill in the following variables with your information.
YOUR_NAME = TODO   # Your name as string (in quotes)
FAVORITE_NUMBER = TODO  # Your favorite number

# The rest of the code below is already written for you.

from flask import Flask, render_template_string
import socket

app = Flask(__name__)

# Simple HTML template (students don't need to modify this)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Codespaces Demo</title>
    <style>
        body { font-family: sans-serif; }
        .container { max-width: 800px; margin: 50px auto; padding: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello {{ name }}!</h1>
        <p>This webpage is being served from:</p>
        <p><strong>{{ hostname }}</strong> on port <strong>{{ port }}</strong></p>
        <p>Your favorite number is: <strong>{{ number }}</strong></p>
    </div>
</body>
</html>
"""

SERVER_PORT = 8000

@app.route('/')
def home():
    hostname = socket.gethostname()
    return render_template_string(HTML_TEMPLATE,
                               name=YOUR_NAME,
                               number=FAVORITE_NUMBER,
                               port=SERVER_PORT,
                               hostname=hostname)

if __name__ == '__main__':
    print(f"\n🚀 Starting server on port {SERVER_PORT}...")
    print(f"👉 Open the 'Ports' tab in Codespaces and forward port {SERVER_PORT}")
    print(f"👉 Then visit the Preview URL that appears\n")
    app.run(host='0.0.0.0', port=SERVER_PORT)
