'''Дана строка, в которой буква h встречается минимум два раза.Удалите из
этой строки первое и последнее вхождение буквы h,а также все символы,
находящиеся между ними.'''

s = input()
pos = s.find('h')
rpos = s.rfind('h')
print(s[:(pos)], s[rpos + 1:], sep='')