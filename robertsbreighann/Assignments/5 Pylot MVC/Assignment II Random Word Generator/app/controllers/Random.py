"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import string
import random

class Random(Controller):
    def __init__(self, action):
        super(Random, self).__init__(action)
        if not session:
            session['count'] = 0
            session['word'] = ''

    def index(self):
        return self.load_view('index.html', count=session['count'], word=session['word'])

    def generate(self):
        session['word'] = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(14))
        session['count'] += 1
        return redirect('/')
