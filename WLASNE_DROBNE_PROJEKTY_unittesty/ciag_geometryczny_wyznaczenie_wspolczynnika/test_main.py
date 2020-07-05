import main
import unittest


class TestMain(unittest.TestCase):

    def test_GiveFactorForGeomSeq(self):

        self.assertEqual(8, main.GiveFactorForGeomSeq(2, 16))
        self.assertEqual(-4, main.GiveFactorForGeomSeq(2, -8))
        self.assertEqual(0, main.GiveFactorForGeomSeq(2, 0))
        self.assertNotEqual(6, main.GiveFactorForGeomSeq(3, 20))


if __name__ == "__main__":
    unittest.main()