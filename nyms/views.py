# Nyms - Application views
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>


from flask import request, jsonify, url_for
from flaskext.genshi import Genshi, render_template
from nyms import app
from nyms.models import Acronym, db


genshi = Genshi(app)
genshi.extensions['html'] = 'html5'


def render(template, **kwargs):
    kwargs.update({
        'static' : lambda res: url_for('static', filename=res),
        'jsescape' : jsescape,
    })
    return render_template(template, kwargs)


def jsescape(string):
    return string.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")


@app.route('/')
def home():
    return render('list-acronyms.html', acronyms=Acronym.query.order_by(Acronym.name).all())


@app.route('/new', methods=['POST'])
def submit_acronym():
    name = request.form['name'].strip()
    descr = request.form['descr'].strip()

    if name == '':
        return jsonify(result='FAILED', error='Empty acronym')
    if descr == '':
        return jsonify(result='FAILED', error='Empty acronym description')
    if Acronym.query.filter_by(name=name).first():
        return jsonify(result='FAILED', error='Acronym already exists')

    acronym = Acronym(name, descr)
    db.session.add(acronym)
    db.session.commit()
    return jsonify(result='OK')


@app.route('/update', methods=['POST'])
def update_acronym():
    name = request.form['name'].strip()
    descr = request.form['descr'].strip()

    if name == '':
        return jsonify(result='FAILED', error='Empty acronym')
    if descr == '':
        return jsonify(result='FAILED', error='Empty acronym description')

    acronym = Acronym.query.filter_by(name=name).first()

    if acronym:
        acronym.description = descr
        db.session.add(acronym)
        db.session.commit()
        return jsonify(result='OK')
    else:
        return jsonify(result='FAILED', error='Acronym does not exist')


@app.route('/delete', methods=['POST'])
def delete_acronym():
    name = request.form['name'].strip()
    if name == '':
        return jsonify(result='FAILED', error='Empty acronym')
    acronym = Acronym.query.filter_by(name=name).first()
    db.session.delete(acronym)
    db.session.commit()
    return jsonify(result='OK')


@app.route('/about')
def about():
    return render('about.html')


@app.route('/contact')
def contact():
    return render('contact.html')
