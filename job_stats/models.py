from .extensions import db, ma
from marshmallow import Schema, fields
import simplejson
from sqlalchemy.dialects.postgresql import VARCHAR, TEXT, DATE, NUMERIC, TIMESTAMP


class Listing(db.Model):

    __tablename__ = "listings"

    title = db.Column(VARCHAR(256), nullable=False)
    company = db.Column(VARCHAR(256), nullable=False)
    url = db.Column(TEXT, nullable=False, primary_key=True)
    location = db.Column(VARCHAR)
    salary = db.Column(NUMERIC)
    summary = db.Column(TEXT)
    posted = db.Column(DATE, nullable=False)
    scraped = db.Column(TIMESTAMP, nullable=False)


class ListingSchema(Schema):
    title = fields.Str()
    company = fields.Str()
    url = fields.Url()
    location = fields.Str()
    salary = fields.Float()
    summary = fields.Str()
    posted = fields.Date()
    scraped = fields.DateTime()

    class Meta:
        model = Listing
        json_module = simplejson
