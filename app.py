import streamlit as st
st.set_page_config(page_title="ALMAHYRA JAPAN CENTER", layout="wide")
st.title("🇯🇵 ALMAHYRA JAPAN CENTER")
st.write("Selamat datang di Lembaga Bahasa Jepang ALMAHYRA JAPAN CENTER🇯🇵")
st.success("Yuk belajar bahasa jepang dari dasar bersama kami ! Bergabunglah jadi keluarga besar kami dan wujudkan mimpimu")

menu = st.sidebar.selectbox("Menu", ["Dashboard", "Data Siswa", "Keuangan"])
if menu == "Dashboard":

    st.header("Profil ALMAHYRA JC")
