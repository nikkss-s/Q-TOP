from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()  # Sometimes `os.getlogin()` fails; I'll suggest an alternative if needed.
    ist_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {name}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {ist_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
