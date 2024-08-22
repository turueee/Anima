from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

from data import mexadatas
from data import anistudio
from data import aniinfo
from data import infcharacters
from data import photocharacters
from data import groopphoto
from data import add_information_to_about_anime_database
from data import add_information_to_character_database
from data import add_information_to_id_genre_database
from data import add_information_to_studio_database

app = Flask(__name__)


@app.route('/anima')
@app.route("/")
def Anima():
    return render_template('anima.html')


@app.route('/mexa')
def mexa():
    return render_template('mexa.html',
                           names=mexadatas()
                           )


@app.route('/mex/<name>')
def mex(name):
    return render_template('base.html',
                           menu=anistudio(name),
                           title=groopphoto(name),
                           infcharacter=infcharacters(name),
                           photocharacter=photocharacters(name),
                           groop=name,
                           **aniinfo(name))


@app.route('/create_about_anime/', methods=['post', 'get'])
def create_about_anime():
    message = ""
    if request.method == 'POST':
        rusname = request.form.get('rusname')
        engname = request.form.get('engname')
        director = request.form.get('director')
        ruslic = request.form.get('ruslic')
        id_genre = int(request.form.get('id_genre'))
        add_information_to_about_anime_database(rusname, engname, director, ruslic, id_genre)
    return render_template('create_about_anime.html', message=message)


@app.route('/create_studio/', methods=['post', 'get'])
def create_studio():
    message = ""
    if request.method == 'POST':
        studio = request.form.get('studio')
        id_genre = request.form.get('engname')
        add_information_to_studio_database(studio, id_genre)
    return render_template('create_studio.html', message=message)


@app.route('/create_id_genre/', methods=['post', 'get'])
def create_id_genre():
    message = ""
    if request.method == 'POST':
        id_genre = request.form.get('id_genre')
        genre = request.form.get('genre')
        add_information_to_id_genre_database(id_genre, genre)
    return render_template('create_id_genre.html', message=message)


@app.route('/create_character/', methods=['post', 'get'])
def create_character():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name')
        information = request.form.get('information')
        id_anime = request.form.get('id_anime')
        add_information_to_about_anime_database(name, information, id_anime)
    return render_template('create_character.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
