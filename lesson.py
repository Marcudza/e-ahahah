from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Authorization', form=form, header=False)


@app.route('/registration')
def reg():
    return render_template('reg.html', title='Registration')


@app.route('/main')
def main_page():
    return render_template('main_page.html', title='StaletDrop', balance=100, name='Garfield')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
