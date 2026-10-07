# 1. relasi UML

  # Asosiasi
class Transaksi:

  def __init__(self, id_transaksi, pelanggan, mobil, lama_sewa):
    self.id_transaksi = id_transaksi

    #relasi asosiasi
    # class transaksi terhubung menggunakan objek dari class Pelanggan dan Mobil
    self.pelanggan = pelanggan # Menyimpan objek Pelanggan
    self.mobil = mobil  # Menyimpan objek Mobil

    self.lama_sewa = lama_sewa

    # Mengakses atribut dan method milik objek Mobil yang diasosiasikan
    self.__total_biaya = self.mobil.hitung_biaya(self.lama_sewa)
    self.mobil.status_tersedia = False

  # Agregasi
  class PerusahaanRental:

  def __init__(self, nama_perusahaan):
    self.nama_perusahaan = nama_perusahaan

    #relasi agregasi
    # List ini menampung referensi objek mobil yang dibuat di luar
    self.daftar_mobil = []

  def tambah_mobil(self, mobil):
    # Objek mobil dimasukkan ke dalam daftar
    self.daftar_mobil.append(mobil)

  def tampilkan_katalog(self):
    print(f"\n=== Katalog Perusahaan: {self.nama_perusahaan} ===")
    for m in self.daftar_mobil:
      print(m.tampilkan_detail())

  # Komposisi
  class Transaksi:

  def __init__(self, id_transaksi, pelanggan, mobil, lama_sewa):
    self.id_transaksi = id_transaksi
    self.pelanggan = pelanggan
    self.mobil = mobil
    self.lama_sewa = lama_sewa
    self.__total_biaya = self.mobil.hitung_biaya(self.lama_sewa)

    # relasi komposisi
    # Objek CatatanRiwayat diciptakan langsung di dalam Transaksi
    # Keberadaannya bergantung penuh pada objek Transaksi ini
    info = (
        f"{pelanggan.nama} menyewa {mobil._merk} {mobil._model} selama"
        f" {lama_sewa} hari. Total: Rp {self.__total_biaya:,}"
    )
    self.riwayat = CatatanRiwayat(f"LOG-{id_transaksi}", info)


# 2. Inheritance

  # SuperClass
  class Mobil:

  total_mobil = 0

  def __init__(self, id_mobil, merk, model, plat_nomor, harga_sewa):
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
   # Class Mobil berperan sebagai induk yang mendefinisikan atribut dasar (_id_mobil, _merk, _model, _harga_sewa_per_hari) serta method dasar (hitung_biaya, tampilkan_detail) yang nantinya akan diturunkan dan dipakai ulang oleh kelas anaknya (subclass).

  # SubClass, super(), Atribuk unik (subclass), Overriding
  class MobilPenumpang(Mobil):

  def __init__(self, id_mobil, merk, model, plat_nomor, harga_sewa, jumlah_kursi):
    super().__init__(id_mobil, merk, model, plat_nomor, harga_sewa)
    self.jumlah_kursi = jumlah_kursi

  def tampilkan_detail(self):
    detail_dasar = super().tampilkan_detail()
    return f"{detail_dasar} | Kategori: Penumpang ({self.jumlah_kursi} Kursi)"


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

  def hitung_biaya(self, lama_sewa):
    biaya_dasar = super().hitung_biaya(lama_sewa)
    return biaya_dasar + (self.biaya_layanan_vip * lama_sewa)

  def tampilkan_detail(self):
    detail_dasar = super().tampilkan_detail()
    return (
        f"{detail_dasar} | Kategori: VIP ({self.fasilitas_vip}) + Rp"
        f" {self.biaya_layanan_vip:,}/hari"
    )

  # dua class ini adalah turunan dari superclass Mobil, di class MobilPenumpang nambahin atribut khusus yaitu jumlah_kursi dan ngelakuin overriding pada tampilkan_detail(). Di MobilMewah nambahin atribut khusus fasilitas+vip dan biaya_layanan_vip, serta ngelakuin overriding pada method hitung_biaya() dan tampikan_detail. Keduanya memakai super().__init__ untuk mewarisi property dan atribut dasar class Mobil. Atribut uniknya ada di class MobilPenumpang yaitu jumlah_kursi, class MobilMewah yaitu fasilitas_vip dan biaya_layanan_vip

  # Protected dan Private pada pewarisan, penggunaan atribut (_nama)
  class Mobil:

  def __init__(self, id_mobil, merk, model, plat_nomor, harga_sewa):
    #protected (_nama)
    # Diakses atau diturunkan langsung ke subclass (MobilPenumpang & MobilMewah)
    self._id_mobil = id_mobil
    self._merk = merk
    self._model = model
    self._harga_sewa_per_hari = harga_sewa

    #private (__nama)
    # rahasia hanya untuk class Mobil, subclass nggak bisa akses langsung
    self.__plat_nomor = plat_nomor
