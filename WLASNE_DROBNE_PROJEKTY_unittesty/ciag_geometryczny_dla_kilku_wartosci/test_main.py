# poprawic bo zle dziala

import main
import unittest


class TestMain(unittest.TestCase):

    def test_GiveGeomSeqElement(self):

        self.assertNotEqual(8, main.GiveGeomSeqElement(3, 2, 10))
        self.assertEqual(32768, main.GiveGeomSeqElement(1, 2, 16))
        self.assertEqual(-32, main.GiveGeomSeqElement(1, -2, 6))
        self.assertNotEqual(1, main.GiveGeomSeqElement(1, 2, 0))
        self.assertEqual(0, main.GiveGeomSeqElement(1, 0, 2))

    def test_GiveGeomSeqElementII(self):

        self.assertTrue(main.GiveGeomSeqElementII())


if __name__ == "__main__":
    unittest.main()
