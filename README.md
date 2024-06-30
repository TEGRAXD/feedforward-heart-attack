# Heart Attack Prediction (Deep Feedforward)

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Deep Learning Feedforward (Regresion). Adapun model yang digunakan merupakan model untuk memprediksi persentase serangan jantung berdasarkan:

-   `age` atau usia dengan tipe data integer (bilangan bulat)
-   `sex` atau jenis kelamin pasien (0: perempuan, 1: laki-laki)
-   `cp` atau jenis nyeri dada (0: Typical angina, 1: Atypical angina, 2: Non-anginal pain, 3: Asymptomatic)
-   `trtbps` atau tekanan darah saat istirahat (dalam mmHg)
-   `chol` atau kadar kolesterol dalam mg/dL
-   `fbs` atau gula darah puasa > 120 mg/dl (1 = benar, 0 = salah) 
-   `thalachh` atau detak jantung maksimal yang dicapai

## Folder, file, dan kegunaannya

-   templates/
    -   index.html --> Berisi template website
-   app.py --> Berisi konfigurasi route dan program utama
-   heart_attack_model.keras --> Model feedforward (regresi) yang sudah di-training
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Regresi Linier

## Cara menjalankan program pada komputer Anda

### Menjalankan program

1. Buka terminal/command prompt/power shell
2. Buat virtual environment dengan\
   `python -m venv <nama-environment>`
3. Aktifkan virtual environment dengan\
   `<path\to\your\project>\<nama-environment>\Scripts\activate`
4. Install semua dependency/package Python dengan\
   `pip install -r requirements.txt`
5. Jalankan program menggunakan perintah\
   `python app.py`

### Akses melalui Website

Setelah program berjalan:

1. Anda akan diberikan URL untuk membuka website berupa `localhost:5000/` atau `127.0.0.1:5000/`
1. Buka URL dengan browser, coba masukkan data yang ingin di prediksi
1. Anda akan diberikan prediksi serangan jantung pada bagian output halaman website