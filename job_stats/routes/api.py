from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
)
from ..models import Listing, ListingSchema
from marshmallow import ValidationError
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.schema import Table, MetaData
from sqlalchemy.exc import OperationalError, ProgrammingError

from ..extensions import db
import sys


bp = Blueprint("jobs", __name__, url_prefix="/")


@bp.route("/api", methods=["GET"])
def index():
    return render_template("index.html")


@bp.route("/add", methods=["POST"])
def add_job():

    data = request.json

    if type(data) == list:
        try:
            new_jobs = ListingSchema(many=True).load(data)
        except ValidationError as err:
            return jsonify({"ValidationError": err.messages})
    else:
        try:
            new_jobs = ListingSchema().load(data)
        except ValidationError as err:
            return jsonify({"ValidationError": err.messages})

    with db.engine.connect() as conn:
        table = Table("listings", MetaData(), autoload_with=db.engine)
        try:
            insert_stmt = (
                insert(table)
                .values(data)
                .on_conflict_do_nothing(index_elements=["url"])
            )
        except:
            print(sys.exc_info)
            msg = {"msg": "Unable to create insert statement."}
            return jsonify(msg), 500

        try:
            conn.execute(insert_stmt)
            msg = {"msg": "Insert statement executed. New jobs saved to database"}
            return jsonify(msg), 200
        except ProgrammingError as e:
            msg = {"msg": "Unable to execute statement.", "stmt": insert_stmt}
            return jsonify(msg), 500


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
            listings = listings.order_by(Listing.psysted.desc())
        else:
            listings = listings.order_by(Listing.psysted)

    listing_schema = ListingSchema(many=True)

    jobs = listing_schema.dump(listings)

    return jsonify(jobs), 200
