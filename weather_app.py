weather = {
    "Samarqand": "☀️ Quyoshli, 35°C",
    "Toshkent": "🌤 Qisman bulutli, 37°C",
    "Buxoro": "☀️ Issiq, 40°C",
    "Andijon": "🌦 Yomg'ir, 28°C",
    "Namangan": "⛅ Bulutli, 31°C"
}

city = input("Shahar nomini kiriting: ")

if city in weather:
    print(f"{city} ob-havosi:")
    print(weather[city])
else:
    print("Bu shahar bazada mavjud emas.")
