from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/share', methods=['GET', 'POST'])
def share():
    if request.method == 'POST':
        # with open('change.txt', 'w') as f:
        path = request.form['path']
        if not os.path.isfile(path):
            return "No Such File Exists"
        else:
            with open('change.txt', 'w') as f:
                f.write(path)
            return "<h1 class='bold grow'> File Sharing Has Been Started </h1>"
    return "nice"


app.run(debug=True)
