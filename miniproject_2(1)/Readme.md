# Server Analyzer & Monitoring API (Prototype)

Backend monitoring dan manajemen server berbasis **Python** dan **SQLite** dengan arsitektur berlapis **`Database -> Logic -> API`**, dirancang untuk memisahkan tanggung jawab antara penyimpanan data, validasi/aturan bisnis, dan lapisan *endpoint* API.

## Arsitektur Proyek

Proyek ini disusun mengikuti alur berlapis agar mudah dirawat dan dikembangkan:

* **Database Layer (`database.py`)**: Mengelola inisialisasi tabel SQLite (`log_reg` dan `servers`), *seeding* akun awal `root` saat inisialisasi database, serta operasi *query* (pengecekan user, verifikasi kredensial, dan pengelolaan data server).
* **Logic Layer (`register.py`, `login.py`, serta modul proses server)**: Menangani validasi input, pengecekan duplikasi, pelemparan *custom exception*, dan alur proses sebelum data dikirim ke database atau dikembalikan ke API.
* **API Layer**: Menerima *request* dari klien, memanggil *logic* yang sesuai, dan mengatur hak akses peran (`root`, `admin`, `user`).

## Fitur & Alur Saat Ini

* **Inisialisasi Database & Akun `root`**:
  * Membuat tabel `log_reg` (`id`, `nama` unik, `password`, `role`) dan tabel data server (`servers`).
  * Melakukan *seeding* akun `root` secara aman (hanya dibuat jika belum ada) untuk menghindari *privilege escalation* pada pendaftaran publik.
* **Registrasi (`register.py`)**:
  * Validasi input username dan panjang minimal password.
  * Pengecekan duplikasi username sebelum penyimpanan.
  * Penetapan peran default `'user'` untuk akun yang didaftarkan melalui alur registrasi.
* **Autentikasi / Login (`login.py`)**:
  * Validasi input dasar dan verifikasi kredensial melalui lapisan database.
* **Manajemen Data Server (`servers`)**:
  * Perancangan penyimpanan informasi server (`server_id`, `ssh_port`, `status`) dengan validasi anti-duplikat dan nilai `status` default saat penambahan data.

## Rencana Pengembangan Selanjutnya

1. **Modul & Class Logic Server (`server_proc.py`)**
   * Membangun class/logic pengelolaan data server (`server_id`, `ssh_port`, `status`) dengan validasi input (tidak kosong, rentang port valid `1–65535`), pengecekan anti-duplikat, dan penetapan nilai `status` default saat penambahan data.
2. **Testing Lapisan Database & Logic**
   * Melakukan pengujian alur penuh sebelum masuk ke lapisan API: inisialisasi database & akun `root`, skenario registrasi (`valid`, `username` duplikat, `password` < 8 karakter), skenario login (`berhasil`, `input` kosong, kredensial salah), serta penambahan & pengecekan data server.
3. **Integrasi Lapisan API**
   * Menyambungkan seluruh logic (`register`, `login`, dan `server`) ke *endpoint* API (`POST` / `GET`), lengkap dengan pengaturan HTTP status code dan pengecekan hak akses berbasis `role` (`root`, `admin`, `user`).

## Catatan Penggunaan

1. Pastikan dependensi Python yang dibutuhkan sudah terpasang di *environment* aktif.
2. Jalankan inisialisasi database terlebih dahulu agar tabel dan akun awal `root` tersedia.
3. Sesuaikan nama file modul dan *custom exception* (`exception.py`) dengan struktur direktori lokalmu.