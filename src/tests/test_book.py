import unittest
from app import app

class TestBook(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_invalid_characters(self):
        data = {
            "title": "", 
            "author": "Test",
            "year": "2024",
            "publisher": "Test",
            "ISBN_number": "1234567891234", 
        }
        response = self.app.post("/add_book", data=data, follow_redirects=True)
        self.assertIn(b"Title must have 1-25 characters", response.data)

    def test_invalid_author(self):
        data = {
            "title": "Test",
            "author": "",  
            "year": "2024",
            "publisher": "Test",
            "ISBN_number": "1234567891234",
        }
        response = self.app.post("/add_book", data=data, follow_redirects=True)
        self.assertIn(b"Author must have 1-25 characters", response.data)
        
    def test_empty_year(self):
        data = {
            "title": "Test",
            "author": "Test",
            "year": "",
            "publisher": "Test",
            "ISBN_number": "1234567890123",
        }
        response = self.app.post("/add_book", data=data, follow_redirects=True)
        self.assertIn(b"Year is required", response.data)
        
    def test_negative_year(self):
        data = {
            "title": "Test",
            "author": "Test",
            "year": "-2024",
            "publisher": "Test",
            "ISBN_number": "1234567890123",
        }
        response = self.app.post("/add_book", data=data, follow_redirects=True)
        self.assertIn(b"Year must be a positive number", response.data)
        
    def test_invalid_publisher(self):
        data = {
            "title": "Test",
            "author": "Test",
            "year": "2024",
            "publisher": "",
            "ISBN_number": "1234567890123",
        }
        response = self.app.post("/add_book", data=data, follow_redirects=True)
        self.assertIn(b"Publisher must have 1-25 characters", response.data)
        
    def test_empty_ISBN(self):
        data = {
            "title": "Test",
            "author": "Test",
            "year": "2024",
            "publisher": "Test",
            "ISBN_number": "",
        }
        response = self.app.post("/add_book", data=data, follow_redirects=True)
        self.assertIn(b"ISBN_number is required", response.data)

    def test_negative_ISBN(self):
        data = {
            "title": "Test",
            "author": "Test",
            "year": "2024",
            "publisher": "Test",
            "ISBN_number": "-123456789123",
        }
        response = self.app.post("/add_book", data=data, follow_redirects=True)
        self.assertIn(b"ISBN number must be 13 digits", response.data)
    
    
if __name__ == "__main__":
    unittest.main()
