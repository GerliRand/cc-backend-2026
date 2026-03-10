from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Read pickle file (using Module 2 model)
with open("sentiment_analysis_model.pkl", "rb") as file:
    data = pickle.load(file)

# Checking that the backend server is running
@app.route("/")
def home():
    return jsonify({
        "message": "Backend is running..."
    })
   
# api endpoint
@app.route("/api", methods=["POST"])
def sentiment():
    body = request.get_json()

    # Checking that it is the correct format
    if not body:
        return jsonify({
            "error": "Request body must be JSON format "
        }), 400

    # Checking that the text field exists
    if "text" not in body:
        return jsonify({
            "error": "Missing text field"
        }), 400
    
    # Extract the text sent from the frontend
    text = body["text"]

    # Checking that the text is not empty
    if text == "":
        return jsonify({
            "error": "Text field is empty"
        })
    
    # Using the trained model to predict the sentiment of the text
    prediction = data.predict([text])[0]
    
    # Return the original text and the predicted sentiment as JSON
    return jsonify({
        "text": text,
        "prediction": prediction
    })