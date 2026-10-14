from difflib import get_close_matches

buah = ["apel", "jeruk", "mangga", "melon", "markisa"]

masukan = input("cari buah: ").strip().lower()
hasil = get_close_matches(masukan, buah, n=1, cutoff=0.75)
if hasil:
    print(f"Buah {hasil[0]} tersedia")
else:
    print("Buah " + masukan + " tidak tersedia")

    buah.pop(1)