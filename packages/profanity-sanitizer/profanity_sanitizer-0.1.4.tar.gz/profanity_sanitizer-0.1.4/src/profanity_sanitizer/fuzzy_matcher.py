from typing import Union

from fuzzywuzzy import fuzz


class FuzzyMatcher:
    """Class responsible for performing fuzzy matching."""

    @staticmethod
    def get_fuzzy_score(word: str, text: str) -> Union[int, float]:
        """
        Perform fuzzy matching between a word and text.

        Args:
            word (str): The word to match.
            text (str): The text to match against.

        Returns:
            Union[int, float]: The fuzzy matching score.
        """
        return fuzz.partial_ratio(word, text)
