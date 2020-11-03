from flask_restful import reqparse


parser_create = reqparse.RequestParser()
parser_create.add_argument("phone", required=True, type=str)
parser_create.add_argument("email", required=True, type=str)
parser_create.add_argument("name", required=True, type=str)
