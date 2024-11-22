import unittest
from util import validate_reference, UserInputError

class TestTReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_length_does_not_raise_error(self):
        validate_reference("Valid Title", "Valid Author", "2024", "Valid Publisher", "1234567890123")

    def test_too_short_or_long_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference("Sh", "Valid Author", "2024", "Valid Publisher", "1234567890123")

        with self.assertRaises(UserInputError):
            validate_reference("A" * 101, "Valid Author", "2024", "Valid Publisher", "1234567890123")


if __name__ == "__main__":
    unittest.main()