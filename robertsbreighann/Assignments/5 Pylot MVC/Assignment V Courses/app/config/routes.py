
from system.core.router import routes

routes['default_controller'] = 'Courses'
routes['POST']['/courses/add'] = 'Courses#add'
routes['POST']['/courses/delete/<id>'] = 'Courses#delete_confirm'
routes['POST']['/courses/delete_confirm/<id>'] = 'Courses#delete'
