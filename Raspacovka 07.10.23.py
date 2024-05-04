def print_params(a = 1, b = 'String', c = True):  #Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию
    print(a, b, c)  # Функция должна выводить эти параметры.

print_params()  # Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(3, 4, 5)
print_params(b = 25)  # Проверьте, работают ли вызовы print_params(b = 25)
print_params(c = [1, 2, 3])  # Проверьте, работают ли вызов print_params(b = 25) print_params(c = [1,2,3])

values_list = [1, True, 'String']  # Создайте список values_list с тремя элементами разных типов.
values_dict = {'a' : 1, 'b' : True, 'c' : 'String'}  # Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
print_params(*values_list)  # Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
print_params(**values_dict)

values_list_2 = [2, False]  # Создайте список values_list_2 с двумя элементами разных типов
print_params(*values_list_2, 42)  # Проверьте, работает ли print_params(*values_list_2, 42)
