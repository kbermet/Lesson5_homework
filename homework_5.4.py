# Создать (не прогаммно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translate = {"One": "Один",
             "Two":"Два",
             "Three": "Три",
             "Four": "Четыре"}

with open ('text_44.txt', 'w', encoding='utf-8') as rus_file:
    with open ('text_4.txt', encoding='utf-8') as my_file:
        rus_file.writelines([line.replace(line.split()[0], translate.get(line.split()[0]))
                             for line in my_file])
