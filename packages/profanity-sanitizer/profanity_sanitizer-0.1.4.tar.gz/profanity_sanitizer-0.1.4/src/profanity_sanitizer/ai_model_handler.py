from transformers import pipeline


class AIModelHandler:
    """Class responsible for handling the AI model for toxicity detection."""

    def __init__(self, model_name: str) -> None:
        self.model: pipeline = pipeline("text-classification", model=model_name)

    def contains_toxicity(self, text: str) -> float:
        """
        Check if the text contains toxic content using AI-based detection.

        Args:
            text (str): The text to check for toxicity.

        Returns:
            float: The toxicity score if toxic content is detected, otherwise 0.0.
        """
        result = self.model(text)
        for res in result:
            if res["label"].upper() in ["TOXIC", "INSULT", "THREAT"]:
                return res["score"]
        return 0.0
