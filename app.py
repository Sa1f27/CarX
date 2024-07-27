from flask import Flask, render_template, request, jsonify
import pytesseract
import speech_recognition as sr

app = Flask(__name__)

# Configure Tesseract
pytesseract.pytesseract.tesseract_cmd = r'path_to_your_tesseract_executable'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictive-maintenance', methods=['POST'])
def predictive_maintenance():
    daily_usage = request.form['daily_usage']
    last_maintenance = request.form['last_maintenance']
    fuel_usage = request.form['fuel_usage']
    prediction = "Next maintenance in 10 days"  # Placeholder
    return jsonify({"prediction": prediction})

@app.route('/customer-inquiries', methods=['POST'])
def customer_inquiries():
    question = request.form['question']
    answer = "Your vehicle is in good condition."  # Placeholder
    return jsonify({"answer": answer})

@app.route('/best-match', methods=['POST'])
def best_match():
    location = request.form['location']
    best_towing_service = "Towing Service A"  # Placeholder
    return jsonify({"best_towing_service": best_towing_service})

@app.route('/3d-car-models', methods=['POST'])
def car_models():
    video_file = request.files['video']
    # Process the video file (placeholder)
    return jsonify({"status": "3D model created successfully"})

@app.route('/ai-chat-interface', methods=['POST'])
def ai_chat():
    message = request.form['message']
    response = "Your car is being repaired."  # Placeholder
    return jsonify({"response": response})

@app.route('/insurance-info-extraction', methods=['POST'])
def insurance_info_extraction():
    image_file = request.files['image']
    text = pytesseract.image_to_string(image_file)
    extracted_info = "Policy Number: 123456"  # Placeholder
    return jsonify({"extracted_info": extracted_info})

@app.route('/inventory-management', methods=['POST'])
def inventory_management():
    audio_file = request.files['audio']
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    inventory_update = "Inventory updated successfully"
    return jsonify({"inventory_update": inventory_update})

if __name__ == '__main__':
    app.run(debug=True)
