from flask import Flask, request, render_template, jsonify
import os
from ocr import extract_text_from_pdf, extract_financial_details
from chatbot import get_ai_response

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    """Handles PDF upload and extracts financial details."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded!"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    extracted_text = extract_text_from_pdf(file_path)
    tax_details = extract_financial_details(extracted_text)

    return jsonify(tax_details)

@app.route("/chat", methods=["POST"])
def chat():
    """Handles AI-powered tax queries."""
    data = request.json
    query = data.get("query", "")
    response = get_ai_response(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
