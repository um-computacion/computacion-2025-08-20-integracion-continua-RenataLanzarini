import unittest
from main import suma

class testprueba{unittest.case}:


    def test_suma(self):
        self.assertEquals(suma(2,3),5)


if __name__ =="__main__":
    unittest.main()
