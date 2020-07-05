import main
import unittest


class testMain(unittest.TestCase):

    def test_GiveGeomSeqElement(self):

        self.assertEqual(8, main.GiveGeomSeqElement(1, 2, 4))
        self.assertNotEqual(3, main.GiveGeomSeqElement(1, 4, 4))
        self.assertEqual(0, main.GiveGeomSeqElement(1, 0, 4))
        self.assertEqual(-8, main.GiveGeomSeqElement(1, -2, 4))
        self.assertNotEqual(14, main.GiveGeomSeqElement(1, 2, 5))


if __name__ == "__main__":
    unittest.main()
