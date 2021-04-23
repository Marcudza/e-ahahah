from collections import Counter

from flask import Flask, render_template, request, redirect, make_response
import sqlite3

con = sqlite3.connect("slots.sqlite")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS ladder (
        name  STRING NOT NULL,
        password  STRING NOT NULL,
        balance INT    NOT NULL
    );
""")
result1 = cur.execute("""SELECT * FROM ladder""").fetchall()
for elem in result1:
    print(elem)
print('ahahaha', result1)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['POST', 'GET'])
def login():
    with sqlite3.connect("slots.sqlite") as con1:
        if request.method == 'POST':
            username = request.form['username']
            cur1 = con1.cursor()
            result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
            con1.commit()
            if not result or result[0][1] != int(request.form['password']):
                return render_template('login.html', title='Authorization', header=False, error=True)
            resp = make_response(redirect('/main', code=302))
            resp.set_cookie('userID', result[0][0])

            return resp
        username = request.cookies.get('userID')
        cur1 = con1.cursor()
        result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
        con1.commit()
        if not result:
            return render_template('login.html', title='Authorization', header=False, error=False)

        return redirect('/main', code=302)


@app.route('/registration', methods=['POST', 'GET'])
def reg():
    if request.method == 'GET':
        return render_template('register.html', title='Registration', header=False, error=False)
    elif request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            return render_template('register.html', title='Registration', header=False, error=True)
        with sqlite3.connect("slots.sqlite") as con1:
            cur1 = con1.cursor()
            cur1.execute("""INSERT INTO ladder(name, password, balance) 
                                VALUES (?, ?, ?)""", (request.form['username'], request.form['password'], 1000))
            con1.commit()
            resp = make_response(redirect('/main', code=302))
            resp.set_cookie('userID', request.form['username'])

            return resp


@app.route('/main')
def main_page():
    username = request.cookies.get('userID')
    with sqlite3.connect("slots.sqlite") as con1:
        cur1 = con1.cursor()
        result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
        con1.commit()
        if not result:
            return redirect('/', code=302)
        return render_template('main_page.html', title='StaletDrop', balance=result[0][2], name=result[0][0])


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    username = request.cookies.get('userID')
    with sqlite3.connect("slots.sqlite") as con1:
        cur1 = con1.cursor()
        result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
        if request.method == 'POST':
            if 'amount' in request.form.to_dict():
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (request.form['amount'], username))
                result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
            else:
                resp = make_response(redirect('/', code=302))
                resp.set_cookie('userID', '')
                con1.commit()
                return resp
        con1.commit()
        if not result:
            return redirect('/', code=302)

        return render_template('profile.html', title='My profile', balance=result[0][2], name=result[0][0],
                               password=result[0][1], disableProfileInfo=True, header=False)


@app.route('/koi', methods=['POST', 'GET'])
def koi_slot():
    with sqlite3.connect("slots.sqlite") as con1:
        username = request.cookies.get('userID')
        cur1 = con1.cursor()
        result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
        con1.commit()
        if not result:
            return redirect('/', code=302)

        if request.method == 'POST':
            numbers = request.form.to_dict()
            numbers = Counter([numbers['0'], numbers['1'], numbers['2']])
            Counter(numbers).items()
            maxx = 0
            for num in numbers:
                cur = numbers[num]
                if cur > maxx:
                    maxx = cur
            old_result = result[0][2]
            if maxx == 2:
                new_result = old_result + 200
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (new_result, username))
            elif maxx == 3:
                new_result = old_result + 1000
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (new_result, username))
            else:
                new_result = old_result - 100
                if new_result < 0:
                    new_result = 0
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (new_result, username))
            result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
        return render_template('koi_slot.html', title='KOI Princess', balance=result[0][2], name=result[0][0])


@app.route('/mayana', methods=['POST', 'GET'])
def mayana_slot():
    with sqlite3.connect("slots.sqlite") as con1:
        username = request.cookies.get('userID')
        cur1 = con1.cursor()
        result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
        con1.commit()
        if not result:
            return redirect('/', code=302)

        if request.method == 'POST':
            numbers = request.form.to_dict()
            numbers = Counter([numbers['0'], numbers['1'], numbers['2']])
            Counter(numbers).items()
            maxx = 0
            for num in numbers:
                cur = numbers[num]
                if cur > maxx:
                    maxx = cur
            old_result = result[0][2]
            if maxx == 2:
                new_result = old_result + 200
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (new_result, username))
            elif maxx == 3:
                new_result = old_result + 1000
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (new_result, username))
            else:
                new_result = old_result - 100
                if new_result < 0:
                    new_result = 0
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (new_result, username))
            result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
        return render_template('mayana_slot.html', title='Mayana', balance=result[0][2], name=result[0][0])


@app.route('/df', methods=['POST', 'GET'])
def df_slot():
    with sqlite3.connect("slots.sqlite") as con1:
        username = request.cookies.get('userID')
        cur1 = con1.cursor()
        result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()
        con1.commit()
        if not result:
            return redirect('/', code=302)

        if request.method == 'POST':
            numbers = request.form.to_dict()
            numbers = Counter([numbers['0'], numbers['1'], numbers['2']])
            Counter(numbers).items()
            maxx = 0
            for num in numbers:
                cur = numbers[num]
                if cur > maxx:
                    maxx = cur
            old_result = result[0][2]
            if maxx == 2:
                new_result = old_result + 200
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (new_result, username))
            elif maxx == 3:
                new_result = old_result + 1000
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (new_result, username))
            else:
                new_result = old_result - 100
                if new_result < 0:
                    new_result = 0
                cur1.execute("""UPDATE ladder SET balance = ? WHERE name = ?""", (new_result, username))
            result = cur1.execute("""SELECT * FROM ladder WHERE name = ?""", (username,)).fetchall()

        return render_template('df_slot.html', title='Divine Fortune', balance=result[0][2], name=result[0][0])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
