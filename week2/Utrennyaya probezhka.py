"""В первый день спортсмен пробежал X километров, а затем он каждый день
 увеличивал пробег на 10% от предыдущего значения (для решения задачи
 разрешается использовать числа с запятой, которые в Питоне пишутся
 через точку).

По данному числу X определите номер дня, на который пробег спортсмена
составит не менее Y километров."""

x = int(input())
y = int(input())

i = 1
while x < y:
    x *= 1.1
    i += 1
print(int(i))
