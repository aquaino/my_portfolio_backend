from flask_restful import Resource, fields, marshal, reqparse
from app.models import db, Customer as CustomerModel
from flask import Response, request

# Input
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('sector', type=str, required=True)
parser.add_argument('website', type=str)

# Output (marshalling)
customer_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'sector': fields.String,
    'website': fields.String,
}


class Customer(Resource):

    # Get a customer
    def get(self, id):
        customer = CustomerModel.query.filter_by(id=id).first()
        if customer:
            return marshal(customer, customer_fields), 200
        else:
            return Response(status=404)

    # Update a customer
    def put(self, id):
        customer = CustomerModel.query.filter_by(id=id).first()
        if customer:
            args = parser.parse_args()
            customer.name = args['name']
            customer.sector = args['sector']
            customer.website = args['website']
            db.session.commit()
            return marshal(customer, customer_fields), 200
        else:
            return Response(status=404)

    # Delete a customer
    def delete(self, id):
        customer = CustomerModel.query.filter_by(id=id).first()
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return Response(status=204)
        else:
            return Response(status=404)


class CustomerList(Resource):

    # Get all customers
    def get(self):
        customers = CustomerModel.query.all()
        if customers:
            return marshal(customers, customer_fields), 200
        else:
            return [], 200

    # Create a customer
    def post(self):
        args = parser.parse_args()
        customer = CustomerModel(
            name=args['name'], sector=args['sector'], website=args['website'])

        db.session.add(customer)
        db.session.commit()

        return marshal(customer, customer_fields), 201
