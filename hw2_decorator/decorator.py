# 1
# def foo():
#     print("func")
#     pass
#
#
# x_list = [foo, foo, foo]
# for function in x_list:
#     function()
# print("----1.end----")


# 2
# def foo():
#     print("func")
#
#
# def foo2():
#     return foo
#
#
# new_foo = foo2()
# new_foo()
# print("----2.end----")


# 3
# def foo2():
#     def foo():
#         print('func')
#     return foo
#
#
# x = foo2()
# x()
# print("----3.end----")


# 4
# def debugger_decorator(old_function):
#
#     def new_function(a, b):
#         print(f'вызвана функция {old_function.__name__}')
#         print(f'с аргументами {a} и {b}')
#         result = old_function(a, b)
#         print(f'возвращаем {result}')
#         return result
#
#     return new_function
#
#
# @debugger_decorator # sum = debugger_decorator(sum)??
# def sum(a, b):
#     return a + b
#
#
# sum(5, 2)
# print("----4.end----")


# 5
# def debugger_decorator(old_function):
#
#     def new_function(a, b):
#         print(f'вызвана функция {old_function.__name__}')
#         print(f'с аргументами {a} и {b}')
#         try:
#             result = old_function(a, b)
#             print(f'возвращаем {result}')
#             return result
#         except Exception as er:
#             print(f'выпало исключение {er}')
#
#     return new_function
#
#
# @debugger_decorator
# def sum(a, b, c):
#     return a + b + c
#
#
# sum(5, 2)
# print("----5.end----")


# 6
# ПРОБРОС ПАРАМЕТРОВ
#
# def debugger_decorator(old_function):
#
#     def new_function(*args, **kwargs):
#         print(f'вызвана функция {old_function.__name__}')
#         print(f'с аргументами {args} и {kwargs}')
#         try:
#             result = old_function(*args, **kwargs)
#             print(f'возвращаем {result}')
#             return result
#         except Exception as er:
#             print(f'выпало исключение {er}')
#
#     return new_function
#
#
# @debugger_decorator
# def sum(a, b, c, x):
#     return a + b + c + x
#
#
# sum(5, 2, c=4, x=5)
# print("----6.end----")


# 7
# def x70(old_function):
#     summ = 0
#     count = 0
#     def new_function(a, b):
#         something = old_function(a, b)
#         something = something * 70
#         nonlocal summ, count
#         summ += something
#         count += 1
#         return something, summ/count
#     return new_function
#
#
# @x70
# def summ(a, b):
#     return a + b
#
# print(summ(2, 1))
# print("----7.end----")


