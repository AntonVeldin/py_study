import requests
import math

with open("../token") as f:
    lines = f.readlines()
    token = lines[2][:-1]
    app_id = lines[3][:-1]
    version = lines[5]


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
        self.owner_id = requests.get(self.url + "users.get", self.params).json()["response"][0]["id"]
        if user_id is None:
            self.user_id = self.owner_id

    def __str__(self):
        user_url = "https://vk.com/id" + str(self.user_id)
        return user_url

    def __and__(self, other):
        list_1 = self.get_friends()
        list_2 = other.get_friends()
        list_3 = list(set(list_1) & set(list_2))
        return list_3

    def get_friends(self):
        get_friends_url = self.url + "friends.get"
        get_friends_params = {"user_id": self.user_id}
        res = requests.get(get_friends_url, params={**self.params, **get_friends_params}).json()

        pages = math.ceil(res["response"]["count"] / 100)
        full_list_of_friends = []
        offset = 0

        while pages != 0:
            offset_params = {"offset": offset}
            res = requests.get(get_friends_url, params={**self.params, **get_friends_params, **offset_params}).json()

            list_of_friends = res["response"]["items"]
            full_list_of_friends = full_list_of_friends + list_of_friends

            offset += 5000
            pages -= 1

        full_list_of_friends = list(set(full_list_of_friends))
        return full_list_of_friends


user_2_id = "1"

user_1 = UserVK(token, version)
user_2 = UserVK(token, version, user_2_id)

common_friends = user_1 & user_2
print(common_friends)

print(user_2)
print(user_1)


for fr in common_friends:
    user_n = UserVK(token, version, fr)
    print(user_n)