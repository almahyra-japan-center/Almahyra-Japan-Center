import streamlit as st

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="AL MAHYRA JAPAN CENTER",
    page_icon="🎌",
    layout="wide"
)

# GANTI NOMOR WA ADMIN KAMU DISINI
NO_WA_ADMIN = "6281234567890" 

# MENU SIDEBAR
st.sidebar.title("🎌 AL MAHYRA JC")
menu = st.sidebar.radio(
    "Menu",
    ["Beranda", "Program", "Pendaftaran", "Kontak"]
)

# HALAMAN BERANDA
if menu == "Beranda":
    st.header("Selamat Datang di AL MAHYRA JAPAN CENTER")
    st.write("Tempat kursus Bahasa Jepang & Persiapan Kerja ke Jepang")
    st.image("https://placehold.co/800x300/FF0000/FFFFFF?text=AL+MAHYRA+JC", use_column_width=True)

# HALAMAN PROGRAM
elif menu == "Program":
    st.header("📚 Program Kami")
    st.write("1. Kelas Bahasa Jepang N5 - N1")
    st.write("2. Program Pemagangan / TG")
    st.write("3. Kelas Persiapan JLPT & SSW")

# HALAMAN PENDAFTARAN - INI YG PENTING
elif menu == "Pendaftaran":
    st.header("📝 Pendaftaran AL MAHYRA JC")
    st.write("Klik tombol di bawah ini untuk mengisi formulir pendaftaran")
    
    # TOMBOL 1: KE GOOGLE FORM
    st.link_button(
        label="📋 KLIK DISINI UNTUK DAFTAR", 
        url="https://forms.gle/gQ4QZz8yGmmTUc8y5", 
        type="primary",
        use_container_width=True
    )
    
    st.markdown("---")
    
    # TOMBOL 2: KONFIRMASI WA
    pesan_wa = "Halo Admin AL MAHYRA JC, saya baru saja mengisi formulir pendaftaran online."
    link_wa = f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}"
    st.link_button(
        label="📲 KONFIRMASI VIA WA ADMIN", 
        url=link_wa, 
        type="primary",
        use_container_width=True
    )
    
    st.info("Setelah isi form, jangan lupa konfirmasi ke WA Admin ya")

# HALAMAN KONTAK
elif menu == "Kontak":
    st.header("📞 Hubungi Kami")
    st.write(f"WhatsApp Admin: {NO_WA_ADMIN}")
    st.write("Alamat: Semarang, Jawa Tengah")
