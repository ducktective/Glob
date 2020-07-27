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
Пример 2
'''
import re
import os
import pathlib

directory = r'case_1\some_directory'
all_files = os.listdir(directory)
source_file = 'ICIS'
for i in all_files:
    match = re.fullmatch(
        rf'{source_file}_\d\d\d\d_\d\d_\d\d_\d\d_\d\d_.*\.txt', i)
    if match:
        print('ok', match)
print(os.path.abspath('asd.txt'))
