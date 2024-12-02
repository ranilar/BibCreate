import unittest
from util import validate_reference, UserInputError


class TestTReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_book_reference_does_not_raise_error(self):
        validate_reference(
            "book",
            title="ME",
            author="Valid Author",
            year="2024",
            publisher="Valid Publisher",
            ISBN="1234567890123"
        )

    def test_book_reference_with_invalid_ISBN_raises_error(self):
        with self.assertRaises(UserInputError) as context:
            validate_reference(
                "book",
                title="Valid",
                author="Valid Author",
                year="2024",
                publisher="Valid Publisher",
                ISBN="1234"
            )
        self.assertIn("ISBN", context.exception.args[0])


if __name__ == "__main__":
    unittest.main()
