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

  @property
  def plat_nomor(self):
    return self.__plat_nomor

  @property
  def harga_sewa_per_hari(self):
    return self.__harga_sewa_per_hari

  @harga_sewa_per_hari.setter
  def harga_sewa_per_hari(self, nilai_baru):
    if nilai_baru <= 0:
      raise ValueError("Harga sewa harus berupa angka positif lebih dari 0!")
    self.__harga_sewa_per_hari = nilai_baru

  def tampilkan_detail(self):
    status = "Tersedia" if self.status_tersedia else "Sedang Disewa"
    return (
        f"[{self.id_mobil}] {self.merk} {self.model} ({self.plat_nomor}) - Rp"
        f" {self.harga_sewa_per_hari:,}/hari | Status: {status}"
    )

  @classmethod
  def buat_dari_dict(cls, data):
    return cls(
        id_mobil=data["id_mobil"],
        merk=data["merk"],
        model=data["model"],
        plat_nomor=data["plat_nomor"],
        harga_sewa=data["harga_sewa"],
    )

class Pelanggan:

  nama_instansi = "Rental Mobil Jaya Abadi"

  def __init__(self, id_pelanggan, nama, nomor_telepon, no_ktp):
    self.id_pelanggan = id_pelanggan
    self.nama = nama
    self.nomor_telepon = nomor_telepon
    self.no_ktp = no_ktp

  @property
  def no_ktp(self):
    return self.__no_ktp

  @no_ktp.setter
  def no_ktp(self, nilai_baru):
    if not nilai_baru or not str(nilai_baru).isdigit():
      raise ValueError("Nomor KTP hanya boleh berisi angka!")
    self.__no_ktp = str(nilai_baru)

  # INSTANCE METHOD
  def tampilkan_profil(self):
    return f"[{self.id_pelanggan}] {self.nama} | Telp: {self.nomor_telepon}"

  # CLASS METHOD
  @classmethod
  def ubah_nama_instansi(cls, nama_baru):
    cls.nama_instansi = nama_baru

class Transaksi:

  total_transaksi = 0

  def __init__(self, id_transaksi, pelanggan, mobil, lama_sewa):
    self.id_transaksi = id_transaksi
    self.pelanggan = pelanggan
    self.mobil = mobil

    self.lama_sewa = lama_sewa
    self.__total_biaya = self.hitung_total_biaya()

    self.mobil.status_tersedia = False
    Transaksi.total_transaksi += 1

  @property
  def lama_sewa(self):
    return self.__lama_sewa

  @lama_sewa.setter
  def lama_sewa(self, nilai_baru):
    if nilai_baru <= 0:
      raise ValueError("Lama sewa minimal 1 hari!")
    self.__lama_sewa = nilai_baru

  @property
  def total_biaya(self):
    return self.__total_biaya

  def hitung_total_biaya(self):
    return self.lama_sewa * self.mobil.harga_sewa_per_hari

  def proses_pengembalian(self):
    self.mobil.status_tersedia = True
    return f"Mobil {self.mobil.merk} {self.mobil.model} telah berhasil dikembalikan."

  # STATIC METHOD
  @staticmethod
  def hitung_denda(hari_terlambat, tarif_harian):
    if hari_terlambat <= 0:
      return 0
    return hari_terlambat * (tarif_harian * 1.2)


#Uji Programm
#Membuat 2 objek per class
#2 Objek Mobil
mobil1 = Mobil("M01", "Ferrari", "Roma", "KT 1234 AB", 300000)
data_mobil2 = {
    "id_mobil": "M02",
    "merk": "Lamborjini",
    "model": "Diablo",
    "plat_nomor": "KT 6969 CD",
    "harga_sewa": 500000,
}
mobil2 = Mobil.buat_dari_dict(data_mobil2) 

#2 Objek Pelanggan
pelanggan1 = Pelanggan("P01", "Bakil", "08123456789", "6471012345678901")
pelanggan2 = Pelanggan("P02", "Budi", "08987654321", "6471098765432100") 

#2 Objek Transaksi
transaksi1 = Transaksi("TRX01", pelanggan1, mobil1, 3)
transaksi2 = Transaksi("TRX02", pelanggan2, mobil2, 2)  

#Ngetes Methodd
print("===Ngetes Metod===")
#instance method
print("Profil Pelanggan :", pelanggan1.tampilkan_profil())  
print("Status Mobil Awal:", mobil1.tampilkan_detail())  
print(f"Total Biaya Sewa : Rp {transaksi1.total_biaya:,}")

#class method
Pelanggan.ubah_nama_instansi("Rental Tam Hitam Samarinda")
print("Nama Instansi Baru:", Pelanggan.nama_instansi)

#class method
denda = Transaksi.hitung_denda(hari_terlambat=2, tarif_harian=300000)
print(f"Denda Keterlambatan (2 Hari): Rp {denda:,.0f}")

print("\n--- Proses Pengembalian ---")
print(transaksi1.proses_pengembalian())
print("Status Mobil Akhir:", mobil1.tampilkan_detail())

#Uji Validasi Setter
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