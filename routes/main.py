from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def homepage():
    return render_template('homepage.html')