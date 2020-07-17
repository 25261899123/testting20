"""Дан словарь в котором ключи должны быть только строковыми объектами, но
может встретиться Int, как в качестве ключа, но ваша проверка только
проверяет на строку и поэтому у вас выходит баг, ваша задача обработать
исключением ошибку TypeError
Пример:
dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
for x in dict_.keys():
x + 'abc'

Traceback (most recent call last):
File "server.py", line 152, in <module>
x + 'abc'
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Обработайте исключение"""

def metod():
    dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
    try:
        my_list = {key+'abc' for key,value in dict_.items()}

    except Exception as e:
        print(e)
        my_list = {str(key)+'abc' if type(key)== type(str) else ''for key,value in dict_.items()  }
    print(dict_)
metod()