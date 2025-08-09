"""Flask server for emotion detection."""

from flask import Flask, abort, render_template, request

from .EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def detect_emotions() -> str:
    """Detect emotions from the provided text.

    Returns:
        str: The detected emotions and the dominant emotion.

    """
    text = request.args.get("textToAnalyze", "")
    if not text.strip():
        abort(400, "No text provided")

    result = emotion_detector(text)
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is "
        f"<b>{result['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page() -> str:
    """Render the main application page.

    Initiate the rendering of the main application page over the Flask channel.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 5000)
