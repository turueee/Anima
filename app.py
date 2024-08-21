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


if __name__ == "__main__":
    app.run(debug=True)
