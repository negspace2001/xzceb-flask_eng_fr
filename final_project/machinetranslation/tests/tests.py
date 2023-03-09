import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        """ Tests translation from English Text to French Text """
        self.assertEqual(english_to_french("Pineapple"), "Ananas")
        self.assertEqual(english_to_french("I am at work"), "Je suis au travail")
    
    def test_french_to_english(self):
        """ Tests translation from French Text to English Text """
        self.assertEqual(french_to_english("Maison"), "House")
        self.assertEqual(french_to_english("Je fais les tests"), "I do the tests")
    
    def test_english2french_null_value(self):
        """ Tests translation of null value from English to French """
        self.assertRaises(ValueError, english_to_french, None)
    
    def test_french2english_null_value(self):
        """ Tests translation of null value from French to English """
        self.assertRaises(ValueError, french_to_english, None)
    
    def test_bonjour_to_hello(self):
        """ Tests translation from French Text Bonjour to English Text Hello """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    
    def test_hello_to_bonjour(self):
        """ Tests translation from English Text Hello to French Text Bonjour """
        self.assertEqual(english_to_french("Hello"), "Bonjour")

if __name__ == "__main__":
    unittest.main()