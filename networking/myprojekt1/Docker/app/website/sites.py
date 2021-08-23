from flask import Blueprint, jsonify, request, render_template
from .models import Device
from . import db

sites = Blueprint('sites', __name__)

@sites.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@sites.route('/devices/', methods=['GET', 'POST'])
def get_devices():
    if request.method == 'GET':
        return jsonify({'device': [device.get_url() 
                                for device in Device.query.all()]})
    elif request.method == 'POST':
        device = Device()
        device.import_data(request.json)
        db.session.add(device)
        db.session.commit()
        
        return jsonify({}), 201, {'Location': device.get_url()}


@sites.route('/devices/<int:id>', methods=['GET', 'PUT'])
def get_device(id):
    if request.method == 'GET':
        return jsonify(Device.query.get_or_404(id).export_data())
    if request.method == 'PUT':
        device = Device.query.get_or_404(id)
        device.import_data(request.json)
        db.session.add(device)
        db.session.commit()
        return jsonify({})

@sites.route('/devices/<int:id>/version')
def get_device_version(id):
    device = Device.query.get_or_404(id)
    device_name = device.hostname
    prompt = device_name + "#"
    ip = device.mgmt_ip
    result = get_device_version(device_name, prompt, ip, 'maciej', 'maciej')
    return jsonify({'Location ': str(result)})