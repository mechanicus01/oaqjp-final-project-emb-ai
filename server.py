from flask import Flask, jsonify, request, make_response, render_template
from EmotionDetection.emotion_detection import emotion_detector

server = Flask(__name__)

@server.route('/')
def render_index_page():
    return render_template('index.html')

@server.route('/emotionDetector')
def emotion_detect():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is '{response['dominant_emotion']}': {response['joy']},  "
        f"'anger' {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

# Run the app
if __name__ == "__main__":
    server.run(debug=True)