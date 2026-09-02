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

# HALAMAN PROGRAM
elif menu == "Program":
    st.header("📚 Program Kami")
    st.write("1. Kelas Bahasa Jepang N5 - N1")
    st.write("2. Program Pemagangan / TG")
    st.write("3. Kelas Persiapan JLPT & SSW")

# HALAMAN PENDAFTARAN - VERSI AMAN
elif menu == "Pendaftaran":
    st.header("📝 Pendaftaran AL MAHYRA JC")
    st.write("Klik link di bawah ini untuk mengisi formulir pendaftaran")
    
    # TOMBOL 1: KE GOOGLE FORM PAKE MARKDOWN
    st.markdown("""
    <a href="https://forms.gle/gQ4QZz8yGmmTUc8y5" target="_blank">
        <button style="background-color:#FF4B4B;color:white;padding:14px 20px;border:none;border-radius:8px;width:100%;font-size:16px;cursor:pointer;">
        📋 KLIK DISINI UNTUK DAFTAR
        </button>
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # TOMBOL 2: KONFIRMASI WA
    pesan_wa = "Halo Admin AL MAHYRA JC, saya baru saja mengisi formulir pendaftaran online."
    link_wa = f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}"
    st.markdown(f"""
    <a href="{link_wa}" target="_blank">
        <button style="background-color:#25D366;color:white;padding:14px 20px;border:none;border-radius:8px;width:100%;font-size:16px;cursor:pointer;">
        📲 KONFIRMASI VIA WA ADMIN
        </button>
    </a>
    """, unsafe_allow_html=True)
    
    st.info("Setelah isi form, jangan lupa konfirmasi ke WA Admin ya")

# HALAMAN KONTAK
elif menu == "Kontak":
    st.header("📞 Hubungi Kami")
    st.write(f"WhatsApp Admin: {NO_WA_ADMIN}")
    st.write("Alamat: Brebes, Jawa Tengah")
