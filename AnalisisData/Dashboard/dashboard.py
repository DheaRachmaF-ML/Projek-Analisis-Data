# -*- coding: utf-8 -*-
"""Dashboard

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mxbQ5rzqjzZ4Tx5K4BiLbbDNWWhKs5Hb
"""

!pip install streamlit pandas plotly

from google.colab import files

uploaded = files.upload()

from google.colab import files

uploaded = files.upload()

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# 
# 
# day_df = pd.read_csv('day.csv')
# hour_df = pd.read_csv('hour.csv')
# 
# 
# season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
# day_df['season_name'] = day_df['season'].map(season_map)
# 
# 
# st.title("Dashboard Bike Sharing")
# 
# st.subheader("Total Penyewaan Sepeda Berdasarkan Musim")
# season_rentals = day_df.groupby('season_name')['cnt'].sum().reset_index()
# fig1 = px.bar(season_rentals, x='season_name', y='cnt',
#               labels={'season_name': 'Musim', 'cnt': 'Total Penyewaan'},
#               color='season_name')
# st.plotly_chart(fig1)
# 
# 
# st.subheader("Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan")
# day_df['day_type'] = day_df['weekday'].apply(lambda x: 'Weekday' if x < 5 else 'Weekend')
# day_type_rentals = day_df.groupby('day_type')['cnt'].mean().reset_index()
# fig2 = px.bar(day_type_rentals, x='day_type', y='cnt',
#               labels={'day_type': 'Jenis Hari', 'cnt': 'Rata-rata Penyewaan'},
#               color='day_type')
# st.plotly_chart(fig2)
# 
# 
# st.subheader("Pengaruh Suhu terhadap Penyewaan Sepeda")
# fig3 = px.scatter(day_df, x='temp', y='cnt', color='season_name',
#                   labels={'temp': 'Temperatur (Normalisasi)', 'cnt': 'Jumlah Penyewaan'},
#                   title="Hubungan Suhu dan Penyewaan Sepeda")
# st.plotly_chart(fig3)
#

!streamlit run app.py & npx localtunnel --port 8501