# 🚴 Proyek DBS: Analisis Bike Sharing Dataset
Proyek ini dibuat untuk memenuhi sub-mission Coding Camp by DBS Foundation 2025. Proyek ini bertujuan untuk analisis data penyewaan sepeda untuk memahami pola penggunaan berdasarkan musim, cuaca, dan waktu.

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis tren penyewaan sepeda menggunakan dataset Bike Sharing. Analisis dilakukan untuk:
- [x] Memahami pola penyewaan berdasarkan musim & cuaca
- [x] Mengidentifikasi jam sibuk penyewaan sepeda
- [x] Membuat heatmap lokasi penyewaan tertinggi
- [x] Segmentasi pengguna menggunakan RFM Analysis
- [x] Deploy dashboard interaktif dengan Streamlit

## 🧑‍💻 Teknik Analisis yang Digunakan
### 📌 1️⃣ RFM Analysis (Segmentasi Pengguna)
- Mengelompokkan pengguna berdasarkan pola penyewaan:
- Recency → Seberapa lama sejak terakhir kali menyewa
- Frequency → Seberapa sering pelanggan menyewa sepeda
- Monetary → Berapa banyak sepeda yang disewa
### 📌 2️⃣ Geospatial Analysis (Heatmap Lokasi Penyewaan)
- Menampilkan lokasi penyewaan dengan intensitas tertinggi.
### 📌 3️⃣ Clustering Penyewaan Sepeda
- Mengelompokkan jumlah penyewaan ke dalam kategori rendah, sedang, tinggi.

## 🚀 Cara Menjalankan Proyek
### 1️⃣ Clone Repository
```
git clone https://github.com/Rozii23/Proyek_DBS_Analisis_Bike_Sharing_Dataset.git
cd Proyek_DBS_Analisis_Bike_Sharing_Dataset
```
### 2️⃣ Instalasi Dependensi
```
pip install -r requirements.txt
```
### 3️⃣ Jalankan Dashboard
```
streamlit run Dashboard/dashboard.py
```
Aplikasi akan terbuka di browser secara otomatis.

## 🌐 Live Dashboard
🚀 Coba di sini 👉 [Bike Sharing Dashboard](https://upwtwuklplszpiqod8kjwl.streamlit.app/)

## 📜 *Kesimpulan*
- [x] Penyewaan tertinggi terjadi pada musim panas
- [x] Cuaca buruk berdampak negatif pada penyewaan
- [x] Puncak penyewaan terjadi pada jam kerja (pagi & sore)
- [x] Pelanggan dengan Frequency tinggi adalah pelanggan loyal
- [x] Stasiun pusat kota memiliki jumlah penyewaan tertinggi

🚀 Dengan analisis ini, dapat dioptimalkan strategi penempatan sepeda dan harga sewa berdasarkan musim & cuaca.
