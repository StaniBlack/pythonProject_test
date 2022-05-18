
# Цикл for

my_list = [1, 3, 6, 9, 12, 43, 66, 91, 11, 23, 6]

# 1. Найди сумму данного списка

my_list_1 = 0
for i in my_list:
    my_list_1 += i

print('my_list_1', my_list_1)

# 2. Найди сумму только первых пяти элементов (используй слайсирование)

my_list_2 = 0
for i in my_list[:5]:
    my_list_2 += i

print('my_list_1', my_list_1)

# 3. Найди  сумму всех чисел, которые меньше 10

qwe = 0
for i in my_list:
    if i < 10:
        qwe += i

print(qwe)

# 4. Распечатай список по элементам

for i in my_list:
    print(i)

# 5. Создай 2 новых списка: первый с числами, которые больше 20, второй со всеми остальными числами

q = []
w = []
for i in my_list:
    if i > 20:
        q.append(i)
    else:
        w.append(i)

print(q, w)





