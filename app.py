from flask import Flask, render_template, request
import os

app = Flask(__name__)

countries = ['Andorra', 'Austria', 'Belgium', 'Cyprus', 'Estonia', 'Finland',
             'France', 'Germany', 'Greece', 'Ireland', 'Italy', 'Latvia',
             'Lithuania', 'Luxembourg', 'Malta', 'Monaco', 'Netherlands',
             'Portugal', 'San Marino', 'Slovakia', 'Slovenia', 'Spain', 'Vatican City']

# coins = ['2Euro', '1Euro', '50cent', '20cent', '10cent', '5cent', '2cent', '1cent']


@app.route('/', methods=['GET', 'POST'])
def index():

    country_name = ''
    images_list = ['1', '2']

    if request.method == 'POST' and 'submit' in request.form:
        country_name = request.form['country']

        path = "static/Countries/"+country_name+"/"
        images_list = os.listdir(path)

    return render_template('index.html',
                           list_countries=countries,
                           country=country_name,
                           folder=images_list)


if __name__ == '__main__':
    app.run(Debug=True)

