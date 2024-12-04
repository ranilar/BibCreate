import unittest
from entities.reference import Reference

class TestReference(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_bibtex_code(self):
        ref = Reference(id=1, title="My Title", ref_type="misc")

        expected = (
            "@misc{1_My_Title,\n"
            "    title = {My Title},\n"
            "}"
        )

        self.assertEqual(ref.generate_bibtex_code(), expected)

    def test_generate_bibtex_code_with_extra_fields(self):
        ref = Reference(id=2, title="Another Title", ref_type="book")
        ref.author = "John Doe"
        ref.year = 2024
        ref.publisher = "WSOY"

        expected = (
            "@book{2_Another_Title,\n"
            "    title = {Another Title},\n"
            "    author = {John Doe},\n"
            "    year = {2024},\n"
            "    publisher = {WSOY},\n"
            "}"
        )

        self.assertEqual(ref.generate_bibtex_code(), expected)


if __name__ == "__main__":
    unittest.main()
