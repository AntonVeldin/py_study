import hashlib
import datetime


my_origin_path = '/Users/apple/PycharmProjects/Py_study/hw1_iterator_generator/countries.json'
my_log_path = 'log.txt'


def create_hasher(origin_path):
    with open(origin_path, 'r') as f:
        lines = f.readlines()
    for line in lines[:10]:
        yield hashlib.md5(line.encode('utf-8')).hexdigest()


def decorator_logger_for_hash_generator(old_function):

    def new_function(generator, path, log_path):
        now = datetime.datetime.now()
        result = old_function(generator(path))

        result_list = []
        for el in generator(path):
            result_list.append(el)

        with open(log_path, 'a') as log_file:
            log_file.write('time: ' + str(now) + '\n')
            log_file.write('func_name: ' + old_function.__name__ + '\n')
            log_file.write('args: ' + generator.__name__ + ', ' + path + '\n')
            log_file.write('result: ' + str(result_list) + '\n')
            log_file.write('\n')

            log_file.write(
                'time: ' + str(now) + '\n'
                'func_name: ' + old_function.__name__ + '\n'
                'args: ' + generator.__name__ + ', ' + path + ', ' + log_path + '\n'
                'result: ' + str(result_list) + '\n\n'
            )

        return result

    return new_function


@decorator_logger_for_hash_generator
def print_for_hash_generator(hash_generator):
    for el in hash_generator:
        print(el)


print_for_hash_generator(create_hasher, my_origin_path, my_log_path)
