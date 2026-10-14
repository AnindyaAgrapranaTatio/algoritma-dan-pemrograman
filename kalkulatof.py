import time
import sys

print("Selamat datang di kalkulator")
time.sleep(2)
print("Berikan 2 angka dan pilih operasi matematika yang diinginkan.")
time.sleep(2)

def add_2_numbers(number_1, number_2):
    return number_1 + number_2

def subtract_2_numbers(number_1, number_2):
    return number_1 - number_2

def multiply_2_numbers(number_1, number_2):
    return number_1 * number_2

def divide_2_numbers(number_1, number_2):
    return number_1 / number_2


# Input angka dan tipe operasi
number_1 = float(input("Angka 1? "))
number_2 = float(input("Angka 2? "))
operation = int(input("Tipe Operasi? (1: Penjumlahan, 2: Pengurangan, 3: Perkalian, 4: Pembagian): "))

# Percabangan operasi matematika
if operation == 1:
    result = add_2_numbers(number_1, number_2)
elif operation == 2:
    result = subtract_2_numbers(number_1, number_2)
elif operation == 3:
    result = multiply_2_numbers(number_1, number_2)
elif operation == 4:
    if number_2 != 0:
        result = divide_2_numbers(number_1, number_2)
    else:
        print("Pembagian dengan nol tidak dimungkinkan!")
        time.sleep(2)
        sys.exit()
else:
    print("Nomor operasi tidak tepat.")
    time.sleep(2)
    sys.exit()

# Menampilkan hasil akhir
print(f"Hasil: {result}")