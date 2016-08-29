from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db

    def index(self):
        product_data = self.models['Product'].get_all()
        return self.load_view('index.html', product_data=product_data)

    def new(self):
        return self.load_view("add.html")

    def create(self):
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        self.models['Product'].create_product(data)
        return redirect("/")

    def show(self, id):
        product = self.models['Product'].get_product(id)
        return self.load_view('show.html', product = product)

    def edit(self,id):
        product = self.models['Product'].get_product(id)
        return self.load_view('edit.html', product = product)

    def update(self,id):
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price'],
            'id': id
        }
        self.models['Product'].update_product(data)
        return redirect('/')

    def destroy(self,id):
        self.models['Product'].destroy_product(id)
        return redirect('/')
