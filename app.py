import streamlit as st
import os

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", layout="wide")

# Cek dulu file logonya ada apa nggak
NAMA_LOGO = "IMG-20260902-WA0000.jpg"
logo_ada = os.path.exists(NAMA_LOGO)

# Sidebar
st.sidebar.title("🇯🇵 AL MAHYRA JC")
if logo_ada:
    st.sidebar.image(NAMA_LOGO, use_column_width=True)
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Profil", "Visi & Misi", "Kontak"])

# BERANDA
if menu == "Beranda":
    if logo_ada:
        st.image(NAMA_LOGO, width=250)
    st.title("AL MAHYRA JAPAN CENTER")
    st.subheader("Lembaga Kursus Bahasa Jepang")
    st.markdown("### Yuk belajar bahasa jepang dari dasar bersama kami !")
    st.write("Bergabunglah jadi keluarga besar kami dan wujudkan mimpimu")
    st.success("Pendaftaran dibuka setiap awal bulan!")
    st.link_button("💬 Chat Admin WA", "https://wa.me/6287816094321")

# PROFIL
elif menu == "Profil":
    st.header("Profil AL MAHYRA JC")
    if logo_ada:
        st.image(NAMA_LOGO, width=150)
    st.write("AL MAHYRA JAPAN CENTER adalah lembaga kursus Bahasa Jepang yang fokus mengajarkan dari tingkat dasar N5 hingga tingkat lanjutan N1 dengan metode mudah, sistematis, dan menyenangkan.")
    st.write("Kami berlokasi di Desa Karangsari, Kec. Bulakamba, Kab. Brebes")

# VISI MISI
elif menu == "Visi & Misi":
    st.header("Visi & Misi")
    st.subheader("Visi")
    st.info("“Menjadi lembaga kursus Bahasa Jepang yang terpercaya dan berkualitas dalam membentuk generasi yang kompeten, berkarakter, dan siap meraih masa depan melalui penguasaan Bahasa Jepang.”")
    st.subheader("Misi")
    st.write("1. Menyelenggarakan pembelajaran Bahasa Jepang yang sistematis dan menyenangkan")
    st.write("2. Membek
