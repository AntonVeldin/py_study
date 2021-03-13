from pprint import pprint


class YaFolderCreator:
    def __init__(self, token: str):
        self.token = token

    def create_folder(self, folder_path: str):
        import requests

        headers_for_resp = {"Authorization": "OAuth " + self.token}
        create_folder_resp = requests.put(
            "https://cloud-api.yandex.net/v1/disk/resources",
            params={"path": folder_path},
            headers=headers_for_resp
        )
        create_folder_resp.raise_for_status()


token = "AgAAAAAvdyWjAADLWxC8FfvGPkf3lofYcYA0_y0"
folder_path = "2_one"
x = {'description': 'Resource not found.',
 'error': 'DiskNotFoundError',
 'message': 'Не удалось найти запрошенный ресурс.'}

if __name__ == '__main__':
    # uploader = YaFolderCreator(token)
    # result = uploader.create_folder(folder_path)



    def test_created_folder():
        # assert hw_ya_app.remove_doc_from_shelf('10006') is True
        import requests

        headers_for_resp = {"Authorization": "OAuth " + token}
        create_folder_resp = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources",
            params={"path": folder_path},
            headers=headers_for_resp
        )
        # create_folder_resp.raise_for_status()
        resp = create_folder_resp.json()

        pprint(resp)
        print(create_folder_resp)

        # print(create_folder_resp.json())

    test_created_folder()



