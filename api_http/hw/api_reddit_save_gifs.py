import os
from pprint import pprint

import requests

GIFS_DIR = "gifs"

# page1 = requests.get("https://queries.vscport.ru/task/processingvesselpart.aspx")
# # print(page1.text)
# print(page1.text)

response = requests.get(
    "https://www.reddit.com/r/gifs.json?limit=10",
    headers={"User-agent": "netology"}
)
if response.status_code != 200:
    raise Exception("Все очень плохо")
posts = response.json()["data"]["children"]

for post in posts:
    title: str = post["data"]["title"]
    url = post["data"]["url"]
    if "imgur.com/" not in url:
        continue
    url = url.replace(".gifv", ".gif")

    gif_resp = requests.get(url)
    gif_resp.raise_for_status()

    title = "".join(x for x in title if x.isalnum() or x.isspace())
    # title2 = "+".join(["A", "B", "C"])
    # print(title2)

    with open(os.path.join(GIFS_DIR, title + ".gif"), "wb") as f:
        f.write(gif_resp.content)
        print(title)