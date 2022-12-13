from flask_restful import Resource, fields, marshal_with
from app.models import Customer as CustomerModel

customer_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'sector': fields.String,
    'website': fields.String,
}


class Customer(Resource):
    @marshal_with(customer_fields)
    def get(self, id):
        customer = CustomerModel.query.filter_by(id=id).first()
        return customer


class CustomerList(Resource):
    @marshal_with(customer_fields, envelope='customers')
    def get(self):
        customers = CustomerModel.query.all()
        return customers
