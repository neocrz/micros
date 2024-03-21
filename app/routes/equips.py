from app import app, db
from app.models import Equip, EquipSchema, equip_fields
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

equip_schema = EquipSchema()
equips_schema = EquipSchema(many=True)

@app.route("/equips", methods=["POST"])
@jwt_required()
def add_equip():
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "No equipment data provided"}), 400
    
    name = data.get("name")
    if not name:
        return jsonify({"error": "No equipment 'name' provided"}), 400

    try:
        equip_data = {}
        for field in equip_fields:
            equip_data[field] = data.get(field)

        new_equip = Equip(**equip_data)
        db.session.add(new_equip)
        db.session.commit()

    except Exception as E:
        return jsonify({"error": E}), 400

    return jsonify({"data": equip_schema.dump(new_equip)}), 201

@app.route("/equips", methods=["GET"])
@jwt_required()
def get_equips():
    equips = Equip.query.all()
    return jsonify(equips_schema.dump(equips)), 200

@app.route('/equips/<int:id>', methods=['GET'])
@jwt_required()
def get_equip(id):
    equip = Equip.query.get(id)
    if not equip:
        return jsonify({"error" : "Equip not found."}), 404
    return jsonify(equip_schema.dump(equip)), 200

@app.route('/equips/<int:id>', methods=['PUT'])
@jwt_required()
def update_equip(id):
    equip = Equip.query.get(id)
    if not equip:
        return jsonify({"error" : "Equip not found."}), 404
    
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "No equip data provided"}), 400
    for field in equip_fields:
        f = data.get(field)
        if f : setattr(equip, field, f)

    db.session.commit()
    return jsonify(equip_schema.dump(equip)), 200

@app.route('/equips/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_equip(id):
    equip = Equip.query.get(id)
    if not equip:
        return jsonify({"error" : "Equip not found."}), 404

    db.session.delete(equip)
    db.session.commit()
    return jsonify({"message" : "Equip deleted"}), 200
