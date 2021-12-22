from flask_restx import Namespace, reqparse, fields, inputs
from werkzeug.datastructures import FileStorage


api = Namespace('Theta_Drop', description = 'Theta Drop API to start and stop Tracker BOT')

Start_Input_param = api.model(
    'Start_Input_param',{
        'behavior_key_word': fields.String(attribute = 'behavior_key_word'),
    }
)

Stop_Input_param = api.model(
    'Stop_Input_param',{
        'Stop': fields.String(attribute = 'Stop'),
    }
)