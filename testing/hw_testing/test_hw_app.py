import hw_app
from mock import patch


class TestHW:

    @patch('hw_app.get_input', return_value='10006')
    def test_get_doc_owner_name(self, input):
        assert hw_app.get_doc_owner_name() == 'Аристарх Павлов'

    @patch('hw_app.get_input', return_value='10006')
    def test_get_doc_shelf(self, input):
        assert hw_app.get_doc_shelf() == '2'

    def test_show_document_info(self):
        x = {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        assert hw_app.show_document_info(x) == ("insurance", '10006', "Аристарх Павлов")

    def test_remove_doc_from_shelf_1(self):
        assert hw_app.remove_doc_from_shelf('10006') is True

    def test_remove_doc_from_shelf_2(self):
        assert hw_app.remove_doc_from_shelf('there is no doc') is False

    @patch('hw_app.get_input', return_value='4')
    def test_add_new_shelf_1(self, input):
        assert hw_app.add_new_shelf() == ('4', True)

    @patch('hw_app.get_input', return_value='3')
    def test_add_new_shelf_2(self, input):
        assert hw_app.add_new_shelf() == ('3', False)

    @patch('hw_app.get_input', return_value='10006')
    def test_delete_doc(self, input):
        assert hw_app.delete_doc() == ('10006', True)
