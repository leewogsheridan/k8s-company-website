from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <html>
        <head>
            <title>Company Website</title>
        </head>
        <body>
            <h1>Welcome to Our Updated Company Website</h1>

            <p>This application is running on Kubernetes.</p>
            
            <h2>Application Information</h2>
            <p>Company Name: Fake Apple</p>
            <p>Company Address: Zero Apple Park Way, Cupertino, CA, USA</p>
            <p>Contact Email: fakeapple@apple.com</p>
            <p>List of services: /, /info, /health</p>
            <p>Current Application Version: v2</p>
            <p>Application: Company Website</p>
            <p>Technology: Python Flask</p>
            <p>Container Hostname: {hostname}</p>

            <hr>
            <p>Deployed using Docker and Kubernetes.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "application": "company-website"})


@app.route("/info")
def info():
    return jsonify(
        {
            "application": "Company Website",
            "technology": "Python Flask",
            "hostname": socket.gethostname(),
            "environment": os.getenv("APP_ENV", "development"),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
