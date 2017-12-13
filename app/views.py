from app import APP
import requests
from flask import jsonify

@APP.route('/nearby', methods=['GET'])
def getNearBy():
    resp = requests.post('http://198.199.70.165/ShareCab/index.php/api', data={'trans_type':'online'})
    return resp.text
