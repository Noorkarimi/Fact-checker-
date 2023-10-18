from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined trusted sources (simplified)
TRUSTED_SOURCES = {
    "The earth is round": True,
    "The moon is made of cheese": False
}

@app.route('/fact_check', methods=['POST'])
def fact_check():
    claim = request.json.get('claim')
    verification_result = TRUSTED_SOURCES.get(claim, "Claim not found in trusted sources")
    return jsonify({"result": verification_result})

if __name__ == '__main__':
    app.run(debug=True)
