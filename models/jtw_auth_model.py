from flask_restx import Namespace, reqparse, fields, inputs

api = Namespace('Jwt_Token', description= 'JWT Token for authorization')

token_info = api.parser()
token_info.add_argument('Name',location = 'headers')
token_info.add_argument('Email_id',location = 'headers')
token_info.add_argument('Secret_key',location = 'headers')



