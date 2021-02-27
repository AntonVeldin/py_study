import hashlib

my_origin_path = 'countries.json'


def create_hasher(origin_path):
    with open(origin_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        yield hashlib.md5(line.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    my_hasher = create_hasher(my_origin_path)
    for el in my_hasher:
        print(el)
