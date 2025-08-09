"""Module for emotion detection using WATSON NLP. Assume WATSON is pre-configured."""

import requests


def emotion_detector(text_to_analyze: str) -> str | None:
    """Detect emotions in a given text using WATSON NLP Emotion Predict function.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        str: text attribute of response from the WATSON NLP Emotion Predict function

    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=input_json, timeout=60)
    if response.status_code != requests.codes.ok:
        return None
    return response.text
