import hw_ya_app

token = hw_ya_app.token
folder_path = hw_ya_app.folder_path


class TestYaHW:
    import requests

    headers_for_resp = {"Authorization": "OAuth " + token}
    create_folder_resp = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources",
        params={"path": folder_path},
        headers=headers_for_resp
    )
    create_folder_resp.raise_for_status()

    def test_created_folder(self):
        # assert hw_ya_app.remove_doc_from_shelf('10006') is True
        cre
