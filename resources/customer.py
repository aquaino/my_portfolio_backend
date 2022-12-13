from flask_restful import Resource, fields, marshal_with, marshal
from app.models import Customer as CustomerModel
from flask import Response

customer_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'sector': fields.String,
    'website': fields.String,
}


class Customer(Resource):
    def get(self, id):
        customer = CustomerModel.query.filter_by(id=id).first()
        if customer:
            return marshal(customer, customer_fields), 200
        else:
            return None, 200


class CustomerList(Resource):
    def get(self):
        customers = CustomerModel.query.all()
        if customers:
            return marshal(customers, customer_fields), 200
        else:
            return [], 200
