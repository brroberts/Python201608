from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')
    
    def registration(self):
        data = {
            'fname':request.form['fname'],
            'lname':request.form['lname'],
            'email':request.form['email'],
            'password':request.form['password'],
            'confirm':request.form['confirm']
        }
        reg_status =  self.models['User'].register(data)
        if reg_status['status'] == True:
            session['logged'] = True
            session['name'] = data['fname']
            session['rl'] = "registered"
            return redirect('/success')
        else:
            for messages in reg_status['errors']:
                flash(messages)
            return redirect('/')
        
    def user_login(self):
        
        data = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        log_status =  self.models['User'].login(data)
        if log_status:
            session['logged'] = True
            session['name'] = log_status
            session['rl'] = "login"
            return redirect('/success')
        else:
            flash("Invalid email of password")
            return redirect("/")
    
    def success(self):
        print session
        if session['logged']:
            return self.load_view("success.html", name = session['name'],rl=session["rl"])
        else:
            return redirect("/")

    def logout(self):
        return redirect("/")
            

        

