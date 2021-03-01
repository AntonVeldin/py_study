import json
import wikipedia

my_origin_json_path = 'countries.json'
my_result_json_path = 'result.json'


class WikiParser:

    def __init__(self, origin_json_path, result_json_path):
        self.origin_json_path = origin_json_path
        self.result_json_path = result_json_path

    def parse(self):
        country_link_list = []
        with open(self.origin_json_path, 'r') as f:
            json_data = json.load(f)
        for el in json_data[:10]:
            country_link_dict = {'name': None, 'link': None}
            country = el['name']['official']
            try:
                country_link_dict['name'] = country
                country_link_dict['link'] = wikipedia.page(country).url
                country_link_list.append(country_link_dict)
            except wikipedia.exceptions.PageError:
                print(country + " error 1")
                country_link_dict['link'] = None
                country_link_list.append(country_link_dict)
            except wikipedia.exceptions.DisambiguationError:
                print(country + " error 2")
                country_link_dict['link'] = None
                country_link_list.append(country_link_dict)

        with open(self.result_json_path, 'w',) as f:
            json.dump(country_link_list, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    my_parser = WikiParser(my_origin_json_path, my_result_json_path)
    my_parser.parse()
