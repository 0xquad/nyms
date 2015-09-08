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
        'static' : lambda res: url_for('static', filename=res)
    })
    return render_template(template, kwargs)



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


