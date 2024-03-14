from app import app, db
from app.models import Client, ClientSchema, client_fields
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)

@app.route("/clients", methods=["POST"])
@jwt_required()
def add_client():
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "No client data provided"}), 400
    
    trade_name = data.get("trade_name")
    if not trade_name:
        return jsonify({"error": "No client 'trade_name' provided"}), 400

    try:
        client_data = {}
        for field in client_fields:
            client_data[field] = data.get(field)

        new_client = Client(**client_data)
        db.session.add(new_client)
        db.session.commit()

    except Exception as E:
        return jsonify({"error": E}), 400

    return jsonify({"data": client_schema.dump(new_client)}), 201

@app.route("/clients", methods=["GET"])
@jwt_required()
def get_clients():
    clients = Client.query.all()
    return jsonify(clients_schema.dump(clients)), 200

@app.route('/clients/<int:id>', methods=['GET'])
@jwt_required()
def get_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({"error" : "Client not found."}), 404
    return jsonify(client_schema.dump(client)), 200

@app.route('/clients/<int:id>', methods=['PUT'])
@jwt_required()
def update_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({"error" : "Client not found."}), 404
    
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "No client data provided"}), 400
    for field in client_fields:
        f = data.get(field)
        if f : setattr(client, field, f)

    db.session.commit()
    return jsonify(client_schema.dump(client)), 200

@app.route('/clients/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({"error" : "Client not found."}), 404

    db.session.delete(client)
    db.session.commit()
    return jsonify({"message" : "Client deleted"}), 200
