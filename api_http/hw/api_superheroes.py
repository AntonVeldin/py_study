def get_heroes_id_dict(names):
    import requests
    heroes_id = {}
    for name in names:
        req = requests.get("https://superheroapi.com/api/2619421814940190/search/" + name)
        req.raise_for_status()
        res = req.json()
        heroes = res["results"]
        for hero in heroes:
            if hero["name"] == name:
                id = hero["id"]
                heroes_id.setdefault(name, id)
    return heroes_id


def max_intelligence_hero(names):
    import requests
    heroes_id = get_heroes_id_dict(names)
    max_intelligence = 0
    for name in names:
        id = heroes_id[name]
        req1 = requests.get("https://superheroapi.com/api/2619421814940190/" + id + "/powerstats")
        req1.raise_for_status()
        powerstats = req1.json()
        intelligence = int(powerstats["intelligence"])
        if intelligence > max_intelligence:
            max_intelligence = int(intelligence)
            max_intelligence_hero = name
    return [max_intelligence_hero, max_intelligence]


names = ["Hulk", "Captain America", "Thanos"]

hero_with_max_int = max_intelligence_hero(names)[0]
print(hero_with_max_int)