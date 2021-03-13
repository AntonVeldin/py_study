import hashlib
import datetime


my_origin_path = 'countries.json'
my_log_path = 'log.txt'


def create_hasher(origin_path):
    with open(origin_path, 'r') as f:
        lines = f.readlines()
    for line in lines[:10]:
        yield hashlib.md5(line.encode('utf-8')).hexdigest()


def param_decorator_with_log(log_path):
    def decorator_logger_for_hash_generator(old_function):

        def new_function(generator, path):
            now = datetime.datetime.now()
            result = old_function(generator(path))

            result_list = []
            for el in generator(path):
                result_list.append(el)

            with open(log_path, 'a') as log_file:
                log_file.write(
                    'time: ' + str(now) + '\n'
                    'func_name: ' + old_function.__name__ + '\n'
                    'args: ' + generator.__name__ + ', ' + path + ', ' + log_path + '\n'
                    'result: ' + str(result_list) + '\n\n'
                )

            return result

        return new_function
    return decorator_logger_for_hash_generator


@param_decorator_with_log(log_path=my_log_path)
def print_for_hash_generator(hash_generator):
    for el in hash_generator:
        print(el)


print_for_hash_generator(create_hasher, my_origin_path)
