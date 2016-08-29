from system.core.model import Model

class AuthorModel(Model):
    def __init__(self):
        super(AuthorModel, self).__init__()


    def get_authors(self):
        query = "SELECT id, name FROM author;"
        authors = self.db.query_db(query)

        return { author['id']:author['name'] for author in authors }

    def add_author(self, data):
        print 'woot'
        query = "INSERT INTO author (name) VALUES (:name);"
        return self.db.query_db(query, {'name' : data['author']})
