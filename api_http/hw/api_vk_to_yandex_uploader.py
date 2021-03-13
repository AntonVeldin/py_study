import requests
import sys
import time
import datetime
import json


def loading_bar(count, total, size):
    percent = float(count) / float(total) * 100
    sys.stdout.write(
        "\r" +
        str(int(count)).rjust(3, '0') +
        "/" +
        str(int(total)).rjust(3, '0') +
        ' [' +
        '=' * int(percent / 10) * size +
        ' ' * (10 - int(percent / 10)) * size +
        ']'
    )


class UserVK:
    url = "https://api.vk.com/method/"

    def __init__(self, token, api_version, user_id=None):
        self.token = token
        self.api_version = api_version
        self.user_id = user_id
        self.params = {
            "access_token": self.token,
            "v": self.api_version
        }
        res = requests.get(self.url + "users.get", self.params)
        res.raise_for_status()
        self.owner_id = res.json()["response"][0]["id"]

        if user_id is None:
            self.user_id = self.owner_id

    def get_profile_photos(self):
        get_photos_url = self.url + "photos.get"
        params_1 = {
            "owner_id": self.user_id,
            "extended": 1,
            "album_id": "profile"
        }
        pic_list = []

        res = requests.get(get_photos_url,
                           params={
                               **self.params,
                               **params_1
                                }
                           )
        res.raise_for_status()
        photos_list = res.json()["response"]["items"]

        for pic in photos_list:
            pic_dict = {"likes": "", "date": "", "size": "", "url": ""}
            pic_dict["likes"] = pic["likes"]["count"]
            pic_dict["date"] = pic["date"]
            pic_dict["url"] = pic["sizes"][-1]["url"]
            pic_dict["size"] = pic["sizes"][-1]["type"]
            pic_list.append(pic_dict)
        return pic_list

    def get_album(self):
        get_album_url = self.url + "photos.getAlbums"
        get_album_params = {"owner_id": self.user_id}
        res = requests.get(get_album_url,
                           params={
                               **self.params,
                               **get_album_params
                           }
                           )
        res.raise_for_status()
        albums_list = res.json()["response"]["items"]
        albums = []
        for album in albums_list:
            id = album["id"]
            title = album["title"]
            album_dict = {"id": "", "title": ""}
            album_dict["id"] = id
            album_dict["title"] = title
            albums.append(album_dict)
        return albums

    def get_photos(self):
        list_of_albums = self.get_album()
        get_photos_url = self.url + "photos.get"
        params_1 = {
            "owner_id": self.user_id,
            "extended": 1
        }
        pic_list = []
        for album in list_of_albums:
            album_id = album["id"]
            params_2 = {"album_id": album_id}
            album_name = album["title"]
            res = requests.get(get_photos_url,
                               params={
                                   **self.params,
                                   **params_1,
                                   **params_2
                               }
                               )
            res.raise_for_status()
            photos_list = res.json()["response"]["items"]

            for pic in photos_list:
                pic_dict = {"likes": "", "date": "", "size": "", "url": "", "album": ""}
                pic_dict["likes"] = pic["likes"]["count"]
                pic_dict["date"] = pic["date"]
                pic_dict["url"] = pic["sizes"][-1]["url"]
                pic_dict["size"] = pic["sizes"][-1]["type"]
                pic_dict["album"] = album_name
                pic_list.append(pic_dict)
        return pic_list

    def save_photos_to_ya_disc(self, ya_token, photos_from_all_albums=False):
        if photos_from_all_albums is False:
            pic_list = self.get_profile_photos()
            path = "/" + str(self.user_id) + "_all_photos/"
        elif photos_from_all_albums is True:
            pic_list = self.get_photos()
            path = "/" + str(self.user_id) + "_profile_photos/"

        HEADERS = {"Authorization": "OAuth " + ya_token}
        res = requests.put(
                "https://cloud-api.yandex.net/v1/disk/resources/",
                params={"path": path},
                headers=HEADERS
            )
        res.raise_for_status()
        json_file = []
        count = 0
        for pic in pic_list:

            count += 1
            loading_bar(count, len(pic_list), 1)

            likes = pic["likes"]
            url = pic["url"]
            size = pic["size"]
            time_now = datetime.datetime.now()
            time_now = time_now.strftime("%d-%m-%Y_%H-%M-%S")
            name = str(likes) + " " + str(time_now) + ".jpg"
            res = requests.post(
                "https://cloud-api.yandex.net/v1/disk/resources/upload",
                params={"path": path + name, "url": url},
                headers=HEADERS
            )
            res.raise_for_status()

            dict_for_json = {"size": size, "file_name": name}
            json_file.append(dict_for_json)
            time.sleep(1)
        with open("downloaded_photos.json", "w") as f:
            json.dump(json_file, f, ensure_ascii=False, indent=2)
        return


vk_version = "5.126"
vk_token = ""
vk_id = ""
ya_token = ""

user_1 = UserVK(vk_token, vk_version, vk_id)
user_1.save_photos_to_ya_disc(ya_token)

# сохранение фото из всех альбомов:
# user_1.save_photos_to_ya_disc(ya_token, True)