from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    current_app
)
from .models import Listing, ListingSchema

bp = Blueprint("jobs", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@bp.route("/get", methods=["GET"])
def get_all():
    """
    query: string: title: Filters results by title. Looks for the existence of "title" in the actual title, not exact matching.
    query: string: location: Filters results by location by fuzzy matching.
    query: integer: salary: Returns results filtered by equal to or greater than desired salary. Does not currently support hourly wages.   
    query: bool: desc: if True, order by descending, else ascending.
    """

    listings = Listing.query

    args = request.args

    if 'title' in args:
        listings = listings.filter_by(title=args['title'])

    if 'location' in args:
        listings = listings.filter(Listing.location.ilike(args['location']))

    if 'salary' in args:
        listings = listings.filter(Listing.salary >= args['salary'])

    if 'desc' in args:
        if bool(args['desc']):
            listings = listings.order_by(Listing.posted.desc())
        else:
            listings = listings.order_by(Listing.posted)

    listing_schema = ListingSchema(many=True)

    return jsonify(listing_schema.dump(listings)), 200
