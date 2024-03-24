from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_numb = random.randint(0, 10)
    year = datetime.datetime.now().year
    return render_template('index.html', num=random_numb, y=year)

@app.route("/name/<name>")
def get_gender(name):
    gender = requests.get(url=f'https://api.genderize.io?name={name}').json()['gender']
    return render_template('guess.html', n=name, g=gender)

# your code here

if __name__ == '__main__':
    app.run(debug=True)