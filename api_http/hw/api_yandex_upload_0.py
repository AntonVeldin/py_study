from pprint import pprint
import requests

HEADERS = {"Authorization": "OAuth "}

resp = requests.get(
    "https://cloud-api.yandex.net/v1/disk/resources",
    params={"path": "/"},
    headers=HEADERS
)
resp.raise_for_status()
data = resp.json()

for file in data["_embedded"]["items"]:
    print(file["name"])
# pprint(data)

resp1 = requests.get(
    "https://cloud-api.yandex.net/v1/disk/resources/upload?path=%2F%20awesome.gif&overwrite=true",
    params={"path": "/awesome.gif", "overwrite": "true"},
    headers=HEADERS
    )

d = resp1.json()
href = d["href"]
# print(href)

with open("gifs/A little something not coronavirus.gif", "rb") as f:
    resp2 = requests.put(href, files={"file": f})
resp2.raise_for_status()