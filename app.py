from flask import Flask, jsonify, request

app = Flask(__name__)

items = []


@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        update_data = request.get_json()
        item.update(update_data)
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
