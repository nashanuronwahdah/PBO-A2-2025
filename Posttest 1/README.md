# PBO-A2-2025

Posttest 1
JUDUL: "Rental Tam Hitam Samarinda"
Disini ada 3 kelas utama yaitu Mobil untuk data ketersediaan mobilm Pelanggan untuk data penyewa, Transaksi untukngolah proses sewanya.


# 1. Tema dan Class
# 3 class utama yang berdiri sendiri atau saling berinteraksi (menggunakan objek satu sama lain).

Class Pertama
class Mobil:

  total_mobil = 0

  def __init__(self, id_mobil, merk, model, plat_nomor, harga_sewa):
    self.id_mobil = id_mobil
    self.merk = merk
    self.model = model
    self.status_tersedia = True

    self.__plat_nomor = plat_nomor
    self.harga_sewa_per_hari = harga_sewa

    Mobil.total_mobil += 1

Class Kedua
class Pelanggan:

  nama_instansi = "Rental Mobil Jaya Abadi"

  def __init__(self, id_pelanggan, nama, nomor_telepon, no_ktp):
    self.id_pelanggan = id_pelanggan
    self.nama = nama
    self.nomor_telepon = nomor_telepon
    self.no_ktp = no_ktp

Class Ketiga:
class Transaksi:

  total_transaksi = 0

  # Menerima objek pelanggan dan mobil sebagai parameter
  def __init__(self, id_transaksi, pelanggan, mobil, lama_sewa):
    self.id_transaksi = id_transaksi
    self.pelanggan = pelanggan  # Objek Pelanggan
    self.mobil = mobil  # Objek Mobil

    self.lama_sewa = lama_sewa
    self.__total_biaya = self.hitung_total_biaya()

    self.mobil.status_tersedia = False
    Transaksi.total_transaksi += 1

  # Mengakses atribut harga dari objek mobil
  def hitung_total_biaya(self):
    return self.lama_sewa * self.mobil.harga_sewa_per_hari

# 2 Atribut
# Contoh tiga atribut kelas yg dipakai di seluruh program
class Mobil:

  total_mobil = 0  # Menghitung total unit mobil terdaftar


class Pelanggan:

  nama_instansi = "Rental Mobil Jaya Abadi"  # Nama instansi bersama
  


class Transaksi:

  total_transaksi =  0  # Menghitung total transaksi yang berjalan

# Atribut Instance
# Diinisialisasi di dalan __init__ () menggunakan self dan bernilai unik untuk setiap objek.
class Mobil:

  def __init__(self, id_mobil, merk, model, plat_nomor, harga_sewa):
    self.id_mobil = id_mobil
    self.merk = merk
    self.model = model
    self.status_tersedia = True

# Atribut instance unik tersebut untuk setiap objek mobil

# Atribut Publik dan Private
class Pelanggan:

  def __init__(self, id_pelanggan, nama, nomor_telepon, no_ktp):
    # atribut yg di bawah ini bersifat publik dan bisa diakses dari luar
    self.id_pelanggan = id_pelanggan
    self.nama = nama
    self.nomor_telepon = nomor_telepon

   # Yang di bawah ini adalah contoh atribut private, nanti ia akan mengakses setter no_ktp yang berisi self.__no_ktp
    @no_ktp.setter
    def no_ktp(self, nilai_baru):
    if not nilai_baru or not str(nilai_baru).isdigit():
      raise ValueError("Nomor KTP hanya boleh berisi angka!")
    self.__no_ktp = str(nilai_baru)
  
# 3 Method
# Contoh Instance Method (Menerima self untuk mengolah, menampilkan, atau mengubah data objek)
class Mobil:
  def tampilkan_detail(self):
    status = "Tersedia" if self.status_tersedia else "Sedang Disewa"
    return f"[{self.id_mobil}] {self.merk} {self.model} ({self.plat_nomor}) - Rp {self.harga_sewa_per_hari:,}/hari | Status: {status}"

# Class Method (Menerima parameter cls dan menggunakan decorator @classmethod) Ini masih berada di class mobil) 
@classmethod
  def buat_dari_dict(cls, data):
    return cls(
        id_mobil=data["id_mobil"],
        merk=data["merk"],
        model=data["model"],
        plat_nomor=data["plat_nomor"],
        harga_sewa=data["harga_sewa"],
    )

# Static Method (Menggunakan  decorator @staticmethod, tanpa self maupun cls)
class Transaksi:
  @staticmethod
  def hitung_denda(hari_terlambat, tarif_harian):
    if hari_terlambat <= 0:
      return 0
    return hari_terlambat * (tarif_harian * 1.2)

# 4 Getter, Setter, dan Validasi Data
class Pelanggan:

  def __init__(self, id_pelanggan, nama, nomor_telepon, no_ktp):
    self.id_pelanggan = id_pelanggan
    self.nama = nama
    self.nomor_telepon = nomor_telepon
    # Mengisi atribut private via Setter agar melewati proses validasi
    self.no_ktp = no_ktp

  # GEtter (Menggunakan decorator @property)
  @property
  def no_ktp(self):
    return self.__no_ktp

  # Setter (Menggunakan @<nama_properti>.setter dengan nama fungsi yang sama persis)
  @no_ktp.setter
  def no_ktp(self, nilai_baru):
  
  #  3. VALIDASI DATA
    if not nilai_baru or not str(nilai_baru).isdigit():
      raise ValueError("Nomor KTP hanya boleh berisi angka!")

  # Memperbarui nilai atribut private
    self.__no_ktp = str(nilai_baru)

# 5 Pengujian Program
# Uji Programm
# Membuat 2 objek per class
# 2 Objek Mobil
mobil1 = Mobil("M01", "Ferrari", "Roma", "KT 1234 AB", 300000)
data_mobil2 = {
    "id_mobil": "M02",
    "merk": "Lamborjini",
    "model": "Diablo",
    "plat_nomor": "KT 6969 CD",
    "harga_sewa": 500000,
}
mobil2 = Mobil.buat_dari_dict(data_mobil2) 

# 2 Objek Pelanggan
pelanggan1 = Pelanggan("P01", "Bakil", "08123456789", "6471012345678901")
pelanggan2 = Pelanggan("P02", "Budi", "08987654321", "6471098765432100") 

# 2 Objek Transaksi
transaksi1 = Transaksi("TRX01", pelanggan1, mobil1, 3)
transaksi2 = Transaksi("TRX02", pelanggan2, mobil2, 2)  

# Ngetes Methodd
print("===Ngetes Metod===")
# instance method
print("Profil Pelanggan :", pelanggan1.tampilkan_profil())  
print("Status Mobil Awal:", mobil1.tampilkan_detail())  
print(f"Total Biaya Sewa : Rp {transaksi1.total_biaya:,}")

# class method
Pelanggan.ubah_nama_instansi("Rental Tam Hitam Samarinda")
print("Nama Instansi Baru:", Pelanggan.nama_instansi)

# class method
denda = Transaksi.hitung_denda(hari_terlambat=2, tarif_harian=300000)
print(f"Denda Keterlambatan (2 Hari): Rp {denda:,.0f}")

print("\n--- Proses Pengembalian ---")
print(transaksi1.proses_pengembalian())
print("Status Mobil Akhir:", mobil1.tampilkan_detail())

# Output
===Ngetes Metod===
Profil Pelanggan : [P01] Bakil | Telp: 08123456789
Status Mobil Awal: [M01] Ferrari Roma (KT 1234 AB) - Rp 300,000/hari | Status: Sedang Disewa
Total Biaya Sewa : Rp 900,000
Nama Instansi Baru: Rental Tam Hitam Samarinda
Denda Keterlambatan (2 Hari): Rp 720,000

--- Proses Pengembalian ---
Mobil Ferrari Roma telah berhasil dikembalikan.
Status Mobil Akhir: [M01] Ferrari Roma (KT 1234 AB) - Rp 300,000/hari | Status: Tersedia

# Uji Validasi Setter
print("\n=== UJI VALIDASI SETTER ===")
# Input Valid
mobil1.harga_sewa_per_hari = 400000
print(f"Harga sewa baru (Valid)  : Rp {mobil1.harga_sewa_per_hari:,}")

# Input Invalid
try:
  mobil1.harga_sewa_per_hari = -50000
except ValueError as e:
  print(f"Uji Invalid Harga Sewa : Ditolak! ({e})")

try:
  pelanggan1.no_ktp = "ABC123"
except ValueError as e:
  print(f"Uji Invalid No KTP     : Ditolak! ({e})")

# Output
=== UJI VALIDASI SETTER ===
Harga sewa baru (Valid)  : Rp 400,000
Uji Invalid Harga Sewa : Ditolak! (Harga sewa harus berupa angka positif lebih dari 0!)
Uji Invalid No KTP     : Ditolak! (Nomor KTP hanya boleh berisi angka!)
