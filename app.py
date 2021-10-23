from flask import Flask
from flask import redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", code=302)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')