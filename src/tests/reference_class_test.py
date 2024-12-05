import unittest
from entities.reference import Misc, Book


class TestReference(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_bibtex_code(self):
        ref = Misc(id=1, title="My Title")

        expected = (
            "@misc{1_My_Title,\n"
            "    title = {My Title},\n"
            "}"
        )

        self.assertEqual(ref.generate_bibtex_code(), expected)

    def test_generate_bibtex_code_with_extra_fields(self):
        ref = Book(id=2, title="Another Title", author="John Doe", year=2024, publisher="WSOY")

        expected = (
            "@book{2_Another_Title,\n"
            "    title = {Another Title},\n"
            "    author = {John Doe},\n"
            "    year = {2024},\n"
            "    publisher = {WSOY},\n"
            "}"
        )

        self.assertEqual(ref.generate_bibtex_code(), expected)

    def test_no_non_bibtex_fields_in_bibtex(self):
        ref = Book(id=1, title="Test Title", author="John Doe", year=2024, publisher="WSOY")

        bibtex = ref.generate_bibtex_code()

        for field in Book._non_bibtex_fields:
            self.assertNotIn(field, bibtex, f"Field '{field}' should not appear in BibTeX")


if __name__ == "__main__":
    unittest.main()
