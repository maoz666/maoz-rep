'''Дана строка. Замените в этой строке все появления буквы h на букву H,
 кроме первого и последнего вхождения.'''

s = input()
pos = s.find('h')
rpos = s.rfind('h')
substring = (s[(pos + 1):rpos]).replace('h', 'H')
print(s[:pos + 1], substring, s[rpos:], sep="")
