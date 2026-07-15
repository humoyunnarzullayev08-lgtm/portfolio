print("Simple Calculator")

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

print("1. Qo'shish")
print("2. Ayirish")
print("3. Ko'paytirish")
print("4. Bo'lish")

choice = input("Tanlang (1-4): ")

if choice == "1":
    print("Natija:", a + b)
elif choice == "2":
    print("Natija:", a - b)
elif choice == "3":
    print("Natija:", a * b)
elif choice == "4":
    if b != 0:
        print("Natija:", a / b)
    else:
        print("0 ga bo'lish mumkin emas!")
else:
    print("Noto'g'ri tanlov!")
