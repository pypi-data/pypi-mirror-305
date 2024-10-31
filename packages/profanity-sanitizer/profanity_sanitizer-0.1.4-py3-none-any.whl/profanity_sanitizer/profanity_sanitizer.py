import os
import re
from typing import List, Optional, Dict, Union

from .ai_model_handler import AIModelHandler
from .data_loader import DataLoader
from .fuzzy_matcher import FuzzyMatcher
from .models.profanity_result import ProfanityResult
from .semantic_similarity_checker import SemanticSimilarityChecker


class ProfanitySanitizer:
    """
    A class for filtering profanity and toxic content from text.

    This class provides methods to check text against banned words,
    perform fuzzy matching, semantic similarity checks, and AI-based toxicity detection.
    """

    def __init__(
        self,
        banned_words_file: str = None,
        allowed_words_file: str = None,
        replacements_file: str = None,
        removals_pattern: Optional[str] = None,
        use_fuzzy: bool = True,
        fuzzy_threshold: int = 80,
        use_ai: bool = True,
        model_name: str = "unitary/toxic-bert",
        use_semantic: bool = True,
        similarity_threshold: float = 0.8,
        toxicity_threshold: float = 0.5,
        min_problematic_score_threshold: int = 65,
    ) -> None:
        """
        Initialize the ProfanityFilter with various configuration options.

        Args:
            banned_words_file (str): Path to JSON file containing banned words.
            allowed_words_file (str): Path to JSON file containing allowed words.
            replacements_file (str): Path to JSON file containing character replacements.
            removals_pattern (str): Regex pattern for characters to remove.
            use_fuzzy (bool): Whether to use fuzzy matching.
            fuzzy_threshold (int): Threshold for fuzzy matching.
            use_ai (bool): Whether to use AI-based toxicity detection.
            model_name (str): Name of the AI model to use.
            use_semantic (bool): Whether to use semantic similarity checks.
            similarity_threshold (float): Threshold for semantic similarity.
            toxicity_threshold (float): Threshold for AI-based toxicity detection.
            min_problematic_score_threshold (int): Minimum score to consider text problematic.
        """

        data_dir = os.path.join(os.path.dirname(__file__), "data")
        # Set default paths relative to the data directory
        banned_words_file = banned_words_file or os.path.join(
            data_dir, "banned_words.json"
        )
        allowed_words_file = allowed_words_file or os.path.join(
            data_dir, "allowed_words.json"
        )
        replacements_file = replacements_file or os.path.join(
            data_dir, "replacements.json"
        )

        # Load data
        self.banned_words: List[str] = DataLoader.load_json(banned_words_file)
        self.allowed_words: List[str] = DataLoader.load_json(allowed_words_file)
        self.replacements: Dict[str, str] = DataLoader.load_json(replacements_file)

        # Compile regex patterns
        self.removals_pattern: str = removals_pattern or r"[^a-z\s]"
        self.removals_regex: re.Pattern = re.compile(self.removals_pattern)

        # Thresholds and settings
        self.toxicity_threshold: float = toxicity_threshold
        self.use_fuzzy: bool = use_fuzzy
        self.fuzzy_threshold: int = fuzzy_threshold
        self.use_ai: bool = use_ai
        self.use_semantic: bool = use_semantic
        self.similarity_threshold: float = similarity_threshold
        self.min_problematic_score_threshold: int = min_problematic_score_threshold

        # Initialize handlers
        self.ai_handler: Optional[AIModelHandler] = (
            AIModelHandler(model_name) if use_ai else None
        )
        self.semantic_checker: Optional[SemanticSimilarityChecker] = (
            SemanticSimilarityChecker() if use_semantic else None
        )

    @staticmethod
    def contains_banned_word(word: str, text: str) -> bool:
        """
        Check if the text contains a banned word.

        Args:
            word (str): The banned word to check for.
            text (str): The text to check.

        Returns:
            bool: True if the text contains the banned word, False otherwise.
        """
        return word.lower() in text.lower()

    def normalize(self, text: str) -> str:
        """
        Normalize the input string by applying replacements and removals.

        Args:
            text (str): The input string to normalize.

        Returns:
            str: The normalized string.
        """
        text = text.lower()
        for old_char, new_char in self.replacements.items():
            text = text.replace(old_char, new_char)
        text = self.removals_regex.sub("", text)
        return text

    def check_text(self, text: str) -> ProfanityResult:
        """
        Check the input text for profanity and toxicity.

        Args:
            text (str): The input text to check.

        Returns:
            ProfanityResult: The result of the profanity check.
        """
        if self.is_allowed_word(text):
            return ProfanityResult(
                result=f"Text '{text}' is in the allowed words list.",
                reason="allowed_word",
                is_clean=True,
                problematic_score=0,
            )

        normalized_text: str = self.normalize(text)
        results: List[ProfanityResult] = self.check_against_banned_words(
            text, normalized_text
        )

        if self.use_ai:
            ai_result: Optional[ProfanityResult] = self.check_ai_toxicity(
                normalized_text
            )
            if ai_result:
                results.append(ai_result)

        return self.decide_result(results, text)

    def is_allowed_word(self, text: str) -> bool:
        """
        Check if the text is an allowed word.

        Args:
            text (str): The text to check.

        Returns:
            bool: True if the text is an allowed word, False otherwise.
        """
        return self.allowed_words and text.lower() in self.allowed_words

    def check_against_banned_words(
        self, original_text: str, normalized_text: str
    ) -> List[ProfanityResult]:
        """
        Check the input text against the list of banned words.

        Args:
            original_text (str): The original input text.
            normalized_text (str): The normalized input text.

        Returns:
            List[ProfanityResult]: A list of ProfanityResult objects for matched banned words.
        """
        results: List[ProfanityResult] = []
        for banned_word in self.banned_words:
            normalized_banned_word: str = self.normalize(banned_word)

            exact_match: bool = self.contains_banned_word(
                normalized_banned_word, normalized_text
            )
            fuzzy_score: Union[int, float] = (
                FuzzyMatcher.get_fuzzy_score(normalized_banned_word, normalized_text)
                if self.use_fuzzy
                else 0
            )
            semantic_score: float = (
                self.semantic_checker.check_similarity(banned_word, original_text)
                if self.use_semantic and self.semantic_checker
                else 0.0
            )
            ai_score: float = (
                self.ai_handler.contains_toxicity(normalized_text)
                if self.use_ai and self.ai_handler
                else 0.0
            )

            if self.should_flag_word(exact_match, fuzzy_score, semantic_score):
                problematic_score: int = self.calculate_problematic_score(
                    exact_match, fuzzy_score, semantic_score, ai_score
                )
                results.append(
                    ProfanityResult(
                        result=f"Text '{original_text}' matches or is similar to a banned word or phrase.",
                        reason="banned_word",
                        is_clean=False,
                        problematic_score=problematic_score,
                    )
                )
        return results

    def check_ai_toxicity(self, text: str) -> Optional[ProfanityResult]:
        """
        Check the text for toxicity using AI-based detection.

        Args:
            text (str): The text to check.

        Returns:
            Optional[ProfanityResult]: A ProfanityResult if toxicity is detected, None otherwise.
        """
        if not self.ai_handler:
            return None
        ai_score: float = self.ai_handler.contains_toxicity(text)
        if ai_score > self.toxicity_threshold:
            ai_problematic_score: int = int(ai_score * 100)
            return ProfanityResult(
                result=f"Text '{text}' contains toxic content.",
                reason="toxicity",
                is_clean=False,
                problematic_score=ai_problematic_score,
            )
        return None

    def decide_result(
        self, results: List[ProfanityResult], text: str
    ) -> ProfanityResult:
        """
        Decide the final result based on all checks performed.

        Args:
            results (List[ProfanityResult]): List of individual check results.
            text (str): The original input text.

        Returns:
            ProfanityResult: The final decision result
        """
        if not results:
            return ProfanityResult(
                result=f"Text '{text}' is clean.",
                reason=None,
                is_clean=True,
                problematic_score=0,
            )

        # Sort results by problematic_score, highest first
        sorted_results: List[ProfanityResult] = sorted(
            results, key=lambda x: x.problematic_score, reverse=True
        )

        # If we have multiple results, adjust the problematic_score
        if len(sorted_results) > 1:
            highest_score: int = sorted_results[0].problematic_score
            second_highest_score: int = sorted_results[1].problematic_score

            # If the top two problematic_scores are close, reduce the overall problematic_score
            if highest_score - second_highest_score < 20:
                average_score: int = (highest_score + second_highest_score) // 2
                sorted_results[0].problematic_score = average_score

        if sorted_results[0].problematic_score < self.min_problematic_score_threshold:
            return ProfanityResult(
                result=f"Text '{text}' is likely clean, but flagged with low problematic score.",
                reason="low_problematic_score",
                is_clean=True,
                problematic_score=max(100 - sorted_results[0].problematic_score, 50),
            )

        return sorted_results[0]

    def should_flag_word(
        self, exact_match: bool, fuzzy_score: Union[int, float], semantic_score: float
    ) -> bool:
        """
        Determine if a word should be flagged based on matching criteria.

        Args:
            exact_match (bool): Whether there's an exact match.
            fuzzy_score (Union[int, float]): The fuzzy matching score.
            semantic_score (float): The semantic similarity score.

        Returns:
            bool: True if the word should be flagged, False otherwise.
        """
        return (
            exact_match
            or (self.use_fuzzy and fuzzy_score > self.fuzzy_threshold)
            or (self.use_semantic and semantic_score > self.similarity_threshold)
        )

    def calculate_problematic_score(
        self,
        exact_match: bool,
        fuzzy_score: Union[int, float],
        semantic_score: float,
        ai_score: float,
    ) -> int:
        """
        Calculate the problematic score based on various matching criteria.

        Args:
            exact_match (bool): Whether there's an exact match.
            fuzzy_score (Union[int, float]): The fuzzy matching score.
            semantic_score (float): The semantic similarity score.
            ai_score (float): The AI-based toxicity score.

        Returns:
            int: The calculated problematic score.
        """
        if exact_match:
            base_score: int = 100
        else:
            fuzzy_problematic_score: Union[int, float] = (
                fuzzy_score if self.use_fuzzy else 0
            )
            semantic_problematic_score: float = (
                semantic_score * 100 if self.use_semantic else 0
            )

            if self.use_fuzzy and self.use_semantic:
                discrepancy: float = abs(
                    fuzzy_problematic_score - semantic_problematic_score
                )
                max_discrepancy: int = 100
                semantic_weight: float = 1 - (discrepancy / max_discrepancy)
                base_score = int(fuzzy_problematic_score * semantic_weight)
            elif self.use_fuzzy:
                base_score = int(fuzzy_problematic_score)
            elif self.use_semantic:
                base_score = int(semantic_problematic_score)
            else:
                base_score = 0

        if self.use_ai and ai_score > 0:
            ai_factor: float = ai_score / self.toxicity_threshold
            adjusted_score: float = base_score * ai_factor
        else:
            adjusted_score: float = base_score

        return min(max(int(adjusted_score), 0), 100)
