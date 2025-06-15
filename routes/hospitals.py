from flask import Blueprint, request, jsonify
from models.db import get_db_connection

hospitals_bp = Blueprint('hospitals', __name__)

# 🔹 GET all requests
@hospitals_bp.route('/requests', methods=['GET'])
def get_requests():
    conn = get_db_connection()
    requests = conn.execute('SELECT * FROM hospital_requests').fetchall()
    conn.close()

    request_list = []
    for req in requests:
        request_list.append({
            'id': req['id'],
            'hospital_name': req['hospital_name'],
            'blood_group': req['blood_group'],
            'quantity': req['quantity'],
            'status': req['status']
        })

    return jsonify(request_list), 200

# 🔹 POST new blood request
@hospitals_bp.route('/requests/add', methods=['POST'])
def add_request():
    data = request.get_json()
    hospital_name = data.get('hospital_name')
    blood_group = data.get('blood_group')
    quantity = data.get('quantity')

    if not all([hospital_name, blood_group, quantity]):
        return jsonify({'error': 'All fields are required'}), 400

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO hospital_requests (hospital_name, blood_group, quantity) VALUES (?, ?, ?)',
        (hospital_name, blood_group, quantity)
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Blood request submitted successfully'}), 201
