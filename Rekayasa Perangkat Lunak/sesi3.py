"""
TUGAS PERTEMUAN 3 :
Buatlah program sederhana dengan control flow statement. Program harus memiliki variable sebagai berikut :
NIM, NamaMahasiswa, JenisKelamin, TanggalInputNilai, NamaMatakuliah, Absensi, Tugas, UTS, Dan UAS,
Nilai Akhir, KeteranganNilai (Lulus/Tidak Lulus).

Logika Algoritma :
Berikan rumus presentase pada grade nilai tersebut dan buat logika algoritma untuk menampilkan nilai Akhir
0 - 49 (Grade E), 50 - 59 (Grade D), 60 - 63,9 (Grade C), 64 - 67.9 (GradeC+), 68 - 70.9 (B -),
71 - 73.9 (Grade B), 74 - 76.9 (Grade B+), 77 - 79.9(Grade A-), 80 - 100 (Grade A).

"""
import math

NIM = input("Nomor Induk Mahasiswa: ")
NamaMahasiswa = input("Nama Mahasiswa: ")
JenisKelamin = input("Jenis Kelamin Mahasiswa (L/P): ")
TanggalInputNilai = input("Tanggal Input Nilai (DD/MM/YYYY): ")
NamaMatakuliah = input("Nama Matakuliah: ")
Absensi = int(input("Jumlah Kehadiran Mahasiswa (0-14): ")) / 14 * 100
Tugas = int(input("Nilai Tugas Mahasiswa: "))
UTS = int(input("Nilai Ujian Tengah Semester Mahasiswa: "))
UAS = int(input("Nilai Ujian Akhir Semester Mahasiswa: "))

NilaiAkhir = Tugas * 20 / 100 + UTS * 30 / 100 + UAS * 50 / 100

if NilaiAkhir > 50:
    KeteranganNilai = "(Lulus)"
    if NilaiAkhir >= 80:
        grade = 'A'
    elif NilaiAkhir >= 77:
        grade = 'A-'
    elif NilaiAkhir >= 74:
        grade = 'B+'
    elif NilaiAkhir >= 71:
        grade = 'B'
    elif NilaiAkhir >= 68:
        grade = 'B-'
    elif NilaiAkhir >= 64:
        grade = 'C+'
    elif NilaiAkhir >= 60:
        grade = 'C'
    elif NilaiAkhir >= 50:
        grade = 'D'
else:
    KeteranganNilai = "(Tidak Lulus)"
    grade = 'E'

print("--- Biodata Mahasiswa ---")
print(f"Nomor Induk: {NIM}")
print(f"Nama: {NamaMahasiswa}")
print(f"Jenis Kelamin: {JenisKelamin}")

print("\n--- Performa Perkuliahan Mahasiswa ---")
print(f"Persentase Kehadiran: {math.floor(Absensi)}%")
print(f"Tugas: {Tugas}")
print(f"Ujian Tengah Semester: {UTS}")
print(f"Ujian Akhir Semester: {UAS}")
print(f"Nilai Akhir: {NilaiAkhir}, {grade} {KeteranganNilai}")