# Nyms - A simple acronym manager
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>



from flask import Flask, url_for, request, jsonify
from flaskext.genshi import Genshi, render_template


app = Flask(__name__)
genshi = Genshi(app)
genshi.extensions['html'] = 'html5'


def render(template, **kwargs):
    kwargs.update({
        'static' : lambda res: url_for('static', filename=res)
    })
    return render_template(template, kwargs)



class Acronym:
    def __init__(self, acronym, description):
        self.acronym = acronym
        self.description = description


all_acronyms = {

}


def get_acronyms():
    return map(Acronym, all_acronyms)


@app.route('/')
def home():
    return render('list-acronyms.html', acronyms=get_acronyms())


@app.route('/new', methods=['POST'])
def submit_acronym():
    name = request.form['name'].strip()
    descr = request.form['descr'].strip()

    if name == '':
        return jsonify(result='FAILED', error='Empty acronym')
    if descr == '':
        return jsonify(result='FAILED', error='Empty acronym description')
    if name in all_acronyms:
        return jsonify(result='FAILED', error='Acronym already exists')

    acronym = Acronym(name, descr)
    all_acronyms[name] = acronym
    return jsonify(result='OK')


