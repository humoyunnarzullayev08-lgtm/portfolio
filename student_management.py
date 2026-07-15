students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Talaba qo'shish")
    print("2. Talabalarni ko'rish")
    print("3. Talabani qidirish")
    print("4. Talabani o'chirish")
    print("5. Chiqish")

    choice = input("Tanlang (1-5): ")

    if choice == "1":
        name = input("Talaba ismi: ")
        age = input("Yoshi: ")
        students[name] = age
        print("Talaba qo'shildi!")

    elif choice == "2":
        if students:
            print("\nTalabalar ro'yxati:")
            for name, age in students.items():
                print(f"{name} - {age} yosh")
        else:
            print("Talabalar mavjud emas.")

    elif choice == "3":
        name = input("Qidirilayotgan talaba ismi: ")
        if name in students:
            print(f"{name} - {students[name]} yosh")
        else:
            print("Talaba topilmadi.")

    elif choice == "4":
        name = input("O'chiriladigan talaba ismi: ")
        if name in students:
            del students[name]
            print("Talaba o'chirildi.")
        else:
            print("Talaba topilmadi.")

    elif choice == "5":
        print("Dastur tugadi.")
        break

    else:
        print("Noto'g'ri tanlov!")
