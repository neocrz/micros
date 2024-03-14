from app import app, db
from app.models import Client, ClientSchema
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
        new_client = Client(
                address=data.get("address"),
                address_num = data.get("address_num"),
                business_name = data.get("business_name"),
                trade_name = data.get("trade_name")
                )
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
    
    address = data.get("address")
    if address : client.address = address
    address_num = data.get("address_num")
    if address_num : client.address_num = address_num
    business_name = data.get("business_name")
    if business_name : client.business_name = business_name
    trade_name = data.get("trade_name")
    if trade_name : client.trade_name = trade_name

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
