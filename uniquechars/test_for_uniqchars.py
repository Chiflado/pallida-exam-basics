import unittest
import unique_chars

class TestUnique_chars(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(unique_chars.unique_characters(''), [])

    def test_removing_same_letters(self):
        self.assertEqual(unique_chars.unique_characters("anagram"), ["n", "g", "r", "m"])

    def test_for_None(self):
        self.assertFalse(unique_chars.unique_characters(None))


if __name__ == '__main__':
    unittest.main()