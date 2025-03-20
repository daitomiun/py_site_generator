import unittest
from main import extract_title

class TestMain(unittest.TestCase):

    def test_extract_title(self):
        title = extract_title("# test")
        self.assertEqual(title, "test")

    def test_fail_to_extract_title(self):
        with self.assertRaisesRegex(ValueError, "No h1 header found in markdown"):
            extract_title("#### test")


if __name__ == "__main__":
    unittest.main()
