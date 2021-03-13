class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        import os
        import requests

        file_name = os.path.basename(file_path)
        headers_for_resp = {"Authorization": "OAuth " + self.token}
        resp = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": file_name, "overwrite": "true"},
            headers=headers_for_resp
        )
        resp.raise_for_status()
        answer = resp.json()
        href = answer["href"]

        with open(file_path, "rb") as f:
            resp2 = requests.put(href, files={"file": f})
        resp2.raise_for_status()
        return print("Файл загружен")


token = ""
file_path = ""


if __name__ == '__main__':
    uploader = YaUploader(token)
    result = uploader.upload(file_path)