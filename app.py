from flask import Flask, render_template, redirect, url_for, request
# To add a new controller to Main Application first import the Class
# from controllers.example_controller import example_controller
from controllers.graph_controller import graph_controller

app = Flask(__name__)
app.secret_key = 'SECRET'

# Then register a blueprint with the controller
# app.register_blueprint(example_controller)
app.register_blueprint(graph_controller)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/movie/<name>/', defaults={'show_type': "normal"})
# @app.route('/movie/<name>/<show_type>')
# def method_name(name, show_type):
#     return render_template('movie.html', name=name, show_type=show_type)


if __name__ == "__main__":
    app.run(debug=True)
