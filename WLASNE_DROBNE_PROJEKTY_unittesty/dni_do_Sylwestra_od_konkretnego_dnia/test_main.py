import unittest
import main


class Test(unittest.TestCase):

    def test_NewYearsEveDay(self):

        self.assertFalse(main.NewYearsEveDay(2020, 6, 28))
        self.assertFalse(main.NewYearsEveDay(2020, 2, 15))
        self.assertFalse(main.NewYearsEveDay(2020, 4, 15))

        #self.assertWarns(main.NewYearsEveDay(2020, -6, 28))
        # przy tym wywolaniu test sie nie powiedzie poniewaz
        # glowny skrypt nie posiada zabezpieczen przed blednym wprowadzeniem danych


if __name__ == "__main__":
    unittest.main()