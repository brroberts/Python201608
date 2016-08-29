"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('UserModel')

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    # routes['GET']['/'] = 'Welcome#index'
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """

        if 'user' in session: return redirect('/books')
        return self.load_view('index.html')


    # routes['POST']['/'] = 'Welcome#process'
    def process(self):
        if self.checkIfError(request.form, ['action']):
            return redirect('/')

        if request.form['action'] == 'Register':
            if self.checkIfError(request.form, ['email', 'pwd', 'name', 'pwd2', 'alias']):
                return redirect('/')

            d = {}
            for i in request.form: d[i] = request.form[i]

            print "--------------------------"
            session['user'] = self.models['UserModel'].register(d)
            return redirect('/books')

        elif request.form['action'] == 'Login':

            if self.checkIfError(request.form, ['email', 'pwd']):
                return redirect('/')

            session['user'] = self.models['UserModel'].login(request.form)
            return redirect('/books')
        

    def checkIfError(self, dictionary, keys):
        for key in keys:
            if not key in dictionary: return True
        return False

