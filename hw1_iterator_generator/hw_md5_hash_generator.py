import hashlib

my_origin_path = 'countries.json'


def create_hasher(origin_path):
    with open(origin_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        yield hashlib.md5(line.encode('utf-8')).hexdigest()


my_hesher = create_hasher(my_origin_path)
for el in my_hesher:
    print(el)



# with open(my_origin_json_path, 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         if line is not "":
#             print(line)
#             yield line





    # while line != final_line:
    #     line = f.readline()
    #     yield f.readline()
    #     print(line)


    # for line in lines:
    #     while line != "":
    #         print(line)




#
# def my_hasher(origin_path, result_path):
#     with open(origin_path, 'r'):




# print(hashlib.md5("}".encode('utf-8')).hexdigest())
