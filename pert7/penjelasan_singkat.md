# Simulasi UTS

## 1. Urutkan Array
Membuat array dengan nilai acak dan mengurutkannya dari kecil ke besar menggunakan `.sort()`.

```python
Nilai = [3, 7, 2, 5, 1, 4]
Nilai.sort()
print(Nilai)
```

---

## 2. Operasi pada NIM
Mengalikan setiap digit dalam NIM dengan 3 menggunakan list comprehension.

```python
nim = "20240801128"
Jumlah = [int(i) * 3 for i in nim]
print(Jumlah)
```

---

## 3. Array Ganjil, Genap, dan Tengah
Membuat array 1-8, lalu memisahkan bilangan ganjil, genap, dan elemen tengah (indeks 3-4).

```python
array = [1, 2, 3, 4, 5, 6, 7, 8]
ganjil = [i for i in array if i % 2 != 0]
genap = [i for i in array if i % 2 == 0]
tengah = array[3:5]

print(ganjil)
print(genap)
print(tengah)
```

---

## 4. Gabungkan Nama
Menggabungkan input nama depan, tengah, dan belakang menjadi satu string.

```python
first_name = str(input("Nama depan: "))
middle_name = str(input("nama tengah: "))
last_name = str(input("Nama belakang: "))
print("Nama lengkap: ", first_name + " " + middle_name + " " + last_name)
```

---

## 6. Jumlahkan Digit NIM
Menjumlahkan semua digit dalam NIM menggunakan list comprehension dan `sum()`.

```python
nim = "20240801128"
Jumlah = sum([int(i) for i in nim])
print(Jumlah)
```

---

## 7. Ganti Nilai Variabel
Mengganti nilai variabel `nilai` dari 100 menjadi 80.

```python
nilai = 100
nilai = 80
print(nilai)
```

---

## 8. Bandingkan Dua Variabel
Membandingkan dua variabel (`A` dan `B`) menggunakan operator perbandingan.

```python
A = 15
B = 20
banding = A >= B, A <= B
print(banding)
```

---

## 9. Tampilkan Array dengan Indeks
Menampilkan elemen array beserta indeksnya menggunakan `enumerate()`.

```python
array = ["a", 2, 'b', 4, 5]
for i, val in enumerate(array):
    print(i, val)
```

---

## 10. Unpack Array
Membuat array, lalu mengeluarkan setiap elemen ke dalam variabel terpisah.

```python
nilai = [1, 2, 3, 4, 5]
a, b, c, d, e = nilai
print(e)
print(a)
print(b)
```

---

## 11. Angka Terbesar dan Terkecil
Menemukan angka terbesar, terkecil, dan mengurutkan array menggunakan `max()`, `min()`, dan `sorted()`.

```python
array = [7, 3, 1, 8, 5, 9, 0]

besar = max(array)
kecil = min(array)
urutan = sorted(array)
print("Besar: ", besar)
print("Kecil: ", kecil)
print("Urutan: ", urutan)
```

---

##