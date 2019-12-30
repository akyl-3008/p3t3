lst = input("Введите целые числа через пробел: ") 
steps = input("Шаг: ") 
lst = lst[steps:] + lst[:steps]
print(lst)