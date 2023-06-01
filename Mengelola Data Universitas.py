#Berfungsi untuk menghapus teks di terminal
import os

#Kelas Mahasiswa yang berfungsi sebagai media untuk menyimpan nama mahasiswa dan data yang berkaitan
class Mahasiswa:
    #Inisialisasi Atribut kelas ketika objek dari kelas Mahasiswa dibuat
    def __init__(self, nama, nim, jurusan ):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    #Menampilkan Informasi yang ada di dalam kelas Mahasiswa
    def info(self):
        print(f"""Nama Mahasiswa : {self.nama}
NIM Mahasiswa : {self.nim}
Jurusan Asal Mahasiswa : {self.jurusan}
              """)

#Kelas Jurusan yang berfungsi untuk menyimpan nama Jurusan dan menyimpan mahasiswa dari Jurusan yang bersangkutan
class Jurusan:
    #Inisialisasi Atribut ketika objek dari kelas Jurusan dibuat
    def __init__(self, nama):
        self.nama = nama
        self.DaftarMahasiswa = {}

    #Fungsi yang berguna untuk menambahkan mahasiswa ke dalam DaftarMahasiswa
    def tambah(self, mhswa, data):
        self.DaftarMahasiswa[mhswa] = Mahasiswa(data[0], data[1], data[2])
        print(f"{mhswa} berhasil ditambahkan ke jurusan {self.nama} !")

    #Fungsi yang berguna untuk menampilkan semua Mahasiswa yang ada didalam kelas Jurusan
    def info(self):
        strs = f"Daftar Mahasiswa Jurusan {self.nama} :\n"
        i = 1
        for x in self.DaftarMahasiswa:
            strs += (f"{i}. {x}\n")
            i += 1
        print(strs)

#Kelas Universitas, berguna untuk menyimpan nama Universitas dan berfungsi untuk menyimpan objek jurusan yang bersangkutan dengan Kelas Universitas yang dimaksud 
class Universitas:
    #Inisialisasi Atribut kelas ketika Objek dari kelas Universitas dibuat
    def __init__(self, nama):
        self.nama = nama
        self.DaftarJurusan = {}

    #Fungsi yang berguna untuk menambahkan objek jurusan ke dalam DaftarJurusan
    def tambah(self, jurusan):
        self.DaftarJurusan[jurusan] = Jurusan(jurusan)
        print(f"{jurusan} berhasil ditambahkan ke {self.nama} !")

    #Fungsi yang berguna untuk menampilkan semua jurusan yang ada di dalam Universitas yang bersangkutan
    def info(self):
        os.system('cls')
        strs = f"Daftar Jurusan di {self.nama} :\n"
        i = 1
        for x in self.DaftarJurusan:
            strs += (f"{i}. {x}\n")
            i += 1
        print(strs)

#Kelas yang berfungsi untuk memanajemen Informasi
class Manager:
    #Inisialisasi awal pada saat objek dari kelas Manager dibuat, memiliki atribut DaftarUniversitas
    def __init__(self):
        self.DaftarUniversitas = {}

    #Menampilkan semua Universitas yang pernah dimasukkan pengguna
    def Tampilkan_Universitas(self):
        strs = f"Daftar DaftarUniversitas yang Tersedia :\n"
        i = 1
        for x in self.DaftarUniversitas:
            strs += (f"{i}. {x}\n")
            i += 1
        print(strs)

    #Menampilkan semua Jurusan yang ada di Universitas yang dimasukkan Pengguna
    def Tampilkan_Jurusan(self, uni):
        try:
            self.DaftarUniversitas[uni].info()
        except(KeyError):
            print("Nama Universitas Belum Pernah Disimpan Sebelumnya!")
    
    #Menampilkan semua Mahasiswa Yang ada di dalam Universitas dan Jurusan yang dimasukkan pengguna
    def Tampilkan_Mahasiswa(self, uni, jur):
        try:
            self.DaftarUniversitas[uni].DaftarJurusan[jur].info()
        except(KeyError):
            print("Nama Universitas atau Jurusan Belum Pernah Disimpan Sebelumnya!")
    
    #Menampilkan Informasi Mahasiswa yang tersimpan
    def Info_Mahasiswa(self, mhs):
        for x in self.DaftarUniversitas:
            for y in self.DaftarUniversitas[x].DaftarJurusan:
                for z in self.DaftarUniversitas[x].DaftarJurusan[y].DaftarMahasiswa:
                    if z.lower() == mhs.lower():
                        print(f"Mahasiswa {z} berasal dari Universitas {x} dan memiliki informasi berikut : ")
                        self.DaftarUniversitas[x].DaftarJurusan[y].DaftarMahasiswa[z].info()
                        return
        print("Mahasiswa Tidak Ditemukan di Universitas Manapun!")
    
    #Fungsi yang berguna untuk menambahkan objek Universitas ke dalam DaftarUniversitas
    def Tambah_Universitas(self, uni):
        self.DaftarUniversitas[uni] = Universitas(uni)
        print(f"{uni} berhasil ditambahkan ke dalam Program!")
    
    #Fungsi yang berguna untuk menambahkan objek Jurusan ke dalam Universitas yang diinginkan Pengguna
    def Tambah_Jurusan(self, uni, jur):
        self.DaftarUniversitas[uni].tambah(jur)
    
    #Fungsi yang berguna untuk menambahkan objek mahasiswa ke dalam objek Jurusan di dalam Universitas yang diinginkan Pengguna
    def Tambah_Mahasiswa(self, uni, jur, mhswa, data):
        self.DaftarUniversitas[uni].DaftarJurusan[jur].tambah(mhswa, data)

    #Fungsi untuk menjalankan perintah yang dimasukkan oleh pengguna
    def Run(self, cmnd):
        daftarPerintah = ["Tampilkan_Universitas()", "Tampilkan_Jurusan()",
                          "Tampilkan_Mahasiswa()", "Info_Mahasiswa()",
                          "Tambah_Universitas()", "Tambah_Jurusan()",
                          "Tambah_Mahasiswa()"]
        os.system('cls')
        if not cmnd in daftarPerintah:
            print("Perintah tidak Valid!")
        if (cmnd == "Tampilkan_Universitas()"):
            self.Tampilkan_Universitas()
        elif (cmnd == "Tampilkan_Jurusan()"):
            uni = input("Masukkan Universitas asal Jurusan Berada : ")
            self.Tampilkan_Jurusan(uni)
        elif (cmnd == "Tampilkan_Mahasiswa()"):
            uni = input("Masukkan Universitas asal Mahasiswa : ")
            jur = input("Masukkan Jurusan Asal Mahasiswa : ")
            self.Tampilkan_Mahasiswa(uni, jur)
        elif (cmnd == "Info_Mahasiswa()"):
            mhs = input("Masukkan nama Mahasiswa : ")
            self.Info_Mahasiswa(mhs)
        elif (cmnd == "Tambah_Universitas()"):
            uni = input("Masukkan nama Universitas : ")
            self.Tambah_Universitas(uni)
        elif (cmnd == "Tambah_Jurusan()"):
            uni = input("Masukkan nama Universitas : ")
            jur = input("Masukkan nama Jurusan : ")
            self.Tambah_Jurusan(uni, jur)
        elif (cmnd == "Tambah_Mahasiswa()"):
            nama = input("Masukkan Nama Mahasiswa : ")
            nim = input("Masukkan NIM Mahasiswa : ")
            jur = input("Masukkan Jurusan Mahasiswa : ")
            uni = input("Masukkan Universitas Asal Mahasiswa : ")
            data = [nama, nim, jur]
            self.Tambah_Mahasiswa(uni, jur, nama, data)

#Fungsi yang berguna untuk memenuhi pertanyaan soal
def Default(Executor):
    #Membuat Objek XYZ University.
    Executor.Tambah_Universitas("XYZ University")

    #Membuat Objek Teknik Informatike kemudian memasukkannya ke dalam Objek XYZ University.
    Executor.Tambah_Jurusan("XYZ University", "Teknik Informatika")

    #Menambahkan Mahasiswa Alif Nurhidayat Ke Dalam XYZ University
    Executor.Tambah_Mahasiswa("XYZ University", "Teknik Informatika", "ALIF NURHIDAYAT",
                              ["ALIF NURHIDAYAT", "G1A022073", "Teknik Informatika"])
    
    #Menampilkan Daftar Jurusan yang ada di XYZ University.
    Executor.Tampilkan_Jurusan("XYZ University")

    #Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di XYZ University.
    Executor.Tampilkan_Mahasiswa("XYZ University", "Teknik Informatika")

#Fungsi yang berguna sebagai media interaksi dengan Pengguna
def main():
    Executor = Manager()
    Default(Executor)
    first = False
    while True:
        help = """Perintah yang tersedia:
Tampilkan_Universitas(), Tampilkan_Jurusan(),
Tampilkan_Mahasiswa(), Info_Mahasiswa(),
Tambah_Universitas(), Tambah_Jurusan(),
Tambah_Mahasiswa()"""
        if not first:
            print("Selamat Datang Di Program Manajemen Data Universitas")
            first = True
        print("\nKetik 'bantuan' untuk melihat perintah yang tersedia!")
        cmnd = input("Ketikkan Perintah : ")
        if cmnd.lower() == "bantuan":
            os.system('cls')
            print(help)
            continue
        Executor.Run(cmnd)

#Percabangan if yang berguna agar ketika file ini diimpor sebagai modul, program dari fungsi main() tidak ada berjalan.
#Atau, dengan kata lain, program hanya akan berjalan jika file ini yang dieksekusi pertama.
if __name__ == "__main__":
    main()