<h1 align="center">
  Swimmer Detection Using YOLO Algorithm
  <br>
</h1>

<h4 align="center">Swimmer detection application implemented in Python using the <a href="https://github.com/ultralytics/yolov5">YOLO algorithm</a>. The application includes a frontend served with a simple HTTP server and a <a href="https://flask.palletsprojects.com/en/3.0.x/">Flask server</a> that utilizes the model to detect swimmers in images or videos.</h4>

<p align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnQ5MjlvbXBrNnl1amV3ZGRma3M0N2h2MmJ0dGxveDlpN2oyYjkyZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5yfZXty3v88Id2SxSh/giphy.gif" alt="swimmer detection" />
</p>

<div align="center">
  <h3>
    <a href="https://mega.nz/file/gMpWQIxA#vcRiKPtP-S_pg3x3t9BEfE-P3o7KWTINwg8y6b7rjxA">
      Seminar Work
    </a>
</h3>
</div>

## Features

- **YOLO Algorithm**: Utilizes the YOLO (You Only Look Once) algorithm for real-time object detection, specifically trained to detect swimmers.
- **Interactive Frontend**: The frontend interface allows users to upload images or videos and view the detection results in real-time.
- **Flask Server**: A Flask server processes the uploaded media and applies the YOLO model to detect swimmers, providing results back to the frontend.
- **Simple HTTP Server**: The application frontend is served using a simple HTTP server command for easy setup and access.
- **Efficient Detection**: The model is optimized for high accuracy and performance, making it suitable for real-time detection scenarios.

## Requirements

- Python 3.x
- Flask Library
- YOLO Model Files

## How To Use

Clone this repository
```bash
$ git clone https://github.com/DBDoco/yolo-swimmer-detection.git
```

Install required libraries
```bash
$ pip install -r requirements.txt
```

Start the Flask server
```bash
$ python flask_server.py
```

Start the frontend server
```bash
$ python -m http.server
```

Access the application by navigating to http://localhost:8000 in your web browser.
After that you can upload images and videos through the UI. Processed images or videos will be saved to the 'processed' folder.

