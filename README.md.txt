# Flask Data Retrieval and Processing Application

## Overview

This project is a Flask-based web application that simulates a simplified version of a data retrieval and processing system. The application provides endpoints to fetch mock data, process it, store the processed data in temporary in-memory storage, and retrieve the processed data.

## Features
1. **API Endpoint for Data Retrieval:**
**Endpoint:** /fetch-data
**Description:** Simulates fetching data from an external service using mock data.
**Method:** GET

2. **Data Processing:**
**Endpoint:** /process-data
**Description:** Processes the fetched data by performing a simple transformation (e.g., converting text to uppercase) and stores it in in-memory storage.
**Method:** POST
Expected Input: JSON data (e.g., product details).

3. Data Storage:
**Description:** Stores the processed data in a Python dictionary (in-memory storage).

4. API Endpoint to Retrieve Processed Data:
**Endpoint:** /get-processed-data
**Description:** Retrieves the processed data stored in in-memory storage.
**Method:** GET

## Prerequisites
Python 3.x: Ensure Python is installed on your machine.
pip: Python package installer, usually bundled with Python.

## Setup Instructions

1. **Clone the Repository or Download the ZIP**
If using Git:
git clone <repository-url>
cd flask_project

Or download the ZIP file from the provided link and extract it.

2. **Create a Virtual Environment**
python -m venv venv

3. **Activate the Virtual Environment**
**For Windows:**
venv\Scripts\activate

**For Linux/MacOS:**
source venv/bin/activate

4. **Install Dependencies**
pip install -r requirements.txt

5. **Run the Flask Application**
python app.py

6. **Access the Application**
The application will run on http://127.0.0.1:5000/.
You can test different endpoints using a web browser, Postman, or cURL.

## API Endpoints
1. **/fetch-data**
**Method:** GET
**Description:** Fetches mock data.

URL: http://127.0.0.1:5000/fetch-data
Response:
{
    "id": 1,
    "name": "Test Product",
    "description": "This is a mock product description",
    "price": 29.99,
    "category": "Electronics"
}

2. **/process-data**
**Method:** POST
**Description:** Processes the provided JSON data and stores the processed data in memory.

**Input Example:**
{
    "id": 2,
    "name": "Sample Product",
    "description": "This is another mock product description",
    "price": 49.99,
    "category": "Books"
}

Example with Postman:
Set the method to POST.
URL: http://127.0.0.1:5000/process-data
In the Body tab, select raw and JSON, then input the data.
Click Send to process and store the data.

3. **/get-processed-data**
**Method:** GET
**Description:** Retrieves all processed data stored in memory.
**Example:**
URL: http://127.0.0.1:5000/get-processed-data
Response:
json
Copy code
{
    "2": {
        "id": 2,
        "name": "SAMPLE PRODUCT",
        "description": "This is another mock product description",
        "price": 49.99,
        "category": "Books"
    }
}

## Testing
Testing with Postman

1. Fetch Data:
Send a GET request to **http://127.0.0.1:5000/fetch-data**.

2. Process Data:
Send a POST request to **http://127.0.0.1:5000/process-data** with JSON data in the body.

3. Get Processed Data:
Send a GET request to **http://127.0.0.1:5000/get-processed-data**.

## Testing with cURL

1. Fetch Data:
curl http://127.0.0.1:5000/fetch-data

2. Process Data:
curl -X POST http://127.0.0.1:5000/process-data -H "Content-Type: application/json" -d "{\"id\": 2, \"name\": \"Sample Product\", \"description\": \"This is another mock product description\", \"price\": 49.99, \"category\": \"Books\"}"

3. Get Processed Data:
curl http://127.0.0.1:5000/get-processed-data

## Additional Notes
Ensure that the virtual environment is activated when running the Flask app.
The application uses in-memory storage, meaning all stored data will be lost when the server is restarted.