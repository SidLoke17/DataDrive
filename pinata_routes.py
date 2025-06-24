from flask import Blueprint, request, jsonify
from services.pinata_service import pin_json_to_pinata, pin_file_to_pinata, list_pinned_files_from_pinata, unpin_file_from_pinata

pinata_routes = Blueprint('pinata_routes', __name__)

@pinata_routes.route('/pin-log', methods=['POST'])
def pin_log():
    log_data = request.json
    pinata_response = pin_json_to_pinata(log_data)
    if "IpfsHash" in pinata_response:
        return jsonify({"message": "Log pinned successfully", "IpfsHash": pinata_response["IpfsHash"]}), 200
    else:
        return jsonify({"error": "Failed to pin log"}), 500

@pinata_routes.route('/upload-report', methods=['POST'])
def upload_report():
    report_data = request.json
    filepath = "report.json"
    with open(filepath, 'w') as report_file:
        json.dump(report_data, report_file)
    
    pinata_response = pin_file_to_pinata(filepath, 'report.json')
    if "IpfsHash" in pinata_response:
        return jsonify({"message": "Report uploaded successfully", "IpfsHash": pinata_response["IpfsHash"]}), 200
    else:
        return jsonify({"error": "Failed to upload report"}), 500

@pinata_routes.route('/list-pinned-files', methods=['GET'])
def list_pinned_files():
    return jsonify(list_pinned_files_from_pinata()), 200

@pinata_routes.route('/unpin-file/<ipfs_hash>', methods=['DELETE'])
def unpin_file(ipfs_hash):
    response = unpin_file_from_pinata(ipfs_hash)
    return jsonify(response), 200 if response.get('message') else 500
