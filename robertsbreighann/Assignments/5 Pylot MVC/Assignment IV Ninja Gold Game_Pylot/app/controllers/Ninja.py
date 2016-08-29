from system.core.controller import *
from time import strftime
import random


class Ninja(Controller):
    def __init__(self, action):
        super(Ninja, self).__init__(action)

        if 'gold' not in session:
            session['gold'] = 0
        if 'activity' not in session:
            session['activity'] = []

    def index(self):
        TD = strftime('%Y/%m/%d %I:%M %p')
        return self.load_view('index.html',
                                time=TD,
                                gold=session['gold'])

    def process_money(self):
        buildings = {
            'farm':random.randint(5,10),
            'cave':random.randint(0,30),
            'house':random.randint(0,5),
            'casino':random.randint(-50,50)
        }
        gold = buildings[request.form['building']]
        session['gold'] += gold
        result = {
            'class': ('red','green')[gold > 0],
            'activity': "You went to the {} and {} {} gold!".format(request.form['building'],
            ('lost','gained')[gold > 0], gold)
                            }
     
        session['activity'].append(result)
        for ele in session['activity']:
            print ele
        return redirect('/')
