from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def register(self,data):
        name_regex = re.compile(r'[0-9]')
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        query = "SELECT first_name from users where email=:email"
        query_data = {
            'email':data['email'],                
        }
        user_data = self.db.query_db(query, query_data)

        if len(data['fname']) < 2:
            errors.append('First name should atleast be two characters')
        if len(data['fname']) < 2:
            errors.append('First name should atleast be two characters')
        if name_regex.match(data['fname']):
            errors.append('First name should not have numbers')
        if name_regex.match(data['lname']):
            errors.append('Last name should not have numbers')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('Invalid Email')
        if len(data['password']) < 8:
            errors.append('Password should be minimum 8 characters')
        if data['confirm'] !=data['password']:
            errors.append('Confirm password should match password')
        if user_data:
            errors.append('Email already exists')
        
        if errors:
            return {'status':False,'errors':errors}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(data['password'])
            query = "INSERT into users (first_name,last_name,email,password,created_at,updated_at) values (:fname,:lname,:email,:password,NOW(),NOW())"
            query_data = {
                'fname': data['fname'],
                'lname': data["lname"],
                'email':data['email'],
                'password': hashed_pw
            }
            self.db.query_db(query, query_data)
            return {'status': True}

    def login(self,data):
        query = "SELECT first_name,password from users where email=:email"
        query_data = {
            'email': data['email'],                
        }
        user_data = self.db.query_db(query, query_data)
        print user_data
        
        if len(user_data)==1:
            if self.bcrypt.check_password_hash(user_data[0]['password'], data['password']):
                return user_data[0]['first_name']
        else:
            return False
