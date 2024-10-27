from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update_leader', methods=['POST'])
def update_leader_route():
    """Endpoint to update the leader based on node metrics."""
    data = request.json
    if not data or 'node_metrics' not in data:
        return jsonify({"error": "No node metrics provided!"}), 400

    node_metrics = data['node_metrics']
    # Assuming model.update_leader(node_metrics) is defined
    leaders = model.update_leader(node_metrics)
    return jsonify({"new_leaders": leaders})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=45075)  # Ensure the correct port is set
