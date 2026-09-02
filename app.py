import streamlit as st

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="wide")

# CSS BUAT BACKGROUND LANGSUNG DARI INTERNET - PASTI MUNCUL
st.markdown("""
<style>
.stApp {
    background-image: url("https://i.imgur.com/8QZkL3P.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
.block-container {
    background-color: rgba(255, 255, 255, 0.92);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}
h1, h2, h3 {
    color: #B22222;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #B22222 0%, #8B0000 100%);
}
[data-testid="stSidebar"] * {
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

NO_WA_ADMIN = "6281234567890"  # GANTI
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"  # GANTI

with st.sidebar:
    st.title("🎌 AL MAHYRA JC")
    menu = st.radio("Menu", ["Beranda", "Program", "Pendaftaran", "Kontak"])

if menu == "Beranda":
    st.image("logo.png", use_container_width=True)
    st.header("Selamat Datang! 👋")
    st.write("Terima kasih sudah berkunjung ke website resmi kami.")
    st.subheader("Wujudkan Mimpimu Bekerja & Kuliah ke Jepang Bersama Kami")
    st.write("Belajar Bahasa Jepang dengan metode santai, cepat paham, dan dibimbing sampai lulus JLPT.")
    st.divider()
    st.subheader("🏢 Profil Lembaga")
    st.write("**AL MAHYRA JAPAN CENTER** adalah lembaga kursus Bahasa Jepang yang berfokus pada persiapan kerja, magang, dan kuliah ke Jepang. Kami berlokasi di **Brebes, Jawa Tengah** dan juga membuka kelas online untuk seluruh Indonesia.")
    st.subheader("🎯 Visi & Misi")
    st.markdown("**VISI**")
    st.write("Menjadi lembaga kursus Bahasa Jepang terpercaya yang membentuk generasi kompeten, berkarakter, dan siap meraih masa depan di Jepang.")
    st.markdown("**MISI**")
    st.write("1. **Pembelajaran Berkualitas**: Sistematis dari dasar sampai lanjutan untuk kerja & kuliah")
    st.write("2. **4 Kemampuan Seimbang**: Membaca, menulis, mendengar, dan berbicara")
    st.write("3. **Bentuk Karakter**: Disiplin, percaya diri, bertanggung jawab, dan beretika")
    st.write("4. **Kenalkan Budaya Jepang**: Etika dan kehidupan masyarakat Jepang")
    st.write("5. **Siap Karier & Studi**: Dukung pendidikan, kerja, dan peluang di Jepang")
    st.write("6. **Lingkungan Nyaman**: Belajar aktif, interaktif, dan menyenangkan")
    st.write("7. **Pendampingan Penuh**: Bimbingan & motivasi sampai capai cita-cita")
    st.divider()
    st.caption("📍 Alamat: Brebes, Jawa Tengah, Indonesia")
    st.subheader("📝 Pendaftaran Dibuka!")
    st.markdown(f'<a href="{LINK_GOOGLE_FORM}" target="_blank"><button style="background-color:#B22222;color:white;padding:14px 20px;border:none;border-radius:8px;width:100%;font-size:16px;cursor:pointer;">KLIK UNTUK DAFTAR ONLINE</button></a>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
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
    st.markdown(f'<a href="{LINK_GOOGLE_FORM}" target="_blank"><button style="background-color:#B22222;color:white;padding:14px 20px;border:none;border-radius:8px;width:100%;font-size:16px;">BUKA GOOGLE FORM</button></a>', unsafe_allow_html=True)

elif menu == "Kontak":
    st.header("📞 Hubungi Kami")
    st.write(f"**WhatsApp Admin**: {NO_WA_ADMIN}")
    st.write("**Alamat**: Brebes, Jawa Tengah, Indonesia")
