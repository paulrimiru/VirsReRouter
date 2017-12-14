from app import APP
import requests
from flask import jsonify, request

@APP.route('/', methods=['POST'])
def getNearBy():
    if request.method == 'POST':
        resp = requests.post('http://198.199.70.165/ShareCab/index.php/api', data=request.args.to_dict())
        return resp.text
    resp = requests.post('http://198.199.70.165/ShareCab/index.php/api', data=request.args.to_dict())
    return resp.text
@APP.route('/wahindi/<endpoint>', methods=['POST'])
def wahindiUrl(endpoint):
    if request.method == 'POST':
        resp = requests.post('http://198.199.70.165:8080/ShareCab/'+endpoint, data=request.args.to_dict())
        return resp.text
    resp = requests.post('http://198.199.70.165:8080/ShareCab/'+endpoint, data=request.args.to_dict())
    return resp.text