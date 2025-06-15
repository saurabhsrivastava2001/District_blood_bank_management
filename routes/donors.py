from flask import Blueprint, request, jsonify
from models.db import get_db_connection

donors_bp = Blueprint('donors', __name__)

# 🔹 GET all donors
@donors_bp.route('/donors', methods=['GET'])
def get_donors():
    conn = get_db_connection()
    donors = conn.execute('SELECT * FROM donors').fetchall()
    conn.close()

    donor_list = []
    for donor in donors:
        donor_list.append({
            'id': donor['id'],
            'name': donor['name'],
            'age': donor['age'],
            'blood_group': donor['blood_group'],
            'contact': donor['contact']
        })

    return jsonify(donor_list), 200

# 🔹 POST new donor
@donors_bp.route('/donors/add', methods=['POST'])
def add_donor():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    blood_group = data.get('blood_group')
    contact = data.get('contact')

    if not all([name, age, blood_group, contact]):
        return jsonify({'error': 'All fields are required'}), 400

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO donors (name, age, blood_group, contact) VALUES (?, ?, ?, ?)',
        (name, age, blood_group, contact)
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Donor added successfully'}), 201
