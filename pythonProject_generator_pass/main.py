import random


massiv = '!@#$%^&*()1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ' #Список символов из которых будет составлен пароль
num = input('login ') #Ввод логина пользователя
password = ''
for x in range(8): #Количество символов в пароле (8)
    password = password + random.choice(list(massiv))
print(password)
r = input('Нажмите N чтобы выйти?\n')