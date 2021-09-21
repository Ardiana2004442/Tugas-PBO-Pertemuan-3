#kelas Volume Balok
class VolumeBalok :
    Panjang = None
    Lebar = None
    Tinggi = None

#membangun instance/variable sebagai "objek nyata"
VB = VolumeBalok()
VolumeBalok.Panjang = 8
VolumeBalok.Lebar = 13
VolumeBalok.Tinggi = 9

Hasil = VolumeBalok.Panjang*VolumeBalok.Lebar*VolumeBalok.Tinggi
#Output yang akan ditampilkan
print("Panjang Balok :", VolumeBalok.Panjang)
print("Lebar Balok :", VolumeBalok.Lebar)
print("Tinggi Balok :", VolumeBalok.Tinggi)
print("Hasil Volume Balok :", Hasil)