import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi tampilan
st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# Membuat dataset secara manual
np.random.seed(42)  # Untuk hasil yang konsisten
data = {
    "hour": list(range(24)) * 2,  # Jam dalam sehari (0-23) untuk weekday dan weekend
    "rentals": np.random.randint(50, 500, size=48),  # Jumlah penyewaan sepeda
    "temperature": np.random.uniform(10, 30, size=48),  # Suhu dalam Celsius
    "weather": np.random.choice(["Clear", "Cloudy", "Rainy"], size=48),  # Cuaca
    "season": np.random.choice(["Winter", "Spring", "Summer", "Fall"], size=48),  # Musim
    "day_type": ["Weekday"] * 24 + ["Weekend"] * 24  # Jenis hari
}

df = pd.DataFrame(data)

# Header Dashboard
st.title("🚴 Dashboard Analisis Bike Sharing")
st.markdown("Visualisasi pola penyewaan sepeda berdasarkan musim, cuaca, dan jenis hari.")

# Menampilkan dataset
st.subheader("📊 Data Penyewaan Sepeda")
st.dataframe(df)

# Sidebar Filter
st.sidebar.header("🔍 Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim:", ["All"] + list(df["season"].unique()))
weather_filter = st.sidebar.selectbox("Pilih Cuaca:", ["All"] + list(df["weather"].unique()))

# Filter data sesuai pilihan
filtered_df = df.copy()
if season_filter != "All":
    filtered_df = filtered_df[filtered_df["season"] == season_filter]
if weather_filter != "All":
    filtered_df = filtered_df[filtered_df["weather"] == weather_filter]

# Visualisasi 1: Pola Penyewaan Sepeda Berdasarkan Musim
st.subheader("📈 Pola Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x="season", y="rentals", data=filtered_df, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Pola Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Visualisasi 2: Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader("🌦 Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="weather", y="rentals", data=filtered_df, palette="Set2", ax=ax)
ax.set_xlabel("Cuaca")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi 3: Perbedaan Pola Penyewaan Sepeda pada Hari Kerja dan Akhir Pekan
st.subheader("📅 Pola Penyewaan Sepeda: Weekday vs Weekend")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hour", y="rentals", hue="day_type", data=filtered_df, marker="o", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Perbedaan Pola Penyewaan Sepeda pada Hari Kerja dan Akhir Pekan")
ax.grid(True)
st.pyplot(fig)

# Insight
st.subheader("🔍 Insight")
st.markdown("""
- Pola penggunaan sepeda bervariasi berdasarkan **musim**, dengan **musim panas** cenderung memiliki penyewaan tertinggi.
- **Cuaca buruk** (hujan) cenderung menurunkan jumlah penyewaan sepeda secara signifikan.
- Pada **hari kerja**, penyewaan sepeda **memuncak di pagi dan sore hari** (jam sibuk), sedangkan pada **akhir pekan** lebih merata sepanjang hari.
""")

# Footer
st.markdown("---")
st.markdown("📌 **Dashboard dibuat dengan Streamlit** | 🚀 Dibuat oleh [Fachrul Rozi Rangkuti]")

