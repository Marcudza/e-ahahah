from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html', title='Домашняя страница')


@app.route('/training/<prof>')
def training(prof):
    print(prof)
    return render_template('training.html', title='Тренировки в полёте', prof=prof)


@app.route('/list_prof/<tag>')
def list_prof(tag):
    if tag not in ['ol', 'ul']:
        return 'Передан неправильный параметр'
    prof = [
        'инженер - исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
        'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
        'метеоролог', 'оператор', 'марсохода', 'киберинженер', 'штурман', 'пилот дронов'
    ]
    return render_template('list_prof.html', tag=tag, prof=prof)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    d = dict()
    d['title'] = 'Анкета'
    d['surname'] = 'Watny'
    d['name'] = 'Mark'
    d['education'] = 'выше среднего'
    d['profession'] = 'штурман марсохода'
    d['sex'] = 'male'
    d['motivation'] = 'Всегда мечтал застрять на Марсе!'
    d['ready'] = True
    return render_template('answer.html', form=d, title=d['title'])


class LoginForm(FlaskForm):
    username = StringField('Id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap = StringField('Id капитана', validators=[DataRequired()])
    cap_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
