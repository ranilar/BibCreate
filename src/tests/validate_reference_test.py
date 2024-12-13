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

    
    def test_missing_required_field_raises_error(self):
        with self.assertRaises(UserInputError) as context:
            validate_reference(
                "book",
                title="Valid Title",
                author="Valid Author",
                year="2024"
            )
        self.assertIn("Publisher is required.", context.exception.error_fields)

    def test_title_exceeding_max_length_raises_error(self):
        with self.assertRaises(UserInputError) as context:
            validate_reference(
                "book",
                title="A" * 101,
                author="Valid Author",
                year="2024",
                publisher="Valid Publisher",
                ISBN="1234567890123"
            )
        self.assertIn("Title must not exceed 100 characters.", context.exception.error_fields)

    def test_invalid_ISBN_length_raises_error(self):
        with self.assertRaises(UserInputError) as context:
            validate_reference(
                "book",
                title="Valid Title",
                author="Valid Author",
                year="2024",
                publisher="Valid Publisher",
                ISBN="1234"
            )
        self.assertIn("ISBN must be exactly 13 characters long.", context.exception.error_fields)

    def test_invalid_ISBN_characters_raises_error(self):
        with self.assertRaises(UserInputError) as context:
            validate_reference(
                "book",
                title="Valid Title",
                author="Valid Author",
                year="2024",
                publisher="Valid Publisher",
                ISBN="123456789abcd"
            )
        self.assertIn("ISBN must contain only numeric characters.", context.exception.error_fields)

    def test_numeric_field_invalid_value_raises_error(self):
        with self.assertRaises(UserInputError) as context:
            validate_reference(
                "article",
                title="Valid Title",
                author="Valid Author",
                year="twenty",
                journal="Valid Journal"
            )
        self.assertIn("Year must be a valid number.", context.exception.error_fields)

    def test_misc_reference_validates_correctly(self):
        validate_reference(
            "misc",
            title="Misc Title",
            note="This is a note with valid length."
        )

    def test_empty_field_is_ignored_if_not_required(self):
        validate_reference(
            "book",
            title="Valid Title",
            author="Valid Author",
            year="2024",
            publisher="Valid Publisher",
            ISBN="1234567890123",
            note="" 
        )

    def test_inproceeding_reference_validates_correctly(self):
        validate_reference(
            "inproceeding",
            title="Conference Paper Title",
            author="Author Name",
            year="2024",
            booktitle="Conference Proceedings",
            DOI="10.1000/xyz123",
            address="123 Conference Street"
        )

    def test_optional_field_exceeding_max_length_raises_error(self):
        with self.assertRaises(UserInputError) as context:
            validate_reference(
                "book",
                title="Valid Title",
                author="Valid Author",
                year="2024",
                publisher="Valid Publisher",
                ISBN="1234567890123",
                note="A" * 101
            )
        self.assertIn("Note must not exceed 100 characters.", context.exception.error_fields)

    def test_required_field_with_empty_string_raises_error(self):
        with self.assertRaises(UserInputError) as context:
            validate_reference(
                "book",
                title="",
                author="Valid Author",
                year="2024",
                publisher="Valid Publisher",
                ISBN="1234567890123"
            )
        self.assertIn("Title is required.", context.exception.error_fields)
    
    def test_empty_input_raises_error(self):
        with self.assertRaises(UserInputError) as context:
            validate_reference("book")
        self.assertIn("Title is required.", context.exception.error_fields)


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
