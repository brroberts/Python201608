from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['POST']["/registration"] = 'Welcome#registration'
routes['POST']['/login'] = "Welcome#user_login"
routes['/success'] = 'Welcome#success'
routes['/logout'] = 'Welcome#logout'

