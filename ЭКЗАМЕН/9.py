list = ["student1","student2","student3"]   # создаём список с нужными элементами
list1 = []                                  # создаём пустой список list1
for x in list:                              # создаём цикл for , где переменная x пройдёт по списку list
    x += "_good"                            # складываем строки x += "_good" аналогично записи x = x+"_good"
    list1.append(x)                         # добавляем в список list1 сложенные строки
print(list1)                                # выводим готовый список
