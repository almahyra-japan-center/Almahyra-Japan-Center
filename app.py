import streamlit as st
st.set_page_config(page_title="ALMAHYRA JAPAN CENTER", layout="wide")
st.title("🇯🇵 ALMAHYRA JAPAN CENTER")
st.write("Selamat datang di lembaga bahasa jepang ALMAHYRA JAPAN CENTER🇯🇵")
st.success("yuk belajar bahasa jepang dari dasar bersama kami ! Bergabunglah jadi keluarga besar kami dan wujudkan mimpimu")

menu = st.sidebar.selectbox("Menu", ["Dashboard", "Data Siswa", "Keuangan"])
if menu == "Dashboard":

    st.header("profil ALMAHYRA JC")
