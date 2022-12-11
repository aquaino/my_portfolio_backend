from flask_restful import Resource

customers = [
    {'name': 'Test 1'},
    {'name': 'Test 2'}
]


class Customer(Resource):
    def get(self, id):
        return customers[id]


class CustomerList(Resource):
    def get(self):
        return customers
