import json
import wikipedia

my_origin_json_path = 'countries.json'
my_result_json_path = 'result.json'


class WikiParser:

    def __init__(self, origin_json_path, result_json_path):
        self.origin_json_path = origin_json_path
        self.result_json_path = result_json_path
        self.country_link_list = []
        self.start = 0
        with open(self.origin_json_path, 'r') as f:
            self.json_data = json.load(f)#[:3]
        self.end = len(self.json_data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            with open(self.result_json_path, 'w', ) as f:
                json.dump(self.country_link_list, f, ensure_ascii=False, indent=4)
            raise StopIteration
        country_link_dict = {'name': None, 'link': None}
        country = self.json_data[self.start]['name']['official']
        try:
            country_link_dict['name'] = country
            country_link_dict['link'] = wikipedia.page(country).url
        except wikipedia.exceptions.PageError:
            print(country + " error 1")
            country_link_dict['link'] = None
        except wikipedia.exceptions.DisambiguationError:
            print(country + " error 2")
            country_link_dict['link'] = None
        self.country_link_list.append(country_link_dict)
        self.start += 1
        return self.start


if __name__ == '__main__':
    my_iterator = WikiParser(my_origin_json_path, my_result_json_path)
    for item in my_iterator:
        print(item)
