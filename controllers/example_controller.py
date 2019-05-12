from flask import Blueprint, render_template
# import peewee

# Instance your controller with Blueprint
example_controller = Blueprint('example_controller', __name__,
                               template_folder='templates/example')


@example_controller.route('/example')
def example():
    return render_template('example/example.html')
