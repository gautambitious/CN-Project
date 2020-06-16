from flask import Flask, render_template, request
import subprocess
from server import Server

app = Flask(__name__)

subprocess.call('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE)


@app.route('/')
def home():
    return "Hello World!"


app.run(port=5009)
