from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app, resources={
    r"/spam_detector": {
        "origins": "https://alejandrobermea.com",
        "supports_credentials": True
    },
    r"/live_spam_words": {
        "origins": "https://alejandrobermea.com",
        "supports_credentials": True
    }
})

model = joblib.load('spam_detector.pkl')
feature_extraction = joblib.load('feature_extraction.pkl')
spam_words = joblib.load('spam_indicative_words.pkl')

@app.route('/')
def home():
    return jsonify({"message": "Spam detection service is running"}), 200

@app.route('/live_spam_words', methods=['POST'])
@cross_origin(origin='https://alejandrobermea.com', supports_credentials=True)
def live_spam_words():
    data = request.get_json()
    email_text = data['text'].lower()
    input_words = set(email_text.split())
    common_spam_words = sorted(
        ((word, spam_words[word]) for word in input_words if word in spam_words),
        key=lambda x: x[1]
    )
    return jsonify({"common_spam_words": common_spam_words}), 200

@app.route('/spam_detector', methods=['POST', 'OPTIONS'])
@cross_origin(origin='https://alejandrobermea.com', supports_credentials=True)
def analyze_email():
    if request.method == 'OPTIONS':
        return jsonify(), 200
    try:
        data = request.get_json()
        email_text = data['text'].lower()
        email_features = feature_extraction.transform([email_text])
        prediction = model.predict(email_features)
        result = "This is spam email" if prediction[0] == 1 else "This isn't spam email"
        return jsonify({"result": result}), 200
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred processing the email text"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
