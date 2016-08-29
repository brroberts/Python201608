"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Ninja'
routes['POST']['/process_money'] = 'Ninja#process_money'
