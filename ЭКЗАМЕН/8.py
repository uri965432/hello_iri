list = [1, 5, 2, 9, 2, 9, 1]    # создаём список
for i in list:                  # создаём цикл for который переменной i будет проходить по списку list
    if list.count(i) == 1:      # создаём условие если число встречается в списке один раз - условие истинно
        print(i)
        