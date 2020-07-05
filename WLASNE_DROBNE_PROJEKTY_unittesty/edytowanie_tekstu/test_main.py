import unittest
import main
import tracemalloc
import main2
from mock import patch, mock_open

'''
def get_input(wiersz):
    return input(open("wiersz.txt"))
'''
tracemalloc.start()


class Test(unittest.TestCase):

    def test_main(self):

        self.assertFalse(main.textEdit.main())

    def test_main2(self):

        self.assertFalse(main2.main2())


if __name__ == "__main__":
    unittest.main()