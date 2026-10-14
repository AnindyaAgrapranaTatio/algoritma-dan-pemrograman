print("Pilihan negara:")
print("1. Afrika Selatan")
print("2. Meksiko")
print("3. India")
print("4. Prancis")

country_choice = input("Pilih nomor negara (1-4): ")
user_age = int(input("Berapa umurmu? "))

if country_choice == "1":
    country = "Afrika Selatan"

    if user_age >= 16:
        print("Kamu boleh berkendara")
    else:
        print("Kamu tidak boleh berkendara")

elif country_choice == "2":
    country = "Meksiko"

    if user_age >= 17:
        print("Kamu boleh berkendara")
    elif user_age >= 15:
        print("Kamu boleh berkendara dengan pengawasan orang tua")
    elif user_age >= 14:
        print("Kamu boleh berkendara dengan pengawasan orang tua")
    else:
        print("Kamu tidak boleh berkendara")

elif country_choice == "3":
    country = "India"

    if user_age >= 17:
        print("Kamu boleh berkendara")
    else:
        print("Kamu tidak boleh berkendara")

elif country_choice == "4":
    country = "Prancis"

    if user_age >= 17:
        print("Kamu boleh berkendara")
    elif user_age >= 14:
        print("Kamu boleh berkendara dengan pengawasan orang tua")
    else:
        print("Kamu tidak boleh berkendara")

else:
    print("Pilihan negara tidak tersedia.")