import time
print("Kali ini kita akan menghitung luas dari persegi dan volume dari kubus.")
time.sleep(2)
sisi = float(input("Berapa panjang sisi persegi? "))

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
print("Luas persegi:", luas_persegi(sisi))

def luas_kubus(luas):
    volume = luas * sisi
    return volume

print("Sekarang coba hitung volume kubus dengan sisi yang sama.")
time.sleep(2)
tebakan = float(input("Berapa volume kubus? "))

if tebakan == luas_kubus(luas_persegi(sisi)):
    print("Jawaban kamu benar!")
else :
    print("Jawaban kamu salah, coba lagi")

    repeat = input("Apakah kamu ingin mengulangi? (ya/tidak) ")
    while repeat.lower() == "ya":
        tebakan2 = float(input("Berapa volume kubus? "))
        if tebakan2 == luas_kubus(luas_persegi(sisi)):
            print("Jawaban kamu benar!")
        else:
            print("Jawaban kamu salah, coba lagi")
        repeat = input("Apakah kamu ingin mengulangi? (ya/tidak) ")

