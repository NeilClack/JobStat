from flask import Blueprint, g, session, url_for, request, render_template, jsonify
from .models import Listing, ListingSchema

bp = Blueprint('jobs', __name__, url_prefix="/")

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/get', methods=["GET"])
def get_all():
    title = request.args.get('title', default=None, type=str)

    # Filter by keyword in title
    if title is not None:
        title = f"%{title}%"
        listings = Listing.query.filter(Listing.title.like(title))
    else:
        listings = Listing.query.all()
    
    
    listing_schema = ListingSchema(many=True)

    return jsonify(listing_schema.dump(listings)), 200
