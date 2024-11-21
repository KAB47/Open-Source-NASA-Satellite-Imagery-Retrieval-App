"""
Satellite Image Retrieval Flask App

This Flask application provides an interface to fetch satellite imagery using the Earth API. 
Users can query the app by providing latitude, longitude, and date parameters.

Modules:
    - flask: To handle web requests and responses.
    - requests: To make HTTP requests to the Earth API.

Routes:
    1. `/` (GET):
        - Displays the homepage (index.html).
    2. `/v5000/earth/imagery/` (GET):
        - Fetches satellite images for given latitude, longitude, and date.

Global Variables:
    - EARTH_API_URL: URL of the Earth API endpoint for retrieving assets.

How it Works:
    - Users send a GET request to `/v5000/earth/imagery/` with query parameters:
        - `lat`: Latitude of the location.
        - `lon`: Longitude of the location.
        - `date`: Date for the satellite image (default: '2024-09-24').
    - The app forwards these parameters to the Earth API to retrieve the image.

Error Handling:
    - Returns a 500 error if the Earth API response fails.

Example Usage:
    GET /v5000/earth/imagery/?lat=29.67&lon=-95.21&date=2017-09-24
"""
from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Earth API endpoint
EARTH_API_URL = "http://127.0.0.1:5000/v5000/earth/assets/"

@app.route('/')
def home():
    """
    Render the homepage.

    Returns:
        HTML template for the homepage.
    """
    return render_template('index.html')

@app.route('/v5000/earth/imagery/', methods=['GET'])
def get_satellite_image():
    """
    Fetch satellite image URL for the given latitude, longitude, and date.

    Query Parameters:
        - lat (float): Latitude of the location.
        - lon (float): Longitude of the location.
        - date (str): Date for the image (default: '2024-09-24').

    Returns:
        JSON response with the image URL or an error message.
    """
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    date = request.args.get('date', '2024-09-24')

    # Forward request to the Earth API
    response = requests.get(EARTH_API_URL, params={'lat': lat, 'lon': lon, 'date': date})
    print(response.status_code, response.text)

    if response.status_code == 200:
        return jsonify({'image_url': response.json().get('url')})
    else:
        return jsonify({'error': 'Unable to fetch image'}), 500

if __name__ == '__main__':
    app.run(debug=True)