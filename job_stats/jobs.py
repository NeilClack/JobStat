from flask import Blueprint, render_template, request, jsonify
from .models import Listing, ListingSchema
from marshmallow.exceptions import ValidationError
from datetime import datetime

bp = Blueprint("jobs", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@bp.route("/jobs", methods=["GET", "POST"])
def get_jobs():
    if request.method == "GET":
        listings = Listing.query

        args = request.args

        if "title" in args:
            listings = listings.filter_by(title=args["title"])

        if "location" in args:
            listings = listings.filter(Listing.location.ilike(args["location"]))

        if "salary" in args:
            listings = listings.filter(Listing.salary >= args["salary"])

        if "company" in args:
            company_string = f"%{args['company']}%"
            listings = listings.filter(Listing.company.ilike(company_string))

        if "desc" in args:
            if bool(args["desc"]):
                listings = listings.order_by(Listing.posted.desc())
            else:
                listings = listings.order_by(Listing.posted)

        listings = listings.all()

        if not listings:
            return "No jobs listed here. Please alter your query.", 400

        listing_schema = ListingSchema(many=True)

        return jsonify(listing_schema.dump(listings)), 200

    if request.method == "POST":
        data = request.json

        listing_schema = ListingSchema()

        try:
            new_listing = listing_schema.load(data)
        except ValidationError:
            return (
                jsonify(
                    {
                        "Error": "Provided data is not valid. Please ensure all fields are properlly formatted and contain relavent information."
                    }
                ),
                400,
            )

        # job_listing = Listing(
        #     title=data['title'],
        #     company=data['company'],
        #     location=data['location'],
        #     posted=datetime.strptime(data['posted'], "%Y-%m-%d"),
        #     entered=datetime.strptime(data['entered'], "%Y-%m-%dT%H:%M:%S.%f")
        # )

        return listing_schema.dumps(new_listing), 200
