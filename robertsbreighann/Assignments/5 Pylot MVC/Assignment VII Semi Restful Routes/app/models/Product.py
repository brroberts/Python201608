from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    
    def get_all(self):
        query = "SELECT * from products"
        product_data = self.db.query_db(query)
        return product_data
    
    def create_product(self,data):
        query = "INSERT into products (name,description,price,created_at,updated_at) values (:name, :description, :price, NOW(), NOW())"        
        self.db.query_db(query,data)
        return True

    def get_product(self,id):
        query = "SELECT * from products where id = :id"
        data = {'id': id}
        product_data = self.db.query_db(query,data)[0]
        return product_data

    def update_product(self, data):
        query = "UPDATE products SET name=:name, description=:description,price=:price,updated_at = NOW() where id = :id"
        return self.db.query_db(query,data)

    def destroy_product(self,id):
        query = "DELETE from products where id=:id"
        data = {'id':id}
        self.db.query_db(query,data)
        return True
        
