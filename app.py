from flask import Flask
from flask import render_template
from flask import url_for
from data import mexadatas
from data import anistudio
from data import aniinfo

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


@app.route('/Evangelion')
def Evangelion():
    return render_template('base.html',
                           menu=anistudio('Евангелион'),
                           title='Евангелион',
                           **aniinfo('Евангелион'))


@app.route('/Darling')
def Darling():
    return render_template('base.html',
                           menu=anistudio('Милый во Франксе'),
                           title='Милый во Франксе',
                           **aniinfo('Милый во Франксе'))


@app.route('/Gurren')
def Gurren():
    return render_template('base.html',
                           menu=anistudio('Гуррен-Лаганн'),
                           title='Гуррен-Лагган',
                           **aniinfo('Гуррен-Лаганн'))


@app.route('/Greh')
def Greh():
    return render_template('base.html',
                           menu=anistudio('Корона грешника'),
                           title='Корона Грешника',
                           **aniinfo('Корона грешника'))


@app.route('/Code')
def Code():
    return render_template('base.html',
                           menu=anistudio('Код Гиас'),
                           title='Код Гиас',
                           **aniinfo('Код Гиас'))


@app.route('/EightySix')
def EightySix():
    return render_template('base.html',
                           menu=anistudio('Восемьдесят шесть'),
                           title='Восемьдесят шесть',
                           **aniinfo('Восемьдесят шесть'))


if __name__ == "__main__":
    app.run(debug=True)
