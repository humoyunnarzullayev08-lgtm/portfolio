tasks = []

while True:
    print("\n===== TO DO LIST =====")
    print("1. Vazifa qo'shish")
    print("2. Vazifalarni ko'rish")
    print("3. Vazifani o'chirish")
    print("4. Chiqish")

    choice = input("Tanlang (1-4): ")

    if choice == "1":
        task = input("Yangi vazifa: ")
        tasks.append(task)
        print("Vazifa qo'shildi.")

    elif choice == "2":
        if not tasks:
            print("Vazifalar mavjud emas.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("O'chirish uchun vazifa yo'q.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            index = int(input("O'chiriladigan vazifa raqami: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"'{removed}' o'chirildi.")
            else:
                print("Noto'g'ri raqam.")

    elif choice == "4":
        print("Dastur tugadi.")
        break

    else:
        print("Noto'g'ri tanlov.")
