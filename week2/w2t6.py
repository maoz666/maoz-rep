'''В доме несколько подъездов. В каждом подъезде одинаковое
количество квартир. Квартиры нумеруются подряд, начиная с единицы.
 Может ли в некотором подъезде первая квартира иметь номер x, а
  последняя – номер y?'''
flat1 = int(input())
flat2 = int(input())

if flat2 // 5 == 0 and flat2 - flat1 == 4:
    print('YES')
else:
    print('NO')