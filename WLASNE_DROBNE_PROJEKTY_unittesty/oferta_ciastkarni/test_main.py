import main
import unittest


class Test(unittest.TestCase):

    def test_main(self):

        self.assertTrue(main.Cake.show_info)

    def test_main2(self):

        self.assertTrue(main.Cake.set_filling)

    def test_main3(self):

        self.assertTrue(main.Cake.add_additives)


if __name__ == "__main__":
    unittest.main()