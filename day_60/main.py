from flask import Flask, render_template, request, valid_login, log_the_user_in


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def receive_data():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)