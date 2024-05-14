from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/8e3c0a68d6abf5641053").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

# your code here

if __name__ == '__main__':
    app.run(debug=True)