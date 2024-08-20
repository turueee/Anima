from flask import Flask
from flask import render_template
from flask import url_for
from data import mexadatas
from data import anistudio
from data import aniinfo
from data import infcharacters
from data import photocharacters
from data import groopphoto

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
                           infcharacter=infcharacters('Евангелион'),
                           photocharacter=photocharacters('Евангелион'),
                           groop=groopphoto('Евангелион'),
                           **aniinfo('Евангелион'))


@app.route('/Darling')
def Darling():
    return render_template('base.html',
                           menu=anistudio('Милый во Франксе'),
                           title='Милый во Франксе',
                           infcharacter=infcharacters('Милый во Франксе'),
                           photocharacter=photocharacters('Милый во Франксе'),
                           groop=groopphoto('Милый во Франксе'),
                           **aniinfo('Милый во Франксе'))


@app.route('/Gurren')
def Gurren():
    return render_template('base.html',
                           menu=anistudio('Гуррен-Лаганн'),
                           title='Гуррен-Лагган',
                           infcharacter=infcharacters('Гуррен-Лаганн'),
                           photocharacter=photocharacters('Гуррен-Лаганн'),
                           groop=groopphoto('Гуррен-Лаганн'),
                           **aniinfo('Гуррен-Лаганн'))


@app.route('/Greh')
def Greh():
    return render_template('base.html',
                           menu=anistudio('Корона грешника'),
                           title='Корона Грешника',
                           infcharacter=infcharacters(''),
                           photocharacter=photocharacters('Корона Грешника'),
                           groop=groopphoto('Корона Грешника'),
                           **aniinfo('Корона Грешника'))


@app.route('/Code')
def Code():
    return render_template('base.html',
                           menu=anistudio('Код Гиас'),
                           title='Код Гиас',
                           infcharacter=infcharacters('Код Гиас'),
                           photocharacter=photocharacters('Код Гиас'),
                           groop=groopphoto('Код Гиас'),
                           **aniinfo('Код Гиас'))


@app.route('/EightySix')
def EightySix():
    return render_template('base.html',
                           menu=anistudio('Восемьдесят шесть'),
                           title='Восемьдесят шесть',
                           infcharacter=infcharacters('Восемьдесят шесть'),
                           photocharacter=photocharacters('Восемьдесят шесть'),
                           groop=groopphoto('Восемьдесят шесть'),
                           **aniinfo('Восемьдесят шесть'))


if __name__ == "__main__":
    app.run(debug=True)
