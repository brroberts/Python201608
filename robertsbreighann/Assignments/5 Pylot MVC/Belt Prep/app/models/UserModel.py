from system.core.model import Model

class UserModel(Model):
    def __init__(self):
        super(UserModel, self).__init__()


    def register(self, data):
        if data['pwd'] != data['pwd2']:
            return None

        query = "INSERT INTO user (name, alias, email, pwd)"
        query += "VALUES (:name, :alias, :email, :pwd);"

        print data
        data['pwd'] = self.bcrypt.generate_password_hash(data['pwd'])
        user_id = self.db.query_db(query, data)

        # TODO: Verify this
        if user_id <= 0:
            return None

        query = "SELECT * FROM user WHERE id=:id LIMIT 1;"
        users = self.db.query_db(query, {'id' : user_id})

        if len(users) != 1:
            return None

        return users[0]


    def login(self, data):
        query = "SELECT * FROM user WHERE email=:email LIMIT 1;"
        users = self.db.query_db(query, data)

        if len(users) != 1:
            return None

        user = users[0]
        
        if not self.bcrypt.check_password_hash(user['pwd'], data['pwd']):
            return None

        return user

    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """