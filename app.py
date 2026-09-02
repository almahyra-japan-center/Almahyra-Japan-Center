import streamlit as st

st.set_page_config(
    page_title="AL MAHYRA JAPAN CENTER",
    page_icon="🎌",
    layout="wide"
)

# === DATA KAMU ===
NO_WA_ADMIN = "6281234567890"  # GANTI KE NOMOR KAMU
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"  # GANTI KE LINK FORM KAMU
# =================

# MENU KIRI
with st.sidebar:
    st.title("🎌 AL MAHYRA JC")
    menu = st.radio("Menu", ["Beranda", "Program", "Pendaftaran", "Kontak"])

# ISI KANAN
if menu == "Beranda":
    
    # 1. LOGO KAMU - INI SUDAH BENER
    st.image("logo.png", use_container_width=True)
    
    # 2. SAMBUTAN HANGAT
    st.header("Selamat Datang! 👋")
    st.write("Terima kasih sudah berkunjung ke website resmi kami.")
    
    # 3. AJAKAN SINGKAT
    st.subheader("Wujudkan Mimpimu Bekerja & Kuliah ke Jepang Bersama Kami")
    st.write("Belajar Bahasa Jepang dengan metode santai, cepat paham, dan dibimbing sampai lulus JLPT.")
    st.divider()

    # 4. PROFIL LEMBAGA
    st.subheader("🏢 Profil Lembaga")
    st.write("**AL MAHYRA JAPAN CENTER** adalah lembaga kursus Bahasa Jepang yang berfokus pada persiapan kerja, magang, dan kuliah ke Jepang. Kami berlokasi di Semarang dan juga membuka kelas online untuk seluruh Indonesia.")
    
    # 5. VISI MISI
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🎯 Visi**")
        st.write("Menjadi pusat kursus Bahasa Jepang terpercaya yang melahirkan SDM siap kerja di Jepang.")
    with col2:
        st.markdown("**🚀 Misi**")
        st.write("1. Memberi pengajaran berkualitas\n2. Membimbing sampai lulus JLPT\n3. Menyalurkan ke perusahaan Jepang")
    
    st.divider()

    # 6. ALAMAT KECIL
    st.caption("📍 Alamat: Brebes, Jawa Tengah, Indonesia")

    # 7. PENDAFTARAN
    st.subheader("📝 Pendaftaran Dibuka!")
    st.markdown(f'<a href="{LINK_GOOGLE_FORM}" target="_blank"><button style="background-color:#FF4B4B;color:white;padding:14px 20px;border:none;border-radius:8px;width:100%;font-size:16px;cursor:pointer;">KLIK UNTUK DAFTAR ONLINE</button></a>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 8. KONTAK
    st.subheader("📞 Hubungi Admin")
    pesan_wa = "Halo%20Admin%20AL%20MAHYRA%20JC,%20saya%20ingin%20bertanya..."
    st.markdown(f'<a href="https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}" target="_blank"><button style="background-color:#25D366;color:white;padding:14px 20px;border:none;border-radius:8px;width:100%;font-size:16px;cursor:pointer;">CHAT ADMIN VIA WHATSAPP</button></a>', unsafe_allow_html=True)

elif menu == "Program":
    st.header("📚 Program Kami")
    st.write("1. **Kelas Reguler N5 - N1**: 3x seminggu")
    st.write("2. **Kelas Privat**: Fleksibel sesuai jadwal")
    st.write("3. **Program Kerja/TG**: Persiapan SSW + Interview")

elif menu == "Pendaftaran":
    st.header("📝 Form Pendaftaran")
    st.write("Silahkan isi formulir online di bawah ini:")
    st.markdown(f'<a href="{LINK_GOOGLE_FORM}" target="_blank"><button style="background-color:#FF4B4B;color:white;padding:14px 20px;border:none;border-radius:8px;width:100%;font-size:16px;">BUKA GOOGLE FORM</button></a>', unsafe_allow_html=True)

elif menu == "Kontak":
    st.header("📞 Hubungi Kami")
    st.write(f"**WhatsApp Admin**: {NO_WA_ADMIN}")
    st.write("**Alamat**: Brebes, Jawa Tengah, Indonesia")
    st.write("**Jam Operasional**: Senin - Sabtu, 09.00 - 17.00 WIB")
