import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

    def test2(self):
        self.assertRaises(Exception, englishToFrench, "")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        
    def test2(self):
        self.assertRaises(Exception, frenchToEnglish, "")

unittest.main()