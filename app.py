from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def index():

    search = None
    data = None

    con = sqlite3.connect('test.db')
    db = con.cursor()

    if request.method == 'POST' and 'search' in request.form:
        search = request.form['search']
        res = db.execute('SELECT value, cur_name, country FROM coins where cur_name = ?', (search,))
        data = res.fetchall()
    return render_template('index.html', coins=data, search=search)


if __name__ == '__main__':
    app.run(Debug=True)
