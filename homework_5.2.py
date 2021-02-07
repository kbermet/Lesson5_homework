# Создать текстовый фай(не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

fname = "my_file.txt"

num_lines = 0
num_words = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_lines += 1
        num_words += len(words)
        print(f'You typed: {num_words} words')
        print(f'You typed: {num_lines} lines')

