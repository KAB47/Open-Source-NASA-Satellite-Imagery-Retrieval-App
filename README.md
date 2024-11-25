# Open-Source-Satellite-Imagery-Retrieval-App
An (In progress) Flask-based web application that fetches satellite imagery from Landsat using the Earth API. Users can input latitude, longitude, and date to retrieve high-quality Earth images.

# Satellite Imagery Flask App

This project provides a Flask-based web application to fetch satellite imagery using an Earth API. It integrates with Google Earth Engine to retrieve Landsat 8 satellite images.

## Roadblock
- I am trying get the flask app (app.py) to fetch the satellite image from the 'earth_api' app but have not been successful.
- What I have tried:

- Changing the app route
- Fully defining the parameters
- Reassessing and changing the 'EARTH_API_URL' and 'app.py' endpoints.

- If you have any contributions to make, feel free!

## Features
- **User Interface**: Home page for interacting with the application.
- **REST API**: Endpoint to fetch satellite imagery based on geographic coordinates, date, and other parameters.

## Architecture
1. **Main Flask App**:
   - Serves as the front-end and proxy to the Earth API.
   - Endpoint: `/v5000/earth/imagery/`
2. **Earth API**:
   - Handles communication with Google Earth Engine.
   - Processes and serves satellite images.

## Endpoints
### Main App
- **GET** `/v5000/earth/imagery/`
  - **Parameters**:
    - `lat`: Latitude (required).
    - `lon`: Longitude (required).
    - `date`: Date (default: `2024-09-24`).
  - **Response**:
    - JSON with the URL of the satellite image.

### Earth API
- **GET** `/v5000/earth/imagery/`
  - Fetches and processes satellite images directly from Google Earth Engine.

## Requirements
- **Python**: 3.7+
- **Libraries**:
  - Flask
  - Flask-CORS
  - Requests
  - PIL (Pillow)
  - Google Earth Engine (`ee`)

## Extra
The 'earth_api' is apart of an open-source NASA project. You can find the repo it is contained in here: https://github.com/nasa/earth-imagery-api/blob/main/flaskproject/app.py
There is an index.html page located in the 'templates' folder and acts as a front end to the backend 'app.py' file.
