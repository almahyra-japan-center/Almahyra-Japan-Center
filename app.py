import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", layout="wide")

NAMA_LOGO = "logo.png"

st.sidebar.title("🇯🇵 AL MAHYRA JC")
try:
    st.sidebar.image(NAMA_LOGO, use_container_width=True)
except:
    pass 
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Tentang Kami", "Jadwal & Biaya", "Pendaftaran", "Kontak"])

if menu == "Beranda":
    try:
        st.image(NAMA_LOGO, width=250)
    except:
        pass
    st.title("AL MAHYRA JAPAN CENTER")
    st.subheader("Lembaga Kursus Bahasa Jepang")
    st.markdown("### Yuk belajar bahasa jepang dari dasar bersama kami!")
    st.write("Bergabunglah jadi keluarga besar kami dan wujudkan mimpimu ke Jepang")
    st.success("🔥 Pendaftaran Gelombang Oktober 2026 Dibuka!")
    st.link_button("💬 Chat Admin WA", "https://wa.me/6287816094321")

elif menu == "Tentang Kami":
    st.header("Tentang AL MAHYRA JAPAN CENTER")
    try:
        st.image(NAMA_LOGO, width=150)
    except:
        pass
    
    st.subheader("Profil")
    st.write("AL MAHYRA JAPAN CENTER adalah lembaga kursus Bahasa Jepang yang fokus mengajarkan dari tingkat dasar N5 hingga tingkat lanjutan N1 dengan metode mudah, sistematis, dan menyenangkan.")
    st.write("Kami berlokasi di Desa Karangsari, Kec. Bulakamba, Kab. Brebes")
    
    st.divider()
    
    st.subheader("Visi")
    st.info("Menjadi lembaga kursus Bahasa Jepang yang terpercaya dan berkualitas dalam membentuk generasi yang kompeten, berkarakter, dan siap meraih masa depan melalui penguasaan Bahasa Jepang.")
    
    st.subheader("Misi")
    st.write("1. Menyelenggarakan pembelajaran Bahasa Jepang yang sistematis dan menyenangkan")
    st.write("2. Membekali peserta dengan kemampuan bahasa untuk studi, kerja, dan budaya Jepang")
    st.write("3. Menumbuhkan semangat disiplin, kerja keras, dan rasa tanggung jawab")

# ... bagian Jadwal, Pendaftaran, Kontak tetep sama kayak kode sebelumnya ...
