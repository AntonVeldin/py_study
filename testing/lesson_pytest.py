from main import multiplication, multiplication_string


class TestMultiplication:

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print('method setup')

    def test_number_3_4(self):
        assert multiplication(3, 4) == 12, 'Ошибка'

    def test_string_a_3(self):
        assert multiplication_string('a', 3) == 'aaa', 'Ошибка'

    def teardown(self):
        print('method tear_down')

    def teardown_class(self_class):
        print('method tear_down_class')
