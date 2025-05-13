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

## 12. Digit Genap dan Ganjil
Memisahkan digit genap dan ganjil dari NIM menggunakan list comprehension.

```python
nim = "22106666"
genap = [int(i) for i in nim if int(i) % 2 == 0]
ganjil = [int(i) for i in nim if int(i) % 2 != 0]
print("Genap: ", genap)
print("Ganjil: ", ganjil)
```

---

## 13. Hitung Luas Persegi
Membuat fungsi untuk menghitung luas persegi panjang (`panjang * lebar`).

```python
panjang = int(input("Panjang: "))
lebar = int(input("Lebar: "))

def LuasPersegi(panjang, lebar):
    return panjang * lebar

print(panjang, 'x', lebar, '=', LuasPersegi(panjang, lebar))
```

---

## 14. Urutkan Array Tanpa `sort()`
Mengurutkan array dari besar ke kecil menggunakan `sorted(reverse=True)`.

```python
array = [5, 3, 8, 2]
urut = sorted(array, reverse=True)
print(urut)
```

---

## 15. Gabungkan Nama Depan dan Belakang
Menggabungkan input nama depan dan belakang menjadi satu string.

```python
nama_depan = str(input("Nama depan: "))
nama_belakang = str(input("Nama belakang: "))

print(f"Halo, saya {nama_depan} {nama_belakang}")
```

---

## 16. Cek Palindroma
Membuat fungsi untuk mengecek apakah kata adalah palindroma (dibaca sama dari depan dan belakang).

```python
def is_palindroma(kata):
    return kata == kata[::-1]
kata = str(input("Masukan Kata: "))
print(kata)
if is_palindroma(kata):
    print("kata tersebut adalah palindroma")
else: 
    print("Kata tersebut bukan palindroma")

result = is_palindroma(kata)
print(f"Apakah '{kata}' adalah palindroma? {result}")
```

---

## 17. Kelipatan 3
Membuat list angka 1-20, lalu menampilkan angka yang habis dibagi 3 menggunakan list comprehension.

```python
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
kelipatan = [i for i in list if i % 3 == 0]
print(kelipatan)
```

---

## 18. Data Mahasiswa
Menampilkan nama mahasiswa dengan IPK di atas 3.0 dari list dictionary.

```python
mahasiswa = [
  {"nama": "Andi", "ipk": 3.2},
  {"nama": "Budi", "ipk": 2.9},
  {"nama": "Citra", "ipk": 3.7},
  {"nama": "Dewi", "ipk": 3.5},
  {"nama": "Eko", "ipk": 2.8},
  {"nama": "Fani", "ipk": 3.9},
  {"nama": "Gina", "ipk": 3.1},
  {"nama": "Hadi", "ipk": 2.7},
  {"nama": "Ika", "ipk": 3.4},
  {"nama": "Joko", "ipk": 2.6}
]
for mhs in mahasiswa:
    if mhs["ipk"] > 3.0:
        print("Mahasiswa dengan ipk 3.0: ", mhs["nama"])
```

---

## 19. Jumlahkan Digit Angka
Menjumlahkan semua digit dalam angka yang dimasukkan pengguna.

```python
jumlah_digit = input("Masukkan angka: ")
hasil = sum([int(i) for i in jumlah_digit])
print("Jumlah digit: ", hasil)
```

---

## 20. Konversi Angka ke Huruf
Membuat fungsi untuk mengonversi nilai angka (0-100) menjadi huruf (A-E) berdasarkan rentang nilai.

```python
nilai = int(input("Masukkan nilai: "))

def angka_ke_huruf(nilai):
    if 80 <= nilai <= 100:
        return "A"
    elif 70 <= nilai < 80:
        return "B"
    elif 60 <= nilai < 70:
        return "C"
    elif 50 <= nilai < 60:
        return "D"
    else:
        return "E"

print(angka_ke_huruf(nilai))
```