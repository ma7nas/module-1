from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/films/list')
def get_films():
    return render_template('film_list.html')

@app.route('/films/table')
def get_films_table():
    with open("films.csv", 'r') as films:
        film_table = films.read().splitlines()

    counter = 0
    film_dictionary = {}
    film_dlist = []
    while counter < len(film_table):
        film_string = film_table[counter]
        film = film_string.split(",")
        film_dictionary["id"] = counter
        film_dictionary["name"] = film[0]
        film_dictionary["rating"] = film[1]
        film_dlist.append(film_dictionary.copy())
        counter += 1

    return render_template('film_list.html', films=film_dlist)