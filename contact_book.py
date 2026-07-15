contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Kontakt qo'shish")
    print("2. Kontaktlarni ko'rish")
    print("3. Kontaktni qidirish")
    print("4. Kontaktni o'chirish")
    print("5. Chiqish")

    choice = input("Tanlang (1-5): ")

    if choice == "1":
        name = input("Ism: ")
        phone = input("Telefon raqami: ")
        contacts[name] = phone
        print("Kontakt qo'shildi.")

    elif choice == "2":
        if contacts:
            print("\nKontaktlar:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Kontaktlar mavjud emas.")

    elif choice == "3":
        name = input("Qidirilayotgan ism: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Kontakt topilmadi.")

    elif choice == "4":
        name = input("O'chiriladigan ism: ")
        if name in contacts:
            del contacts[name]
            print("Kontakt o'chirildi.")
        else:
            print("Kontakt topilmadi.")

    elif choice == "5":
        print("Dastur tugadi.")
        break

    else:
        print("Noto'g'ri tanlov!")
