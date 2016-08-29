from system.core.router import routes

routes['default_controller'] = 'Products'
routes['/products/new'] = 'Products#new'
routes['POST']['/products/create'] = 'Products#create'
routes['/products/edit/<id>'] = 'Products#edit'
routes['POST']['/products/udpate/<id>'] = 'Products#udpate'
routes['/products/destroy/<id>'] = 'Products#destroy'