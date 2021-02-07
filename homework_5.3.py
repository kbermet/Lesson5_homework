# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

with open("text_3.txt", "r", encoding='utf-8') as f_obj:
    staff = {line.split()[0]: float(line.split()[1]) for line in f_obj}
    print(f'Average salary = {round(sum(staff.values()) / len(staff), 3)}\n'
          f'Less than 20K {[e[0] for e in staff.items() if e[1] < 20000]}')
