from app import APP
import requests
from flask import jsonify, request

@APP.route('/', methods=['POST'])
def getNearBy():
    if request.method == 'POST':
        resp = requests.post('http://198.199.70.165/ShareCab/index.php/api', data=request.args)
        return resp.text
    resp = requests.post('http://198.199.70.165/ShareCab/index.php/api', data=request.args)
    return resp.text
