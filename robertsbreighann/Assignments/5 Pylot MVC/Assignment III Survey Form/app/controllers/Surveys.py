from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db
   
    def index(self):        
        return self.load_view('index.html')
        
    def surveyProcess(self):
        if "count" not in session:
            session["count"] = 0
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        session['count']+=1        
        return redirect("/result")

    def result(self):        
        data = {
            "name": session['name'],
            "location": session["location"],
            "language": session['language'],
            "comment": session['comment'],
            "count": session['count']
        }
        return self.load_view('result.html', data = data)    
    
    def back(self):
        return redirect("/")        
