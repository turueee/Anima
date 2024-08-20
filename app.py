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

@app.route('/mex/<name>')
def mex(name):
    return render_template('base.html',
                           menu=anistudio(name),
                           title=groopphoto(name),
                           infcharacter=infcharacters(name),
                           photocharacter=photocharacters(name),
                           groop=name,
                           **aniinfo(name))


if __name__ == "__main__":
    app.run(debug=True)
