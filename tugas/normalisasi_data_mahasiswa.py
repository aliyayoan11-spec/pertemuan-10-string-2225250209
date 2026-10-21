def normalisasi_nama(nama):
    """Menghapus spasi berlebih dan mengubah ke format title case."""
    return " ".join(nama.strip().split()).title()

def buat_inisial(nama):
    """Membuat inisial dari huruf awal setiap kata."""
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)

def normalisasi_kode(kode):
    """Membersihkan kode kelas, ubah ke huruf besar, dan ganti spasi dengan tanda hubung."""
    kata = kode.strip().upper().split()
    return "-".join(kata)
def main():
    # Input dari pengguna
    nama = input("Nama: ")
    kode = input("Kode kelas: ")
    
    # Proses normalisasi dan perhitungan
    nama_bersih = normalisasi_nama(nama)
    kode_bersih = normalisasi_kode(kode)
    inisial = buat_inisial(nama)
    jumlah_kata = len(nama_bersih.split())
    
    # Tampilkan hasil secara rapi sesuai format
    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial : {inisial}")

if __name__ == "__main__":
    main()