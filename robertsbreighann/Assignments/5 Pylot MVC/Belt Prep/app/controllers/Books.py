"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('BookModel')
        self.load_model('AuthorModel')
        self.load_model('ReviewModel')

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    # routes['GET']['/books'] = 'Books#index'
    def index(self):
        if not 'user' in session: return redirect('/')

        books = self.models['BookModel'].get_books()
        reviews = self.models['ReviewModel'].get_recent()

        return self.load_view('books.html', reviews=reviews, books=books)


    # routes['GET']['/books/add'] = 'Books#add'
    def add(self):
        if not 'user' in session: return redirect('/')
        authors = self.models['AuthorModel'].get_authors()

        return self.load_view('addbook.html', authors=authors)


    # routes['POST']['/books/add'] = 'Books#process'
    def process(self):
        if self.checkIfError(request.form, ['title', 'author_list', 'author', 'review', 'rating']):
            return redirect('/')

        if request.form['author_list'] != '0':
            author_id = request.form['author_list']
        else:
            if len(request.form['author']) < 2:
                flash('type in a real name')
                return redirect('/')

            author_id = self.models['AuthorModel'].add_author(request.form)

        data = dict(request.form)
        data['author_id'] = author_id
        book_id = self.models['BookModel'].add_book(data)

        data = {
            'user_id': session['user']['id'],
            'book_id': book_id,
            'review': request.form['review'],
            'rating': request.form['rating']
        }
        review = self.models['ReviewModel'].add_review(data)

        return redirect('/books')

        
        
    def checkIfError(self, dictionary, keys):
        for key in keys:
            if not key in dictionary: return True
        return False

