"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)

        self.load_model('CourseModel')
        self.db = self._app.db


    def index(self):
        courses = self.models['CourseModel'].get_courses()
        return self.load_view('index.html', courses=courses)

    def add(self):
        if 'name' not in request.form:
            flash('Must have a name')
            return redirect('/')
        elif len(request.form['name']) < 2:
            flash('Must have a name')
            return redirect('/')
        else:
            course_details = {
                'name' : request.form['name'],
                'description' : [request.form['description'] if 'description' in request.form else 'None']
            }
            self.models['CourseModel'].add_course(course_details)

        return redirect('/')

    def delete_confirm(self,id):
        course = self.models['CourseModel'].get_course(id)
        return self.load_view('delete.html', course=course)


    def delete(self,id):
        if request.form['submit'] == 'yes':
            self.models['CourseModel'].delete_course(id)
        return redirect('/')
