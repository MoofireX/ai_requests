import base64
from google import generativeai as genai
from flask import Flask, jsonify, request

genai.configure(api_key="AIzaSyBrl1diAZs34jZ1H5YlVvMMXSsNq1cnFDU")
model = genai.GenerativeModel("gemini-pro-vision")

app = Flask(__name__)

@app.route("/genai", methods=["POST"])
def gemini(requests):
    try:
        data = request.get_json()
        prompt = data.get('prompt')
        image = data.get('image')

        if not prompt or not image:
            return jsonify({"Error": "Missing prompt or imag"}), 400 

        response = model.generate_content([
            prompt,
            {
                "inline_data" : {
                    "mime_type" : "image/png",
                    "data" : image
                }
            }
        ])

        return jsonify({"response": response.text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/")
def index():
    return "Gemini API is running!"

if __name__ == "__main__":
    app.run()
