from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
)
from ..models import Listing, ListingSchema
from ..extensions import db


bp = Blueprint("jobs", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@bp.route("/add", methods=["POST"])
def add_job():

    data = request.json
    new_job_schema = ListingSchema()

    if type(data) == list:
        for job in data:
            new_job = new_job_schema.load(job)
    else:
        new_job = new_job_schema.load(job)

    return jsonify({"msg": "Saved"}), 200


@bp.route("/get", methods=["GET"])
def get_all():

    listings = Listing.query

    args = request.args

    if "title" in args:
        if "exact" in args:
            listings = listings.filter(Listing.title.ilike(args["title"]))
        else:
            listings = listings.filter(Listing.title.contains(args["title"]))

    if "company" in args:
        if "exact" in args:
            listings = listings.filter(Listing.title.ilike(args["company"]))
        else:
            listings = listings.filter(Listing.title.contains(args["company"]))

    if "location" in args:
        listings = listings.filter(Listing.location.ilike(args["location"]))

    if "salary" in args:
        listings = listings.filter(Listing.salary >= args["salary"])

    if "desc" in args:
        if bool(args["desc"]):
            listings = listings.order_by(Listing.posted.desc())
        else:
            listings = listings.order_by(Listing.posted)

    listing_schema = ListingSchema(many=True)

    jobs = listing_schema.dump(listings)

    return jsonify(jobs), 200
