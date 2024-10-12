import random
keys = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = input("Ведите длину пароля: ")
password = ""

if int(length) < 4:
    print("Ваш пароль слишком короткий. Программа установила длину 4 символа(минимум). ")
    length = 4

for i in range(int(length)):
    password += random.choice(keys)

print(password)
