'''Дана строка, в которой буква h встречается как минимум два раза. Выведите
 измененную строку: повторите последовательность символов, заключенную между
  первым и последним появлением буквы h два раза (сами буквы h не входят в
   повторяемый фрагмент, т. е. их повторять не надо).'''

s = input()
pos = s.find('h')
rpos = s.rfind('h')
print(s[:rpos], s[pos + 1:rpos], s[rpos:], sep='')
