from . import db


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    sector = db.Column(db.String(), nullable=False)
    website = db.Column(db.String())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'sector': self.sector,
            'website': self.website
        }
