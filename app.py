import streamlit as st
import base64
import os

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    bin_str = get_base64_of_bin_file('Baground.jpg')
    bg_image = f"url(data:image/jpg;base64,{bin_str})"
except:
    bg_image = "linear-gradient(180deg, #FFF5F5 0%, #ffffff 100%)"

# LOGO BASE64 BUAT HEADER
try:
    logo_bin_str = get_base64_of_bin_file('logo.png')
    logo_base64 = f"data:image/png;base64,{logo_bin_str}"
except:
    logo_base64 = ""

st.markdown(f"""
<style>
.stApp {{
    background-image: {bg_image};
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* GA USAH PAKAI BOX PUTIH */
.block-container {{
    background: transparent;
    padding-top: 120px !important; /* KASIH JARAK BUAT HEADER LOGO */
    padding-left: 2.5rem !important; /* KASIH JARAK DARI SIDEBAR */
    padding-right: 2rem !important;
    max-width: 750px !important; /* BIAR PANJANG KE BAWAH */
}}

/* HEADER PUTIH BUAT LOGO */
[data-testid="stHeader"] {{
    background: white;
    height: 100px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}}

/* GEDEIN LOGO DI HEADER */
[data-testid="stHeader"] img {{
    height: 80px !important;
    width: auto !important;
}}

/* TEXT PERSIS KAYAK DI FOTO - HITAM ABU */
h1 {{ 
    color: #262730 !important; /* HITAM ABU */
    font-weight: 700;
    font-size: 2rem;
    text-shadow: none; /* HAPUS SHADOW */
    text-align: left;
}}
h2 {{ 
    color: #262730 !important; /* HITAM ABU */
    font-weight: 700;
    font-size: 1.5rem;
    text-shadow: none;
    text-align: left;
    line-height: 1.4;
}}
p, li {{
    color: #31333F !important; /* ABU GELAP */
    font-size: 16px; /* NORMAL */
    font-weight: 400;
    text-shadow: none; /* HAPUS SHADOW */
    text-align: left;
    line-height: 1.7;
}}

[data-testid="stSidebar"] {{
    background: #B22222;
}}
[data-testid="stSidebar"] * {{
    color: white;
    font-weight: bold;
}}
</style>
""", unsafe_allow_html=True)

# LOGO DI HEADER BAWAAN STREAMLIT
if logo_base64:
    st.logo(logo_base64, link=None)

NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

with st.sidebar:
    st.title("🎌 AL MAHYRA JC")
    menu = st.radio("Menu", ["Beranda", "Program", "Pendaftaran", "Kontak"])

if menu == "Beranda":
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
