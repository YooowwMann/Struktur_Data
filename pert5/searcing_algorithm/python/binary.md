#Binery Seardch

#Binery Search adalah algoritma pencarian yang efisien untuk menemukan posisi dari sebuah elemen dalam array yang sudah terurut.

#Algoritma ini bekerja dengan membagi dua bagian dari array yang sudah terurut dan membandingkan elemen tengah dengan elemen yang dicari.

#Jika elemen tengah lebih kecil dari elemen yang dicari, maka pencarian dilanjutkan pada bagian kanan dari array.

#Jika elemen tengah lebih besar dari elemen yang dicari, maka pencarian dilanjutkan pada bagian kiri dari array.

#Jika elemen yang dicari ditemukan, maka algoritma akan mengembalikan indeks dari elemen tersebut.

#Jika elemen yang dicari tidak ditemukan, maka algoritma akan mengembalikan -1.

#Contoh penggunaan algoritma Binery Search

#dapat dilihat pada kode di atas.

#Pada contoh di atas, kita memiliki array data yang sudah terurut dan kita ingin mencari elemen 3 dalam array tersebut.

#Kita menggunakan fungsi bs untuk melakukan pencarian dengan algoritma Binery Search.

#Jika elemen 3 ditemukan, maka fungsi akan mengembalikan indeks dari elemen tersebut.

#Jika elemen 3 tidak ditemukan, maka fungsi akan mengembalikan -1.

#Kita juga menampilkan hasil pencarian dengan mencetak indeks dari elemen yang ditemukan atau pesan "Not Found" jika elemen tidak ditemukan.

#Kelebihan dari algoritma Binery Search adalah efisiensinya dalam mencari elemen dalam array yang sudah terurut.

#Algoritma ini memiliki kompleksitas waktu O(log n), yang jauh lebih cepat dibandingkan dengan algoritma pencarian linear yang memiliki kompleksitas waktu O(n).

#Namun, algoritma Binery Search hanya dapat digunakan pada array yang sudah terurut.

#Jika array tidak terurut, maka kita harus mengurutkan array terlebih dahulu sebelum menggunakan algoritma ini.

#Dalam contoh di atas, kita menggunakan array data yang sudah terurut untuk melakukan pencarian.

#Namun, jika kita memiliki array yang tidak terurut, kita harus mengurutkan array terlebih dahulu sebelum menggunakan algoritma Binery Search.

#Kita dapat menggunakan algoritma pengurutan seperti Quick Sort atau Merge Sort untuk mengurutkan array sebelum melakukan pencarian.

#Dengan menggunakan algoritma Binery Search, kita dapat dengan cepat menemukan elemen yang dicari dalam array yang sudah terurut.