"""Test the emotion detector's ability to identify emotions."""

# ruff: noqa: ANN201, PT009
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit test cases for emotion detector."""

    def _return_dominant_emotion(self, text: str) -> str:
        return emotion_detector(text)["dominant_emotion"]  # pyright: ignore[reportReturnType]

    def test_emotion_detector_returns_joy_appropriately(self):
        """Test that emotion_detector returns joy for positive statements."""
        text = "I am glad this happened"
        self.assertEqual(self._return_dominant_emotion(text), "joy")

    def test_emotion_detector_returns_anger_appropriately(self):
        """Test that emotion_detector returns anger for negative statements."""
        text = "I am really mad about this"
        self.assertEqual(self._return_dominant_emotion(text), "anger")

    def test_emotion_detector_returns_disgust_appropriately(self):
        """Test that emotion_detector returns disgust for disgusting statements."""
        text = "I feel disgusted just hearing about this"
        self.assertEqual(self._return_dominant_emotion(text), "disgust")

    def test_emotion_detector_returns_sad_appropriately(self):
        """Test that emotion_detector returns sadness for sad statements."""
        text = "I am so sad about this"
        self.assertEqual(self._return_dominant_emotion(text), "sadness")

    def test_emotion_detector_returns_fear_appropriately(self):
        """Test that emotion_detector returns fear for fearful statements."""
        text = "I am really afraid that this will happen."
        self.assertEqual(self._return_dominant_emotion(text), "fear")


if __name__ == "__main__":
    unittest.main()
