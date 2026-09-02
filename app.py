import streamlit as st

st.set_page_config(page_title="ALMAHYRA JAPAN CENTER", layout="wide")

st.sidebar.title("🇯🇵 ALMAHYRA JC")
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Profil", "Visi & Misi", "Kontak"])

if menu == "Beranda":
    st.title("🇯🇵 ALMAHYRA JAPAN CENTER")
    st.write("Selamat datang di Lembaga Bahasa Jepang ALMAHYRA JAPAN CENTER")
    st.write("")
    st.markdown("### Yuk belajar bahasa jepang dari dasar bersama kami !")
    st.write("Bergabunglah jadi keluarga besar kami dan wujudkan mimpimu")
    st.success("Pendaftaran dibuka setiap awal bulan!")

elif menu == "Profil":
    st.header("Profil ALMAHYRA JC")
    st.write("ALMAHYRA JAPAN CENTER adalah lembaga kursus Bahasa Jepang yang fokus mengajarkan dari tingkat dasar N5 hingga tingkat lanjutan N1 dengan metode mudah, sistematis, dan menyenangkan.")
    st.write("Kami berlokasi di rumah di Desa Karangsari, Kec. Bulakamba, Kab. Brebes")

elif menu == "Visi & Misi":
    st.header("Visi & Misi")
    st.subheader("Visi")
    st.info("“Menjadi lembaga kursus Bahasa Jepang yang terpercaya dan berkualitas dalam membentuk generasi yang kompeten, berkarakter, dan siap meraih masa depan melalui penguasaan Bahasa Jepang.”")
    st.subheader("Misi")
    st.write("1. Menyelenggarakan pembelajaran Bahasa Jepang yang berkualitas")
    st.write("2. Meningkatkan kemampuan berbahasa Jepang: membaca, menulis, mendengar, berbicara")
    st.write("3. Membentuk peserta didik yang disiplin, percaya diri, bertanggung jawab")
    st.write("4. Mengenalkan budaya dan etika masyarakat Jepang")
    st.write("5. Mempersiapkan peserta didik untuk pendidikan/kerja di Jepang")
    st.write("6. Menciptakan lingkungan belajar yang nyaman dan menyenangkan")
    st.write("7. Memberikan pendampingan dan motivasi")

elif menu == "Kontak":
    st.header("Informasi Kontak")
    st.write("📍 **Alamat**: Desa Karangsari RT 005/01, Kec. Bulakamba, Kab. Brebes")
    st.write("📞 **WhatsApp Admin**: 0878-1609-4321")
