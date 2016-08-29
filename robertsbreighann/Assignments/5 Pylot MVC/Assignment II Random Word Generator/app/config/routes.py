
from system.core.router import routes

routes['default_controller'] = 'Random'
routes['/generate'] = 'Random#generate'
