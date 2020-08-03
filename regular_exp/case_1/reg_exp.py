'''
Выяснить, подходит ли файл по маске
Примеры:
path\to\file\SCI_2020_16_05_16_28_TABLE_NAME OTHER INFO(1).xlsx
path\to\file\SCI_TABLE_NAME OTHER INFO(1).xlsx
path\to\file\TABLE_NAME OTHER INFO(1).xlsx
path\to\file\ICIS_2020_13_05_11_41_BLALBA_BLA.xls
path\to\file\ICIS_2020_13_05_11_41_BLALBA_BLA.xls.xlsx
У "подходящего файла":
Формат <имя источника>_<YYYY_dd_mm_HH_MM>_<все что угодно>.<формат файла>
В дальнейшем для обработки нужны (в последующих функциях):
путь до файла
полное имя файла
имя файла без расширения
И в данном случае все эти значения проще получить с помощью библиотеки os, без регулярок, советую посмотреть)
'''
import re
import os
from os import path

# enter the directory
directory = os.path.join('some_directory')
# take all file's name in directory variable
all_files = os.listdir(directory)
# enter source
source_file = 'ICIS'
# creating empty matching list
match_files = []
# go through the lis of all files
for file in all_files:
    match = re.fullmatch(
        rf'{source_file}_\d\d\d\d_\d\d_\d\d_\d\d_\d\d_.*\.txt', file)
    if match:
        match_files.append(path.join(directory, match.string))

match_files_only_name = []
for file in match_files:
    temp_string = path.splitext(file)[0]
    match_files_only_name.append(temp_string)

# directory
print('dirrectory = ', directory)
print('-------------------------')
# full name
print('list of match files = ', match_files)
print('-------------------------')
# name witout name suffix
print('only name from match_files with out name suffix = ',
      match_files_only_name)
