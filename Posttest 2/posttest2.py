#class komposisi
class CatatanRiwayat:

  def __init__(self, kode_riwayat, detail_transaksi):
    self.kode_riwayat = kode_riwayat
    self.detail_transaksi = detail_transaksi

  def cetak_struk(self):
    return (
        f"--- STRUK RESMI ---\nKode: {self.kode_riwayat}\nDetail:"
        f" {self.detail_transaksi}\n-------------------"
    )


#superclas
class Mobil:

  total_mobil = 0

  def __init__(self, id_mobil, merk, model, plat_nomor, harga_sewa):
    #atribt protected
    self._id_mobil = id_mobil
    self._merk = merk
    self._model = model
    self._harga_sewa_per_hari = harga_sewa

    self.status_tersedia = True
    self.__plat_nomor = plat_nomor

    Mobil.total_mobil += 1

  @property
  def plat_nomor(self):
    return self.__plat_nomor

  @property
  def harga_sewa_per_hari(self):
    return self._harga_sewa_per_hari

  @harga_sewa_per_hari.setter
  def harga_sewa_per_hari(self, nilai_baru):
    if nilai_baru <= 0:
      raise ValueError("Harga sewa harus berupa angka positif lebih dari 0!")
    self._harga_sewa_per_hari = nilai_baru

  def hitung_biaya(self, lama_sewa):
    return lama_sewa * self._harga_sewa_per_hari

  def tampilkan_detail(self):
    status = "Tersedia" if self.status_tersedia else "Sedang Disewa"
    return (
        f"[{self._id_mobil}] {self._merk} {self._model} ({self.plat_nomor}) -"
        f" Rp {self._harga_sewa_per_hari:,}/hari | Status: {status}"
    )


#subclas 1=
class MobilPenumpang(Mobil):

  def __init__(self, id_mobil, merk, model, plat_nomor, harga_sewa, jumlah_kursi):
    super().__init__(id_mobil, merk, model, plat_nomor, harga_sewa)
    self.jumlah_kursi = jumlah_kursi

  # method overriding
  def tampilkan_detail(self):
    detail_dasar = super().tampilkan_detail()
    return f"{detail_dasar} | Kategori: Penumpang ({self.jumlah_kursi} Kursi)"


#subclass 2
class MobilMewah(Mobil):

  def __init__(
      self,
      id_mobil,
      merk,
      model,
      plat_nomor,
      harga_sewa,
      fasilitas_vip,
      biaya_layanan_vip=100000,
  ):
    super().__init__(id_mobil, merk, model, plat_nomor, harga_sewa)
    self.fasilitas_vip = fasilitas_vip 
    self.biaya_layanan_vip = biaya_layanan_vip

  #metod overriding
  def hitung_biaya(self, lama_sewa):
    biaya_dasar = super().hitung_biaya(lama_sewa)
    return biaya_dasar + (self.biaya_layanan_vip * lama_sewa)

  #method overriding
  def tampilkan_detail(self):
    detail_dasar = super().tampilkan_detail()
    return (
        f"{detail_dasar} | Kategori: VIP ({self.fasilitas_vip}) + Rp"
        f" {self.biaya_layanan_vip:,}/hari"
    )


#class pelanggan
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

  def tampilkan_profil(self):
    return f"[{self.id_pelanggan}] {self.nama} | Telp: {self.nomor_telepon}"

  @classmethod
  def ubah_nama_instansi(cls, nama_baru):
    cls.nama_instansi = nama_baru


#class transaksi
class Transaksi:

  total_transaksi = 0

  def __init__(self, id_transaksi, pelanggan, mobil, lama_sewa):
    self.id_transaksi = id_transaksi
    self.pelanggan = pelanggan  
    self.mobil = mobil  
    self.lama_sewa = lama_sewa

    self.__total_biaya = self.mobil.hitung_biaya(self.lama_sewa)
    self.mobil.status_tersedia = False

    info = (
        f"{pelanggan.nama} menyewa {mobil._merk} {mobil._model} selama"
        f" {lama_sewa} hari. Total: Rp {self.__total_biaya:,}"
    )
    self.riwayat = CatatanRiwayat(f"LOG-{id_transaksi}", info)

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

  def proses_pengembalian(self):
    self.mobil.status_tersedia = True
    return (
        f"Mobil {self.mobil._merk} {self.mobil._model} telah berhasil"
        " dikembalikan."
    )

  @staticmethod
  def hitung_denda(hari_terlambat, tarif_harian):
    if hari_terlambat <= 0:
      return 0
    return hari_terlambat * (tarif_harian * 1.2)


#class agregasi
class PerusahaanRental:

  def __init__(self, nama_perusahaan):
    self.nama_perusahaan = nama_perusahaan
    self.daftar_mobil = [] 

  def tambah_mobil(self, mobil):
    self.daftar_mobil.append(mobil)

  def tampilkan_katalog(self):
    print(f"\n=== Katalog Perusahaan: {self.nama_perusahaan} ===")
    for m in self.daftar_mobil:
      print(m.tampilkan_detail())


#uji
if __name__ == "__main__":
  print("=== UJI INHERITANCE ===")
  mobil1 = MobilPenumpang(
      "M01", "Avanza", "Veloz", "KT 1234 AB", 300000, jumlah_kursi=7
  )
  mobil2 = MobilMewah(
      "M02",
      "Ferrari",
      "Roma",
      "KT 6969 CD",
      1000000,
      fasilitas_vip="Sopir + Mini Bar",
      biaya_layanan_vip=200000,
  )

  print(mobil1.tampilkan_detail())
  print(mobil2.tampilkan_detail())

  print("\n=== UJI AGREGASI ===")
  rental = PerusahaanRental("Rental Tam Hitam Samarinda")
  rental.tambah_mobil(mobil1)
  rental.tambah_mobil(mobil2)
  rental.tampilkan_katalog()

  print("\n=== UJI TRANSAKSI ===")
  pelanggan1 = Pelanggan("P01", "Bakil", "08123456789", "6471012345678901")
  pelanggan2 = Pelanggan("P02", "Budi", "08987654321", "6471098765432100")

  transaksi1 = Transaksi("TRX01", pelanggan1, mobil1, lama_sewa=3)
  transaksi2 = Transaksi("TRX02", pelanggan2, mobil2, lama_sewa=2)

  print(f"Total Biaya TRX01: Rp {transaksi1.total_biaya:,}")
  print(f"Total Biaya TRX02: Rp {transaksi2.total_biaya:,}")

  print("\n=== UJI KOMPOSISI ===")
  print(transaksi1.riwayat.cetak_struk())

  print("\n--- Pengembalian ---")
  print(transaksi1.proses_pengembalian())
  print("Status Mobil1 Akhir:", mobil1.tampilkan_detail())

  print("\n=== UJI SETTER ===")
  mobil1.harga_sewa_per_hari = 400000
  print(f"Harga sewa baru mobil1: Rp {mobil1.harga_sewa_per_hari:,}")

  try:
    mobil1.harga_sewa_per_hari = -50000
  except ValueError as e:
    print(f"Harga Sewa Invalid: {e}")

  try:
    pelanggan1.no_ktp = "ABC123INVALID"
  except ValueError as e:
    print(f"No KTP Invalid: {e}")