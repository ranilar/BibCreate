import unittest
from util import validate_tag  

class TestValidateTag(unittest.TestCase):
    def test_validate_tag_valid(self):
        self.assertTrue(validate_tag("valid_tag"))
        self.assertTrue(validate_tag("a"))
        self.assertTrue(validate_tag("a" * 50))

    def test_validate_tag_invalid_length(self):
        with self.assertRaises(ValueError) as context:
            validate_tag("a" * 51) 
        self.assertEqual(str(context.exception), "Tag name must be between 1 and 50 characters.")

if __name__ == '__main__':
    unittest.main()