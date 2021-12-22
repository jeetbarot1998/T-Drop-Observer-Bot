from flask_restx import Resource
from flask import request, jsonify
from utilities.Jwt_auth import create_token
import config
from models.jtw_auth_model import api, token_info

@api.route('/key_gen')
class GenerateJwtKey(Resource):
    @api.expect(token_info)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    def post(self):
        """ GENERATE JWT KEY FOR AUTHORIZATION """
        if (not request.headers['Name']
                and not request.headers['Email_id']
                and not request.headers['Secret_key']):
            return 'You are not authorized'

        incoming_key = request.headers['Secret_key']
        if incoming_key not in config.Secret_key:
            return 'You are not authorized'

        authorized = False
        user_email_id = config.Private_key
        for index, entries in enumerate(config.user_detials_list):
            if user_email_id == entries['email']:
                user_details = config.user_detials_list[index]
                authorized = True

        if not authorized:
            return 'You are not authorized'

        user_email_id = config.Private_key
        token = create_token(user_details, 100, user_email_id)

        return jsonify(token)




