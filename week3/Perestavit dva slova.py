'''Дана строка, состоящая ровно из двух слов, разделенных пробелом.
Переставьте эти слова местами. Результат запишите в строку и выведите
получившуюся строку. При решении этой задачи нельзя пользоваться циклами
и инструкцией if.'''

s = input()

spacepos = s.find(' ')
print(s[spacepos + 1:], s[:spacepos])