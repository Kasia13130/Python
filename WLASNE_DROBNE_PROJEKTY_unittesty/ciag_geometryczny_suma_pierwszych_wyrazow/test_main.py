import main
import unittest


class TestMain(unittest.TestCase):

    def test_GiveSumOfNElementsGeomSeq(self):

        self.assertEqual(80, main.GiveSumOfNElementsGeomSeq(2, 3, 4))
        self.assertNotEqual(-60, main.GiveSumOfNElementsGeomSeq(-2, -3, -3))
        self.assertEqual(26, main.GiveSumOfNElementsGeomSeq(2, 3, 3))