from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

if __name__ == '__main__':
    app.run(debug=True)
