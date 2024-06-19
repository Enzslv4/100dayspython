from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    def my_length_check(form, field):
        if len(field.data) < 8:
            raise ValidationError('Name must be more than 8 characters')
    password = PasswordField('Password', validators=[DataRequired(), my_length_check])
    submit = SubmitField(label="Log In")
    

app = Flask(__name__)
app.secret_key = "asdasdasdasd"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
        
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
