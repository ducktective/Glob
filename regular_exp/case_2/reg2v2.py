'''
Пример 2
Составить из файлов в директории список с параметрами
Примеры:
10_STG.TABLE_1.sql
1_STG.sql
2_STG.TABLE_6.sql
4_STG.TABLE_3.sql
3_STG.TABLE_5.sql
DEV.sql
У "подходящего файла" формат:
<число>_<имя схемы>.<имя объекта>.sql
или
<число>_<имя схемы>.sql
имя схемы и имя объекта могут состоять только из букв, цифр и  "_"
Что нужно сделать:
Составить структуру(список, массив, словарь, что хочешь), в которой есть следующие значения:
Число
Имя схемы.имя объекта или Имя схемы
Логический флаг исходя из того, есть ли в имени объекта "VIEW"
Сам скрипт (тут он будет рассматриваться в примере 3)
Упорядочить эту структуру по значению числа, по возрастанию
'''
import re
import os
from os import path

# enter the directory
directory = os.path.join('folder')
# take all file's name in directory variable
all_files = os.listdir(directory)
# creat empty matching list
match_files = []
# go through the lis of all files
for file in all_files:
    match = re.fullmatch(
        r'\d+_\w+\.\w+\.sql', file)
    if match:
        match_files.append(path.join(match.string))
    match = re.fullmatch(
        r'\d+_\w+\.sql', file)
    if match:
        match_files.append(path.join(match.string))

fill = []
temp_dict = {}
for i in match_files:
    temp_dict = {}
    temp_re = re.match(r'\d+', i)
    temp_dict['number'] = temp_re.group(0)
    temp_re = re.match(r'\_(\w+?)', i)
    temp_dict['scheme_name_and_more'] = temp_re.group(1)
    fill.append(temp_dict)
print(fill)
