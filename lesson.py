from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Authorization', header=False, error=False)
    elif request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        pass_db = '123'
        # check password in db
        error = request.form['password'] != pass_db
        if error:
            return render_template('login.html', title='Authorization', header=False, error=True)
        return redirect('/main', code=302)


@app.route('/registration', methods=['POST', 'GET'])
def reg():
    if request.method == 'GET':
        return render_template('register.html', title='Registration', header=False, error=False)
    elif request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        if not request.form['username'] or not request.form['password']:
            return render_template('register.html', title='Registration', header=False, error=True)
        # add user to db
        return redirect('/main', code=302)


@app.route('/main')
def main_page():
    # get username and balance from db
    return render_template('main_page.html', title='StaletDrop', balance=100, name='Garfield')


@app.route('/profile')
def profile():
    # get username, balance, password from db
    return render_template('profile.html', title='My profile', balance=100, name='Garfield', password='123',
                           disableProfileInfo=True, header=False)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
