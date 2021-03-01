import unittest
from main import multiplication, multiplication_string


class TestMultiplication(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     # 1 user
    #     print('method SetUpClass')

    def setUp(self):
        print('method SetUp')
        # n users
        self.a = 3
        self.b = 4
        self.result = 12

    def test_number_3_4(self):
        print('test number 3 4')
        self.assertEqual(12, multiplication(3, 4))

    def test_strings_a_3(self):
        print('test line * 3')
        self.assertEqual('aaa', multiplication_string('a', 3))

    def tearDown(self):
        print('method tearDown')

    # @classmethod
    # def tearDownClass(cls):
    #     print('class method TearDownClass')


if __name__ == '__main__':
    unittest.main()
