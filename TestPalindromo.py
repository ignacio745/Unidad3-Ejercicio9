from Palindromo import Palindromo
import unittest
from unittest import TestCase


class TestPalindromo(TestCase):
    __unPalindromo =  None
    __noPalindromo = None

    def setUp(self) -> None:
        self.__unPalindromo = Palindromo("amorroma")
        self.__noPalindromo = Palindromo("Prueba")
    
    def testUnPalindromo(self):
        self.assertTrue(self.__unPalindromo.esPalindromo())
    
    def testNoPalindromo(self):
        self.assertFalse(self.__noPalindromo.esPalindromo())

if __name__ == "__main__":
    unittest.main()