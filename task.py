class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

# Membuat objek mahasiswa
mhs1 = Mahasiswa("Vika Aidila Adhari", "A", "Pendidikan Komputer", "Keguruan", "Samarinda", "Tenggarong")

# Menampilkan nilai atribut objek
print("Informasi Mahasiswa:")
print("Nama:", mhs1.nama) 
print("Kelas:", mhs1.kelas) 
print("Prodi:", mhs1.prodi)  
print("Fakultas:", mhs1.fakultas)
print("Tempat Tinggal:", mhs1.tempat_tinggal)  
print("Asal:", mhs1.asal)  


        

