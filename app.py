import streamlit as st

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", layout="wide")

NAMA_LOGO = "logo.png"

st.sidebar.title("🇯🇵 AL MAHYRA JC")
try:
    st.sidebar.image(NAMA_LOGO, use_container_width=True) # <-- yg bener ini
except:
    pass # kalau logo error, di skip aja

menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Profil", "Visi & Misi", "Kontak"])

if menu == "Beranda":
    try:
        st.image(NAMA_LOGO, width=250)
    except:
        pass
    st.title("AL MAHYRA JAPAN CENTER")
    st.subheader("Lembaga Kursus Bahasa Jepang")
    st.markdown("### Yuk belajar bahasa jepang dari dasar bersama kami!")
    st.write("Bergabunglah jadi keluarga besar kami dan wujudkan mimpimu")
    st.success("Pendaftaran dibuka setiap awal bulan!")
    st.link_button("💬 Chat Admin WA", "https://wa.me/6287816094321")

elif menu == "Profil":
    st.header("Profil AL MAHYRA JC")
    try:
        st.image(NAMA_LOGO, width=150)
    except:
        pass
    st.write("AL MAHYRA JAPAN CENTER adalah lembaga kursus Bahasa Jepang yang fokus mengajarkan dari tingkat dasar N5 hingga tingkat lanjutan N1 dengan metode mudah, sistematis, dan menyenangkan.")

elif menu == "Visi & Misi":
    st.header("Visi & Misi")
    st.subheader("Visi")
    st.info("Menjadi lembaga kursus Bahasa Jepang yang terpercaya dan berkualitas dalam membentuk generasi yang kompeten, berkarakter, dan siap meraih masa depan melalui penguasaan Bahasa Jepang.")
    st.subheader("Misi")
    st.write("1. Menyelenggarakan pembelajaran Bahasa Jepang yang sistematis dan menyenangkan")
    st.write("2. Membekali peserta dengan kemampuan bahasa untuk studi, kerja, dan budaya Jepang")
    st.write("3. Menumbuhkan semangat disiplin, kerja keras, dan rasa tanggung jawab")
    st.write("4. Menjalin kerja sama dengan lembaga di Jepang")

elif menu == "Kontak":
    st.header("Informasi Kontak")
    try:
        st.image(NAMA_LOGO, width=120)
    except:
        pass
    st.write("📍 **Alamat**: Desa Karangsari RT 005/01, Kec. Bulakamba, Kab. Brebes")
    st.write("📞 **WhatsApp Admin**: 0878-1609-4321")
    st.write("📅 **Pendaftaran**: Dibuka setiap awal bulan")
    st.link_button("💬 Chat Sekarang", "https://wa.me/6287816094321")
