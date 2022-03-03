from flask import Flask, jsonify, render_template
from datetime import date
# import time
app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"Date of Call": date.today()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


@app.route('/home')
def home():
   return render_template('home.html')
if __name__ == '__main__':
   app.run()