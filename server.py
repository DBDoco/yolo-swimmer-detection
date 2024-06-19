from flask import Flask, request, send_from_directory, jsonify
import os
import torch
import cv2
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./models/exp5/weights/best.pt')

def process_image(image_path, output_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = model(img_rgb)
    results_img = results.render()[0]  
    results_img_bgr = cv2.cvtColor(results_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, results_img_bgr)

def process_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model(img_rgb)
        results_img = results.render()[0]
        results_img_bgr = cv2.cvtColor(results_img, cv2.COLOR_RGB2BGR)
        
        if out is None:
            out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (frame.shape[1], frame.shape[0]))
        
        out.write(results_img_bgr)

    cap.release()
    out.release()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        output_path = os.path.join(app.config['PROCESSED_FOLDER'], 'output_' + file.filename)
        if file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            process_image(file_path, output_path)
        elif file.filename.lower().endswith(('.mp4', '.avi', '.mov')):
            process_video(file_path, output_path)
        else:
            return jsonify({"error": "Unsupported file format"}), 400
        return jsonify({"filename": 'output_' + file.filename}), 200

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
