# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об оrончании ввода данных свидетельствует пустая строка.

f = open("my_file.txt", 'w')
text = input('Enter anything here: ')
f.write(f"{text}\n")
f.close()