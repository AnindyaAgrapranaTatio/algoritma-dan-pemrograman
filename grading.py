import time
import sys

print("Silahkan berikan nilai antara 0 dan 10 (-1 untuk berhenti)")
time.sleep(2)

# Fungsi untuk mengumpulkan nilai dari pengguna
def get_grades_from_user(grades_list):
    ask_for_grades = True
    while ask_for_grades:
        user_input = input("Nilai berikutnya: ")
        grade = float(user_input)
        
        if grade == -1:
            ask_for_grades = False
        elif 0 <= grade <= 10:
            grades_list.append(grade)
           

# Fungsi untuk mencari nilai minimum
def compute_list_minimum(number_list):
    if not number_list:
        return None
    minimum = number_list[0]
    for item in number_list:
        if item < minimum:
            minimum = item
    return minimum

# Fungsi untuk mencari nilai maksimum
def compute_list_maximum(number_list):
    if not number_list:
        return None
    maximum = number_list[0]
    for item in number_list:
        if item > maximum:
            maximum = item
    return maximum

# Fungsi untuk menghitung rata-rata
def compute_list_average(number_list):
    if not number_list:
        return 0
    total_sum = sum(number_list)
    average = total_sum / len(number_list)
    return average

grades = []

# Mengambil nilai dari user
get_grades_from_user(grades)

# Pengecekan jika list kosong
if len(grades) == 0:
    print("Anda belum memberikan nilai apa pun!")
    time.sleep(2)
    sys.exit()

print(f"Kamu telah memberi {len(grades)} nilai.")
time.sleep(2)

# Menghitung statistik
minimum_val = compute_list_minimum(grades)
maximum_val = compute_list_maximum(grades)
average_val = compute_list_average(grades)

# Menampilkan hasil akhir
print(f"Min: {minimum_val}, Max: {maximum_val}, Rata rata: {average_val}")