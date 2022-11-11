from flask import Blueprint, g, session, url_for, request, render_template

bp = Blueprint('jobs', __name__, url_prefix="/")

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')