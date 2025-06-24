from flask import Blueprint, request, jsonify
from services.explanation_service import explain_result

explanation_routes = Blueprint('explanation_routes', __name__)

@explanation_routes.route('/explain', methods=['POST'])
def explain():
    try:
        # Get input from the request
        data = request.json
        model_name = data.get('model_name')
        input_data = data.get('input_data')
        result = data.get('result')

        # Generate explanation
        explanation = explain_result(model_name, input_data, result)

        # Return the explanation
        return jsonify({"explanation": explanation}), 200
    except Exception as e:
        print(f"Error in /explain route: {e}")
        return jsonify({"error": str(e)}), 500
