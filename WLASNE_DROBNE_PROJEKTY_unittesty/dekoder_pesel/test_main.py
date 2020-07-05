if 1:   # jesli jest 1 to dziala
    import main
    import unittest
    from unittest.mock import patch


    class TestMain(unittest.TestCase):

        @patch("main2.DekodowanieDnia.dzien", return_value="70")        # mockowanie funkcji dzien z klasy DekodowanieDnia z pliku main2, co ta funkcja ma zwrocic
        @patch("main.NumerPesel.getInput", return_value="93021503033")      # mockowanie funkcji getInput z klasy NumerPesel z pliku main, funkcja zwraca pesel
        def test_pesel(self, pesel):

            self.assertTrue(pesel())

        @patch("main.NumerPesel.getInput", return_value="93021503033")
        def test_pesel(self, pesel):
            self.assertTrue(main.NumerPesel.pesel())            # drugi sposob przy testowaniu funkcji (to samo co wyzej)


# przykladowy unittest na potrzeby sprawdzenia sposobu testowania funkcji z mockowaniem
if 0:       # jesli 0 to funkcja nie zadziala

    from unittest.mock import patch
    from unittest import TestCase


    def get_input(text):
        return input(text)


    def answer():
        ans = get_input("enter yes or no")
        if ans == "yes":
            return "you entered yes"
        if ans == "no":
            return "you entered no"


    class Test(TestCase):

        # get_input will return 'yes' during this test
        @patch("test_main.get_input", return_value="yes")
        def test_answer_yes(self, cos):
            self.assertEqual(answer(), "you entered yes")

        @patch("test_main.get_input", return_value="no")
        def test_answer_no(self, cos):
            self.assertEqual(answer(), "you entered no")


if __name__ == "__main__":
    unittest.main()