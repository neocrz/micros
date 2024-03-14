from app import app, db
from app.models import Client, ClientSchema
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)
client_fields = ("id",
                  "address",
                  "address_num",
                  "business_name",
                  "city",
                  "client_type",
                  "cnpj",
                  "contact_name",
                  "cpf",
                  "email",
                  "ie",
                  "im",
                  "phone1",
                  "phone2",
                  "phone3",
                  "rg",
                  "state",
                  "trade_name",
                  "zip_code"
                  )
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
                city = data.get("city"),
                client_type = data.get("client_type"),
                cnpj = data.get("cnpj"),
                contact_name = data.get("contact_name"),
                cpf = data.get("cpf"),
                email = data.get("email"),
                ie = data.get("ie"),
                im = data.get("im"),
                phone1 = data.get("phone1"),
                phone2 = data.get("phone2"),
                phone3 = data.get("phone3"),
                rg = data.get("rg"),
                state = data.get("state"),
                trade_name = data.get("trade_name"),
                zip_code = data.get("zip_code")
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
