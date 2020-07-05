import unittest
import main


class Test(unittest.TestCase):

    def test_main(self):

        self.assertFalse(main.NewYearsEveDay(day=27))
        self.assertFalse(main.NewYearsEveDay(month=5))
        self.assertFalse(main.NewYearsEveDay(year=2020))

        # przy tych wywolaniach test się nie wykona poniewaz wartosci parametrow sa bledne
        #self.assertFalse(main.NewYearsEveDay(day=-27))
        #self.assertFalse(main.NewYearsEveDay(month=13))


if __name__ == "__main__":
    unittest.main()