# Daftar pizza yang tersedia
available_pizzas = [
    "Pizza Keju",
    "Pizza Sosis",
    "Pizza Ayam",
    "Pizza Jamur"
]

# Harga setiap pizza
pizza_prices = {
    1: 20000,
    2: 25000,
    3: 30000,
    4: 22000
}

# Inisialisasi
pizza_order = []
total_price = 0

print("Halo!")

continue_ordering = True

while continue_ordering:
    answer = input("Apakah kamu mau menambah pesanan? (ya/tidak): ")

    if answer.lower() == "ya":
        print("\nDaftar Pizza:")
        for i, pizza in enumerate(available_pizzas, 1):
            print(f"{i}. {pizza} - Rp{pizza_prices[i]:,}")

        pizza_choice = int(input("Pizza apa yang mau kamu pesan? (masukkan angka): "))

        # Menambahkan pizza ke pesanan
        pizza_order.append(available_pizzas[pizza_choice - 1])

        # Menambahkan harga pizza ke total
        total_price += pizza_prices[pizza_choice]

        print(
            f"Kami menambahkan {available_pizzas[pizza_choice - 1]} "
            "ke Pizza Kedalam List"
        )

        print(f"Total sementara: Rp{total_price:,}\n")

    else:
        continue_ordering = False


# Menampilkan total sebelum tip
print(f"\nKamu harus membayar Rp{total_price:,}")


# Meminta tip
tip = int(input("Apakah kamu mau memberi tip (0% 10% 20%)? "))

total_price = total_price + (total_price * tip / 100)

print(f"\nTerimakasih! Total pesanan yang harus kamu bayar: Rp{total_price:,.0f}")