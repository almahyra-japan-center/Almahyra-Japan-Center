import streamlit as st

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", layout="wide", page_icon="logo.png")

# Sidebar pakai logo
st.sidebar.image("logo.png", use_column_width=True)
st.sidebar.title("AL MAHYRA JC")
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Profil", "Visi & Misi", "Kontak"])

if menu == "Beranda":
    st.image("logo.png", width=250) # Logo besar di tengah
    st.title("AL MAHYRA JAPAN CENTER")
    st.write("Lembaga Kursus Bahasa Jepang")
    st.markdown("### Yuk belajar bahasa jepang dari dasar bersama kami !")
    st.write("Bergabunglah jadi keluarga besar kami dan wujudkan mimpimu")
    st.success("Pendaftaran dibuka setiap awal bulan!")
    
    st.markdown("### Kelas yang tersedia:")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("N5", "Dasar")
    with col2: st.metric("N4", "Menengah") 
    with col3: st.metric("N3-N1", "Lanjutan")
    
    st.link_button("💬 Chat Admin WA", "https://wa.me/6287816094321")

elif menu == "Profil":
    st.header("Profil AL MAHYRA JC")
    st.image("logo.png", width=150)
    st.write("AL MAHYRA JAPAN CENTER adalah lembaga kursus Bahasa Jepang yang fokus mengajarkan dari tingkat dasar N5 hingga tingkat lanjutan N1 dengan metode mudah, sistematis, dan menyenangkan.")
    st.write("Kami berlokasi di rumah di Desa Karangsari, Kec. Bulakamba, Kab. Brebes")

elif menu == "Visi & Misi":
    st.header("Visi & Misi")
    st.subheader("Visi")
    st.info("“Menjadi lembaga kursus Bahasa Jepang yang terpercaya dan berkualitas dalam membentuk generasi yang kompeten, berkarakter, dan siap meraih masa depan melalui penguasaan Bahasa Jepang.”")
    st.subheader("Misi")
    for i in range(1,8):
        st.write(f"{i}. Misi nomor {i}") # isi lengkapnya sesuai yg kmrn ya

elif menu == "Kontak":
    st.header("Informasi Kontak")
    st.image("logo.png", width=120)
    st.write("📍 **Alamat**: Desa Karangsari RT 005/01, Kec. Bulakamba, Kab. Brebes")
    st.write("📞 **WhatsApp Admin**: 0878-1609-4321")
    st.write("📅 **Pendaftaran**: Dibuka setiap awal bulan")
    st.link_button("💬 Chat Sekarang", "https://wa.me/6287816094321")
