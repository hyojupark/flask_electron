from flask import render_template
from flask_classful import FlaskView


class BaseView(FlaskView):
    def index(self):
        return render_template('main.html')
