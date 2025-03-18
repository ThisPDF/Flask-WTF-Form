from ensurepip import bootstrap

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length
import dotenv
import os

dotenv.load_dotenv()

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[Length(min=8)])
    submit = SubmitField('Login')


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('CSFR_SECRET_KEY')
bootstrap = Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == os.getenv('admin_email') and form.password.data == os.getenv('admin_pass'):
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
