from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"


class LoginForm(FlaskForm):
    email = EmailField(label='Email:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='submit')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods={'GET', 'POST'})
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template('login.html', form=form)


@app.route("/denied")
def denied():
    return render_template('denied.html')


@app.route("/success")
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
