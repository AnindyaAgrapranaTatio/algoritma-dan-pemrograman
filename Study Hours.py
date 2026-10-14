#membuat variabel jam tidur, jam kerja, jam santai pada hari kerja, jam santai pada akhir pekan
jam_tidur = float(input("Masukkan jam tidur: "))
jam_kerja = float(input("Masukkan jam kerja: "))
jam_santai_hari_kerja = float(input("Masukkan jam santai pada hari kerja: "))
jam_santai_akhir_pekan = float(input("Masukkan jam santai pada akhir pekan: "))

#Kalkulasi jam kerja tersedia pada hari kerja (24 - jam kerja - jam tidur - jam santai pada hari kerja - 3)
Jam_kerja_tersedia_hari_kerja = 24 - jam_kerja - jam_tidur - jam_santai_hari_kerja - 3
#Kalkulasi jam kerja tersedia pada hari libur (24 - jam tidur - jam santai pada akhir pekan - 3)
Jam_kerja_tersedia_akhir_pekan = 24 - jam_tidur - jam_santai_akhir_pekan - 3

#Kalkulasi total jam kerja tersedia dalam seminggu (jam kerja tersedia pada hari kerja * 5 + jam kerja tersedia pada akhir pekan * 2)
Total_jam_kerja_tersedia = Jam_kerja_tersedia_hari_kerja * 5 + Jam_kerja_tersedia_akhir_pekan * 2

#Cetak hasil kalkulasi jam kerja tersedia pada hari kerja, jam kerja tersedia pada akhir pekan, dan total jam kerja tersedia dalam seminggu
print("Jam kerja tersedia pada hari kerja:", Jam_kerja_tersedia_hari_kerja)
print("Jam kerja tersedia pada akhir pekan:", Jam_kerja_tersedia_akhir_pekan)
print("Total jam kerja tersedia dalam seminggu:", Total_jam_kerja_tersedia)
