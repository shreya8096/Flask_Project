from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage to simulate database
data_storage = {}

# Mock data for demonstration purposes
mock_data = {
    "id": 1,
    "name": "Test Product",
    "description": "This is a mock product description",
    "price": 29.99,
    "category": "Electronics"
}

# API Endpoint for Data Retrieval
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    return jsonify(mock_data)

# Data Processing Function
@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.json
    # Example transformation: convert product name to uppercase
    processed_data = {
        "id": data['id'],
        "name": data['name'].upper(),
        "description": data['description'],
        "price": data['price'],
        "category": data['category']
    }
    # Store processed data in memory
    data_storage[data['id']] = processed_data
    return jsonify({"message": "Data processed and stored successfully"}), 201

# API Endpoint to Retrieve Processed Data
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    return jsonify(data_storage)

if __name__ == '__main__':
    app.run(debug=True)
