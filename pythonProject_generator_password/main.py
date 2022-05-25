import random

massiv = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = 0
while 0==0:
length = int(input('Какую нужно длину пароля?' + "\n"))
    for i in range(length):
        password += random.choice(massiv)
    print(password)




#chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#
#while 0==0:
#number = int(input('количество паролей?'+ "\n"))
#length = int(input('длина пароля?'+ "\n"))
#    for n in range(number):
#        password = ('')
#        for i in range(length):
#            password += random.choice(chars)
#        print(password)
#    r = input('Нажмите N чтобы выйти?\n')
#    if r == 'n':
#        break
