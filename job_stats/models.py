from .extensions import db, ma
import simplejson
from sqlalchemy.dialects.postgresql import VARCHAR, TEXT, DATE, NUMERIC, TIMESTAMP


class Listing(db.Model):

    __tablename__ = "listings"

    title = db.Column(VARCHAR(120), nullable=False)
    company = db.Column(VARCHAR(50), nullable=False)
    url = db.Column(TEXT, nullable=False, primary_key=True)
    location = db.Column(VARCHAR)
    salary = db.Column(NUMERIC)
    summary = db.Column(TEXT)
    posted = db.Column(DATE, nullable=False)
    entered = db.Column(TIMESTAMP, nullable=False)


class ListingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Listing
        json_module = simplejson
