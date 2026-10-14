import time
listA = [1, 2, 3, 4, 5]
listB = [6, 7, 8, 9, 10]
listC = []

for i in listA:
    listC.append(i*2)
for i in listB:
    listC.append(i*2)

print(listC)
print("Jumlah semua isi listC:", sum(listC))

time.sleep(1)
a = 1
while a <= 5:
    time.sleep(1)
    print(a*2)
    a += 1