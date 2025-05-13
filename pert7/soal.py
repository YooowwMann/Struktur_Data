def hitung_vokal(kalimat):
    vokal = "aiueoAIUEO"
    jumlah = 0
    for huruf in kalimat:
        if huruf in vokal:
            jumlah += 1
    return jumlah
kalimat = str(input("Masukkan kalimat: "))
print("Jumlah huruf vokal: ", hitung_vokal(kalimat))

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
masuk = int(input("Masukkan angka: "))
angka_lebih_dari = [i for i in array if i > masuk]

print("Angka lebih dari:", masuk , angka_lebih_dari)


array = [1,2,3,4,5,6]
for i in range(array[0], array[-1]+1):
    if i > 1:
        print(i)
        break
    else:
        print(0)

array = [[3], [4], [10], [19], [8], [1], [0], [12]]
print("Array 2D:", array[2][0])
print("Array 2D:", array[0][0])
