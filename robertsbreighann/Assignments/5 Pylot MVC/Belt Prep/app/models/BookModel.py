from system.core.model import Model

class BookModel(Model):
    def __init__(self):
        super(BookModel, self).__init__()

    def add_book(self, data):
        query = "INSERT INTO book (title, author_id) "
        query += "VALUES (:title, :author_id);"

        book_id = self.db.query_db(query, data)

        if book_id <= 0:
            return None

        return book_id

    def get_books(self):
      return self.db.query_db("SELECT * FROM book;")