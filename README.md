# Projek-Analisis-Data
Projek course Analisis data dengan pyhton

# Dashboard Penyewaan Sepeda Menggunakan Streamlit

## Deskripsi
Dashboard ini dibuat untuk menganalisis data penyewaan sepeda dengan menggunakan Streamlit. Visualisasi yang ditampilkan mencakup penyewaan berdasarkan musim, perbandingan antara hari kerja dan akhir pekan, serta pengaruh suhu terhadap penyewaan sepeda.

## 1️⃣ Install Streamlit dan Library Pendukung
Jalankan perintah berikut untuk menginstal Streamlit dan library yang diperlukan:
```python
!pip install streamlit pandas plotly
```

## 2️⃣ Upload Dataset day.csv dan hour.csv
Mengunggah dataset ke Google Colab terlebih dahulu.
```
from google.colab import files

uploaded = files.upload()
```

## 3️⃣ Buat File app.py untuk Streamlit
Membuat file aplikasi Streamlit dengan app.py
```
%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px


day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')


season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
day_df['season_name'] = day_df['season'].map(season_map)


st.title("Dashboard Bike Sharing")

# 1️⃣ Grafik: Penyewaan Sepeda Berdasarkan Musim
st.subheader("Total Penyewaan Sepeda Berdasarkan Musim")
season_rentals = day_df.groupby('season_name')['cnt'].sum().reset_index()
fig1 = px.bar(season_rentals, x='season_name', y='cnt', 
              labels={'season_name': 'Musim', 'cnt': 'Total Penyewaan'},
              color='season_name')
st.plotly_chart(fig1)

# 2️⃣ Grafik: Perbandingan Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan
st.subheader("Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan")
day_df['day_type'] = day_df['weekday'].apply(lambda x: 'Weekday' if x < 5 else 'Weekend')
day_type_rentals = day_df.groupby('day_type')['cnt'].mean().reset_index()
fig2 = px.bar(day_type_rentals, x='day_type', y='cnt', 
              labels={'day_type': 'Jenis Hari', 'cnt': 'Rata-rata Penyewaan'},
              color='day_type')
st.plotly_chart(fig2)

# 3️⃣ Grafik: Korelasi Cuaca dengan Penyewaan Sepeda
st.subheader("Pengaruh Suhu terhadap Penyewaan Sepeda")
fig3 = px.scatter(day_df, x='temp', y='cnt', color='season_name', 
                  labels={'temp': 'Temperatur (Normalisasi)', 'cnt': 'Jumlah Penyewaan'},
                  title="Hubungan Suhu dan Penyewaan Sepeda")
st.plotly_chart(fig3)
```

## 4️⃣ Jalankan Dashboard Streamlit di Colab
Setelah kode di atas dieksekusi, dijalankan perintah ini untuk menjalankan Streamlit dan mendapatkan URL dashboard
```
!streamlit run app.py & npx localtunnel --port 8501
```
