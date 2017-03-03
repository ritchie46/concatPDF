import unittest
from concatPDF.builder import Build, str_to_flt, natural_keys


class TestFileOrder(unittest.TestCase):
    def test_str_to_flt(self):
        self.assertEqual(str_to_flt("2.20"), 2.2)
        self.assertEqual(str_to_flt("2.2.0"), "2.2.0")
        self.assertEqual(natural_keys("1.1_you"), [1.1, "_you"])
        self.assertEqual(natural_keys("1_1_you"), [1, '_', 1, "_you"])
        self.assertEqual(natural_keys("_1.1_1foo2"), ['_', 1.1, '_', 1.0, 'foo', 2.0])


if __name__ == "__main__":
    unittest.main()