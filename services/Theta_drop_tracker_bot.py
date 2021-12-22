from flask_restx import Resource
import config
from models.thetadrp_model import api, Start_Input_param,Stop_Input_param
from bl.tracker_domain import schedule
from utilities.Jwt_auth import token_required

@api.route('/Change_tracker_behaviour')
class StartTracker(Resource):
    @api.expect(Start_Input_param)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    @token_required
    def post(self):
        behaviour_change_key_word = api.payload['behavior_key_word']
        config.check_for_scheduler_status = behaviour_change_key_word
        schedule()
        if behaviour_change_key_word == 'RUN':
            return 'Successfully Started tracker.'
        else:
            return 'Successfully Stopped tracker.'
