'''
Прочесть скрипт из файла, убрать все комментарии и отступы
Убрать все многострочные комментарии
Примеры:
    1./* asdfg*/,
    2./*gdf
    dfd
    s*/
они могут быть в несколько строк
комментарий от /* и до */
убрать все однострочные комментарии
Пример:  --kjhnbg
комментарий от -- и до конца строки
Убрать все отступы и пробелы в начале и конце строки
Должен получиться "чистый" скрипт)
'''
import re
import os
# we need that later, for all lines in file
al_rows = ''
# enter the directory
directory = os.path.join('example')
# take all file's name in directory variable
all_files = os.listdir(directory)
# in all files
for one_file in all_files:
    # opening files
    file = open(os.path.join(directory, one_file), mode='r', encoding='utf8')
    # add everythink in one big string object
    for i in file:
        al_rows += i
    # replace all type of coment on nothing
    al_rows = re.sub(r'(?s)/\*.*?\*/', '\n', al_rows)
    al_rows = re.sub(r'--.*', '', al_rows)
    # closing file
    file.close()
    # open file again, but with 'w' mode
    file = open(os.path.join(directory, one_file), mode='w', encoding='utf8')
    # write clean program
    file.write(al_rows)
    # close file
    file.close()
