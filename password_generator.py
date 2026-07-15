import random
import string

length = int(input("Parol uzunligini kiriting: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Yaratilgan parol:")
print(password)
