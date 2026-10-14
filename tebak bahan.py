import time

ingredient_list = ["terigu", "gula", "telur", "mentega", "susu", "coklat", "vanili"]

score = 0

print("Halo, Kamu harus menebak 3 bahan dari resep kue")
time.sleep(3)

ingredient_1 = input("bahan ke 1? ")

if ingredient_1 in ingredient_list:
    print(f"Tebakan kamu benar, {ingredient_1}")
    score += 1
else:
    print("Tebakan kamu salah")

time.sleep(2)

ingredient_2 = input("bahan ke 2? ")

if ingredient_2 in ingredient_list:
    print(f"Tebakan kamu benar, {ingredient_2}")
    score += 1
else:
    print("Tebakan kamu salah")

time.sleep(2)

ingredient_3 = input("bahan ke 3? ")

if ingredient_3 in ingredient_list:
    print(f"Tebakan kamu benar, {ingredient_3}")
    score += 1
else:
    print("Tebakan kamu salah")

time.sleep(2)

print(f"Selesai kamu memiliki {score} poin!")
print(f"Daftar bahan resep kue: {ingredient_list}")