import streamlit as st
import base64

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

st.markdown(f"""
<style>
.stApp {{
    background-image: {bg_image};
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* GA USAH PAKAI BOX PUTIH SAMA SEKALI */
.block-container {{
    background: transparent;
    padding-top: 150px; /* KASIH JARAK BUAT LOGO */
}}

/* LOGO STICKY DI ATAS */
[data-testid="stHeader"] {{
    background: rgba(255,255,255,0.9);
    backdrop-filter: blur(8px);
}}

h1, h2, h3 {{
    color: #B22222;
    font-weight: 900;
    text-shadow: 2px 2px 5px white;
}}
p, li {{
    color: #111; 
    font-size: 17px;
    font-weight: 600;
    text-shadow: 1px 1px 3px white;
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
st.logo("logo.png")

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
