import os
import unittest

from src.profanity_sanitizer.fuzzy_matcher import FuzzyMatcher
from src.profanity_sanitizer.models.profanity_result import ProfanityResult
from src.profanity_sanitizer.profanity_sanitizer import ProfanitySanitizer


class TestProfanitySanitizer(unittest.TestCase):
    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full paths to the JSON files
        banned_words_file = os.path.join(current_dir, "test_banned_words.json")
        allowed_words_file = os.path.join(current_dir, "test_allowed_words.json")
        replacements_file = os.path.join(current_dir, "test_replacements.json")

        # Initialize the ProfanityFilter with the correct file paths
        self.sanitizer = ProfanitySanitizer(
            banned_words_file=banned_words_file,
            allowed_words_file=allowed_words_file,
            replacements_file=replacements_file,
            use_fuzzy=True,
            use_semantic=True,
            use_ai=True,
        )

    def test_initialization(self):
        # Test that the ProfanityFilter is initialized correctly
        self.assertIsInstance(self.sanitizer, ProfanitySanitizer)
        self.assertTrue(self.sanitizer.use_fuzzy)
        self.assertTrue(self.sanitizer.use_semantic)
        self.assertTrue(self.sanitizer.use_ai)

    def test_normalize(self):
        # Test the normalize method with actual swear words and slurs
        self.assertEqual(self.sanitizer.normalize("F*ck"), "fck")
        self.assertEqual(self.sanitizer.normalize("Sh!t"), "shit")
        self.assertEqual(self.sanitizer.normalize("B!tch"), "bitch")
        self.assertEqual(self.sanitizer.normalize("@$$h0l3"), "asshole")
        self.assertEqual(self.sanitizer.normalize("N1663r"), "nigger")
        self.assertEqual(self.sanitizer.normalize("R3t@rd"), "retard")
        self.assertEqual(self.sanitizer.normalize("F@gg0t"), "faggot")
        self.assertEqual(self.sanitizer.normalize("Wh0r3"), "whore")
        self.assertEqual(self.sanitizer.normalize("C*nt"), "cnt")
        self.assertEqual(self.sanitizer.normalize("D!ck"), "dick")

    def test_contains_banned_word(self):
        # Test the contains_banned_word method
        self.assertTrue(
            self.sanitizer.contains_banned_word("bad", "this is a bad word")
        )
        self.assertFalse(
            self.sanitizer.contains_banned_word("good", "this is a bad word")
        )

        # Test with actual banned words from test_banned_words.json
        self.assertTrue(
            self.sanitizer.contains_banned_word("nigger", "the nigger is offensive")
        )
        self.assertTrue(
            self.sanitizer.contains_banned_word("faggot", "that faggot is hurtful")
        )
        self.assertTrue(
            self.sanitizer.contains_banned_word("kike", "kike is an antisemitic slur")
        )
        self.assertTrue(
            self.sanitizer.contains_banned_word("cunt", "the cunt is vulgar")
        )

        # Test with partial matches (should return True)
        self.assertTrue(
            self.sanitizer.contains_banned_word("nig", "night time is dark")
        )
        self.assertTrue(
            self.sanitizer.contains_banned_word("fag", "fagotto is an instrument")
        )

        # Test with uppercase variations
        self.assertTrue(
            self.sanitizer.contains_banned_word("NIGGER", "THE NIGGER IS OFFENSIVE")
        )
        self.assertTrue(
            self.sanitizer.contains_banned_word("FaGgOt", "ThAt FaGgOt iS hUrTfUl")
        )

        # Test with surrounding punctuation
        self.assertTrue(self.sanitizer.contains_banned_word("cunt", "you're a (cunt)!"))
        self.assertTrue(
            self.sanitizer.contains_banned_word(
                "kike", "anti-semites use 'kike' as a slur"
            )
        )

        # Test with non-matching words
        self.assertFalse(self.sanitizer.contains_banned_word("book", "I love reading"))
        self.assertFalse(self.sanitizer.contains_banned_word("hello", "Hi there!"))

        # Test with words that are substrings of other words
        self.assertTrue(self.sanitizer.contains_banned_word("ass", "I'm passing by"))
        self.assertTrue(
            self.sanitizer.contains_banned_word("cum", "I'm accumulating points")
        )

    def test_fuzzy_match(self):
        # Test the FuzzyMatcher class
        # Test the get_fuzzy_score method with actual banned words and text
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("nigger", "n1gg3r"), 65)
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("faggot", "f@gg0t"), 65)
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("cunt", "kunt"), 75)
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("kike", "k1k3"), 50)
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("asshole", "@ssh0le"), 65)
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("bitch", "b!tch"), 75)
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("fuck", "fvck"), 75)
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("shit", "sh1t"), 75)
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("whore", "wh0r3"), 60)
        self.assertGreaterEqual(FuzzyMatcher.get_fuzzy_score("dick", "d!ck"), 75)

        # Test with unexpected inputs
        self.assertEqual(FuzzyMatcher.get_fuzzy_score("", ""), 100)  # Empty strings
        self.assertEqual(
            FuzzyMatcher.get_fuzzy_score("word", ""), 0
        )  # One empty string
        self.assertEqual(
            FuzzyMatcher.get_fuzzy_score("", "word"), 0
        )  # One empty string
        self.assertEqual(
            FuzzyMatcher.get_fuzzy_score("a" * 1000, "b" * 1000), 0
        )  # Very long strings
        self.assertGreaterEqual(
            FuzzyMatcher.get_fuzzy_score("hello", "hello world"), 65
        )  # Partial match
        self.assertEqual(
            FuzzyMatcher.get_fuzzy_score("hello", "hello"), 100
        )  # Exact match
        self.assertLess(
            FuzzyMatcher.get_fuzzy_score("hello", "goodbye"),
            80,
        )  # No match
        self.assertEqual(
            FuzzyMatcher.get_fuzzy_score("123", "abc"), 0
        )  # Different character types
        self.assertGreaterEqual(
            FuzzyMatcher.get_fuzzy_score("hello", "HeLLo"), 40
        )  # Case-insensitive
        self.assertGreaterEqual(
            FuzzyMatcher.get_fuzzy_score("hello", "he llo"), 30
        )  # Spaces

    def test_check_semantic(self):
        # Test the check_similarity method with real spaCy library

        # Test with similar words
        self.assertGreater(
            self.sanitizer.semantic_checker.check_similarity("happy", "joyful"), 0.5
        )
        self.assertGreater(
            self.sanitizer.semantic_checker.check_similarity("angry", "furious"), 0.5
        )

        # Test with dissimilar words
        self.assertLess(
            self.sanitizer.semantic_checker.check_similarity("cat", "democracy"), 0.3
        )
        self.assertLess(
            self.sanitizer.semantic_checker.check_similarity("computer", "banana"), 0.2
        )

        # Test with same word
        self.assertAlmostEqual(
            self.sanitizer.semantic_checker.check_similarity("test", "test"),
            1.0,
            places=1,
        )

        # Test with empty strings
        self.assertEqual(self.sanitizer.semantic_checker.check_similarity("", ""), 0.0)
        self.assertEqual(
            self.sanitizer.semantic_checker.check_similarity("word", ""), 0.0
        )
        self.assertEqual(
            self.sanitizer.semantic_checker.check_similarity("", "word"), 0.0
        )

        # Test with punctuation
        self.assertGreater(
            self.sanitizer.semantic_checker.check_similarity("hello", "hello!"), 0.6
        )
        self.assertGreater(
            self.sanitizer.semantic_checker.check_similarity("question", "question?"),
            0.6,
        )

        # Test with multi-word phrases
        self.assertGreater(
            self.sanitizer.semantic_checker.check_similarity(
                "good morning", "have a nice day"
            ),
            0.3,
        )
        self.assertLess(
            self.sanitizer.semantic_checker.check_similarity(
                "artificial intelligence", "natural stupidity"
            ),
            0.65,
        )

        # Test with misspelled words
        self.assertGreater(
            self.sanitizer.semantic_checker.check_similarity("receive", "recieve"), 0.6
        )
        self.assertGreater(
            self.sanitizer.semantic_checker.check_similarity("separate", "seperate"),
            0.6,
        )

        # Test with very long strings
        long_string1 = "a" * 1000
        long_string2 = "b" * 1000
        self.assertLess(
            self.sanitizer.semantic_checker.check_similarity(
                long_string1, long_string2
            ),
            0.2,
        )

        # Real use case
        self.assertLess(
            self.sanitizer.semantic_checker.check_similarity("nigger", "bigger"), 0.35
        )
        self.assertLess(
            self.sanitizer.semantic_checker.check_similarity("duck", "fuck"), 0.35
        )
        self.assertLess(
            self.sanitizer.semantic_checker.check_similarity(
                "I have big dick", "My name is Dick"
            ),
            0.35,
        )

    def test_contains_toxicity(self):
        # Test with likely toxic text
        toxic_result = self.sanitizer.ai_handler.contains_toxicity(
            "You are a terrible person!"
        )
        self.assertIsInstance(toxic_result, float)
        self.assertGreater(toxic_result, 0.5)

        # Test with highly toxic text
        highly_toxic_result = self.sanitizer.ai_handler.contains_toxicity(
            "I hate you and wish you would die!"
        )
        self.assertIsInstance(highly_toxic_result, float)
        self.assertGreater(highly_toxic_result, 0.8)

        # Test with mildly toxic text
        mildly_toxic_result = self.sanitizer.ai_handler.contains_toxicity(
            "You're not very smart."
        )
        self.assertIsInstance(mildly_toxic_result, float)
        self.assertGreater(mildly_toxic_result, 0.3)
        self.assertLess(mildly_toxic_result, 0.8)

        # Test with text containing profanity
        profanity_result = self.sanitizer.ai_handler.contains_toxicity(
            "This movie is fucking awesome!"
        )
        self.assertIsInstance(profanity_result, float)
        self.assertGreater(profanity_result, 0.4)

        # Test with text containing racial slurs
        slur_result = self.sanitizer.ai_handler.contains_toxicity("He's such a nigger.")
        self.assertIsInstance(slur_result, float)
        self.assertGreater(slur_result, 0.9)

        # Test with likely non-toxic text
        non_toxic_result = self.sanitizer.ai_handler.contains_toxicity(
            "Have a nice day!"
        )
        self.assertIsInstance(non_toxic_result, float)
        self.assertLess(non_toxic_result, 0.5)

        # Test with neutral text
        neutral_result = self.sanitizer.ai_handler.contains_toxicity("The sky is blue.")
        self.assertIsInstance(neutral_result, float)

        # Test when AI is disabled
        self.sanitizer.use_ai = False
        disabled_result = self.sanitizer.check_text("Any text")
        self.assertTrue(disabled_result.is_clean)
        self.assertNotEqual(disabled_result.reason, "toxicity")

    def test_check_text_allowed(self):
        # Test check_text method with an allowed word
        self.sanitizer.allowed_words = ["duck", "bigger", "night"]
        result = self.sanitizer.check_text("duck")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertEqual(result.reason, "allowed_word")
        self.assertEqual(result.problematic_score, 0)

        result = self.sanitizer.check_text("bigger")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertEqual(result.reason, "allowed_word")
        self.assertEqual(result.problematic_score, 0)

        # Test with a word not in allowed list
        result = self.sanitizer.check_text("not in allowed list")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)  # Assuming it's not a banned word
        self.assertNotEqual(result.reason, "allowed_word")

    def test_check_text_ai_toxicity(self):
        # Ensure AI is enabled for this test
        self.sanitizer.use_ai = True

        # Test with a toxic phrase
        result = self.sanitizer.check_text("You are a terrible person!")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "toxicity")
        self.assertGreater(result.problematic_score, 50)

        # Test with a non-toxic phrase
        result = self.sanitizer.check_text("Have a nice day!")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertNotEqual(result.reason, "toxicity")

    def test_check_text_all_features_off(self):
        # Disable all advanced features
        self.sanitizer.use_fuzzy = False
        self.sanitizer.use_ai = False
        self.sanitizer.use_semantic = False
        self.sanitizer.banned_words = ["nigger", "fuck", "cunt"]

        # Test with an exact match to a banned word
        result = self.sanitizer.check_text("nigger")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertEqual(result.problematic_score, 100)

        # Test with a close match that should be caught because of normalizing
        result = self.sanitizer.check_text("n1gger")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")

        result = self.sanitizer.check_text("n1663r")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")

        result = self.sanitizer.check_text("Xxn1gg3rxx")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")

        # Test with a semantically similar word that should not be caught without semantic matching
        result = self.sanitizer.check_text("african american")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertNotEqual(result.reason, "banned_word")

        # Test with a toxic phrase that should not be caught without AI
        result = self.sanitizer.check_text("You are a terrible person!")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertNotEqual(result.reason, "toxicity")

        # Test with a clean word
        result = self.sanitizer.check_text("hello")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertIsNone(result.reason)
        self.assertEqual(result.problematic_score, 0)

        # Test for scunthrope that should fail as it contains "cunt"
        result = self.sanitizer.check_text("scunthrope")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertEqual(result.problematic_score, 100)

    def test_fuzzy_matching(self):
        self.sanitizer.use_fuzzy = True
        self.sanitizer.use_semantic = False
        self.sanitizer.use_ai = False
        self.sanitizer.fuzzy_threshold = 70
        self.sanitizer.banned_words = ["nigger", "fuck", "cunt"]
        self.sanitizer.allowed_words = ["bigger"]

        # Test with a word that's close to a banned word but not exact
        result = self.sanitizer.check_text("fock")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertGreater(result.problematic_score, 70)

        # Test with a word that's slightly further from a banned word
        result = self.sanitizer.check_text("fack")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertGreater(result.problematic_score, 70)

        # Test with a clean word that shouldn't be caught by fuzzy matching, but it will be because of false positive
        result = self.sanitizer.check_text("duck")
        self.assertIsInstance(result, ProfanityResult)
        # Depending on the fuzzy matching, "duck" might be falsely flagged as "fuck"
        # The test expects it to be flagged
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertGreater(result.problematic_score, 70)

        # Test with a word that is in allowed words
        result = self.sanitizer.check_text("bigger")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertEqual(result.reason, "allowed_word")

        # Test with a word that's very close to a banned word
        result = self.sanitizer.check_text("nigga")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertGreater(result.problematic_score, 70)

        # Reset fuzzy matching
        self.sanitizer.use_fuzzy = False

    def test_fuzzy_and_semantic_matching(self):
        self.sanitizer.use_fuzzy = True
        self.sanitizer.use_semantic = True
        self.sanitizer.use_ai = False
        self.sanitizer.fuzzy_threshold = 70
        self.sanitizer.similarity_threshold = 0.7
        self.sanitizer.banned_words = ["nigger", "fuck", "cunt", "idiot"]
        self.sanitizer.allowed_words = ["bigger"]

        # Test with an allowed word
        result = self.sanitizer.check_text("bigger")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertEqual(result.reason, "allowed_word")

        # Test with a word that fuzzy would flag as banned but has a different meaning than "nigger"
        result = self.sanitizer.check_text("digger")
        self.assertIsInstance(result, ProfanityResult)
        # Depending on the combined fuzzy and semantic matching, "digger" might not be flagged
        self.assertTrue(result.is_clean)
        # The reason might be 'low_problematic_score' due to adjustments in decide_result
        self.assertEqual(result.reason, "low_problematic_score")
        self.assertGreater(result.problematic_score, 30)

        result = self.sanitizer.check_text("hunt")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertEqual(result.reason, "low_problematic_score")
        self.assertGreater(result.problematic_score, 30)

        # Test with a word that fuzzy might not flag as banned but semantic would
        result = self.sanitizer.check_text("fucker")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertGreater(result.problematic_score, 70)

        # Test with a word that's very close to a banned word both fuzzy and semantically
        result = self.sanitizer.check_text("nigga")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertGreater(result.problematic_score, 70)

    def test_check_text_with_all_features_on(self):
        self.sanitizer.use_fuzzy = True
        self.sanitizer.use_semantic = True
        self.sanitizer.use_ai = True
        self.sanitizer.banned_words = ["evening", "nigger", "fuck", "cunt"]
        result = self.sanitizer.check_text("nigger")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertGreater(result.problematic_score, 90)
        self.assertLessEqual(result.problematic_score, 100)

        result = self.sanitizer.check_text("fuck")
        self.assertIsInstance(result, ProfanityResult)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "banned_word")
        self.assertGreater(result.problematic_score, 90)
        self.assertLessEqual(result.problematic_score, 100)

        # Test with a word in a banned list but not offensive, with use_ai it will be flagged as clean because it's
        # not toxic
        result = self.sanitizer.check_text("evening")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertNotEqual(result.reason, "banned_word")
        self.assertNotEqual(result.reason, "toxicity")
        self.assertGreaterEqual(result.problematic_score, 90)

        # Test with a word not in a banned list but offensive
        result = self.sanitizer.check_text("faggot")
        self.assertIsInstance(result, ProfanityResult)
        # Since "faggot" is not in banned_words but AI detects toxicity, it should be flagged
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "toxicity")
        self.assertGreater(result.problematic_score, 90)
        self.assertLessEqual(result.problematic_score, 100)

        # scunthrope problem
        result = self.sanitizer.check_text("scunthrope")
        self.assertIsInstance(result, ProfanityResult)
        self.assertTrue(result.is_clean)
        self.assertNotEqual(result.reason, "banned_word")
        self.assertNotEqual(result.reason, "toxicity")

        # Offensive sentence
        result = self.sanitizer.check_text("kill all cats")
        self.assertIsInstance(result, ProfanityResult)
        # AI should detect toxicity
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "toxicity")
        self.assertGreaterEqual(result.problematic_score, 0)
        self.assertLessEqual(result.problematic_score, 100)

    def test_decide_result(self):
        # Test decide_result method with two close scores
        results = [
            ProfanityResult("Result 1", "reason1", False, 80),
            ProfanityResult("Result 2", "reason2", False, 90),
        ]
        result = self.sanitizer.decide_result(results, "testword")
        self.assertEqual(result.problematic_score, 85)  # (90 + 80) // 2
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "reason2")

        # Test with one result
        results = [ProfanityResult("Result 1", "reason1", False, 70)]
        result = self.sanitizer.decide_result(results, "testword")
        self.assertEqual(result.problematic_score, 70)
        self.assertFalse(result.is_clean)
        self.assertEqual(result.reason, "reason1")

        # Test with no results
        results = []
        result = self.sanitizer.decide_result(results, "clean_word")
        self.assertTrue(result.is_clean)
        self.assertIsNone(result.reason)
        self.assertEqual(result.problematic_score, 0)

        # Test with scores below threshold
        self.sanitizer.min_problematic_score_threshold = 60
        results = [
            ProfanityResult("Result 1", "reason1", False, 50),
            ProfanityResult("Result 2", "reason2", False, 55),
        ]
        result = self.sanitizer.decide_result(results, "low_score_word")
        self.assertTrue(result.is_clean)
        self.assertEqual(result.reason, "low_problematic_score")
        self.assertEqual(result.problematic_score, 50)  # 100 - 50


if __name__ == "__main__":
    unittest.main()
