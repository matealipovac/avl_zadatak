import unittest
from unittest.mock import patch
import hashlib
from entrypoint import create_hash

class TestCreateHash(unittest.TestCase):

    def test_valid_hash(self):
        hashed_content = create_hash("md5", "message")
        expected_content = hashlib.md5("message".encode()).hexdigest()
        self.assertEqual(hashed_content, expected_content)

    def test_unsupported_hash(self):
        try:
            create_hash("invalid_hash", "message")
        except ValueError as e:
            self.assertEqual(str(e), "Unsupported hash function:invalid_hash")

    def test_error_handling(self):
        with patch("hashlib.new") as mock_hash:
            mock_hash.side_effect = Exception("Hashing error")
            hashed_content = create_hash("md5", "message")
            self.assertIsNone(hashed_content)
if __name__ == "__main__":
    unittest.main()
