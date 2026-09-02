import streamlit as st
st.set_page_config(page_title="ALMAHYRA JAPAN CENTER", layout="wide")
st.title("🇯🇵 ALMAHYRA JAPAN CENTER PRO")
st.write("Selamat datang di Sistem Informasi LPK")
st.success("Web berhasil jalan! Ini versi awal")

menu = st.sidebar.selectbox("Menu", ["Dashboard", "Data Siswa", "Keuangan"])
if menu == "Dashboard":
    st.header("Dashboard Admin")
