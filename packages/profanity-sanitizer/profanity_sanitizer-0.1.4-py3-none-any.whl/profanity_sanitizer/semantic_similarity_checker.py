import spacy
from spacy.language import Language
from spacy.tokens import Doc


class SemanticSimilarityChecker:
    """Class responsible for checking semantic similarity using spaCy."""

    def __init__(self) -> None:
        self.nlp: Language = spacy.load("en_core_web_lg")

    def check_similarity(self, text1: str, text2: str) -> float:
        """
        Check the semantic similarity between two texts.

        Args:
            text1 (str): The first text.
            text2 (str): The second text.

        Returns:
            float: The semantic similarity score.
        """
        if not text1.strip() or not text2.strip():
            return 0.0

        doc1: Doc = self.nlp(text1)
        doc2: Doc = self.nlp(text2)

        if doc1.vector_norm and doc2.vector_norm:
            return doc1.similarity(doc2)
        else:
            return 0.0
