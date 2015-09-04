# Nyms - A simple acronym manager
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>



from flask import Flask, url_for
from flaskext.genshi import Genshi, render_template


app = Flask(__name__)
genshi = Genshi(app)
genshi.extensions['html'] = 'html5'


def render(template, **kwargs):
    kwargs.update({
        'static' : lambda res: url_for('static', filename=res)
    })
    return render_template(template, kwargs)



# Import anything that depended on `app`
from nyms.views import *
from nyms.models import *
