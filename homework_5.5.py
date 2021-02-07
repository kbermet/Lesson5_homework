# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open("text_5.txt", 'w', encoding='utf-8') as new_file:
    my_list = [randint(1, 10) for _ in range(10)]
    new_file.write(''.join(map(str, my_list)))

print(sum(my_list))
