from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for, session, request, flash
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from main_application_web import main
import os
from src.utils.moving_pic import rename


app = Flask(__name__)


class Item(object):
    def __init__(self, image, batiment):
        self.image = image
        self.batiment = batiment


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/landmark_recognition')
def landmark_recognition():
    return render_template('landmark_recognition.html')


class ItemForm(Form):
    folderpath = StringField('folderpath', [validators.Length(min=1, max=200)])


IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/add_folderpath', methods=['GET', 'POST'])
def add_folderpath():
    form = ItemForm(request.form)
    if request.method == 'POST' and form.validate():
        folderpath = form.folderpath.data
        rename(folderpath)
        flash('Path well received', 'success')
        return redirect(url_for('results'))

    return render_template('add_folderpath.html', form=form)


@app.route('/results')
def results():
    IMG_LIST = os.listdir('static')
    imagelist = IMG_LIST
    res = main('data/data_test_web')
    return render_template('results.html', imagelist=imagelist, res=res)


if __name__ == '__main__':
    app.run(debug=True)
