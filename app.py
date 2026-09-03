import streamlit as st
import base64

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="centered")

# 1. BACKGROUND + LOGO
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        st.warning(f"File {bin_file} tidak ditemukan. Cek nama file & ejaannya ya 😊")
        return ""

bg = get_base64('latarbelakang_20260903_093332_0000.png') 
logo = get_base64('logo.png')

bg_css = f"url(data:image/png;base64,{bg})" if bg else "linear-gradient(180deg, #FFF0F5 0%, #ffffff 100%)"
logo_html = f'<img src="data:image/png;base64,{logo}" width="140">' if logo else "" # LOGO DIKECILIN DIKIT

# 2. CSS BARU + BACKGROUND BLUR
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
html, body, [class*="st-"] {{ font-family: 'Poppins', sans-serif; }}

/* BACKGROUND + OVERLAY BLUR BIAR TEKS JELAS */
.stApp {{ 
    background-image: {bg_css}; 
    background-size: cover; 
    background-attachment: fixed; 
    background-position: center;
}}
.stApp::before {{ /* LAPISAN BLUR TIPIS */
    content: "";
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(255,255,255,0.25); /* PUTIH TRANSPARAN */
    backdrop-filter: blur(3px); /* BLUR 3PX DOANG */
    z-index: -1;
}}

.block-container {{ padding-top: 1rem; padding-bottom: 2rem; max-width: 800px; }}
header {{ visibility: hidden; }}

/* HEADER LOGO + TULISAN SAMPINGAN */
.hero-header {{
    display: flex;
    align-items: center;
    gap: 20px;
    background: rgba(255,255,255,0.92);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(211, 47, 47, 0.15);
}}
.hero-text h1 {{ color: #D32F2F!important; font-size: 2rem; font-weight: 700; line-height: 1.2; margin: 0; }}
.hero-text p {{ color: #555!important; font-size: 1.1rem; font-weight: 500; margin: 5px 0 0 0; }}

h2 {{ color: #D32F2F!important; font-size: 1.5rem; font-weight: 600; border-bottom: 1px solid #E0E0E0; /* GARIS TIPIS */ padding-bottom: 8px; margin-bottom: 15px; }}
p, li {{ color: #444!important; font-size: 16px; line-height: 1.8; }}
.section {{ 
    background: rgba(255,255,255,0.94); 
    padding: 25px; 
    border-radius: 20px; 
    margin-bottom: 25px; 
    box-shadow: 0 8px 25px rgba(211, 47, 47, 0.1); 
    border: 1px solid rgba(211, 47, 47, 0.15);
    transition: transform 0.3s ease; 
}}
.section:hover {{ transform: translateY(-5px); }}
.contact-box {{ background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%); color: white; padding: 25px; border-radius: 20px; text-align: center; }}
.contact-box p {{ color: white!important; }}
.stButton>button, .stLinkButton>button {{ background: linear-gradient(90deg, #D32F2F 0%, #E57373 100%); color: white; border-radius: 12px; font-weight: 600; border: none; padding: 12px 20px; font-size: 16px; width: 100%; transition: all 0.3s ease;}}
.stButton>button:hover, .stLinkButton>button:hover {{ transform: scale(1.03); }}
</style>
""", unsafe_allow_html=True)

# 3. DATA
NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

# 4. SIDEBAR
with st.sidebar:
    st.markdown(f"<div style='text-align:center'>{logo_html}</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#D32F2F'>AL MAHYRA JC</h3>", unsafe_allow_html=True)
    st.info("Area Login Siswa & Staf masih dalam tahap pengembangan ya 😊")
    st.button("🔐 Login Siswa", disabled=True, use_container_width=True)
    st.button("👨‍🏫 Login Staf/Admin", disabled=True, use_container_width=True)

# 5. ISI PUBLIK - HEADER BARU
st.markdown('<div class="hero-header">', unsafe_allow_html=True) # LOGO + TULISAN SAMPINGAN
st.markdown(f"<div>{logo_html}</div>", unsafe_allow_html=True)
st.markdown("""
<div class="hero-text">
    <h1>AL MAHYRA JAPAN CENTER</h1>
    <p>Belajar Bahasa Jepang, Santai Tapi Pasti 🇯🇵</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("Halo! Pengen bisa Bahasa Jepang tapi bingung mulainya dari mana?") 
st.write("Sini gabung bareng kita 😊 Di AL MAHYRA belajarnya asik, materinya gampang, dan ada sensei yang sabar nemenin kamu.")
st.write("Mau buat hobi, nonton anime tanpa subtitle, atau persiapan ujian JLPT? Bisa banget!")
st.link_button("YUK DAFTAR KELAS BAHASA JEPANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🏢 Kenalan Dulu Yuk sama Kami")
st.write("**AL MAHYRA JAPAN CENTER** itu lembaga kursus Bahasa Jepang di **Brebes**.")
st.write("Fokus kita cuma satu: **Bikin kamu jago Bahasa Jepang dari nol sampe lancar**.")
st.write("✓ **NIB** : 1234567890123")
st.write("✓ **Akta Notaris** : No. 05 Tanggal 10 Januari 2024")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎯 Visi & Misi Kita")
st.subheader("VISI")
st.write("“Menjadi lembaga kursus Bahasa Jepang terpercaya yang membentuk generasi kompeten, berkarakter, dan siap meraih masa depan.”")
st.subheader("MISI")
st.write("**1. Pembelajaran Berkualitas** → Sistematis dari dasar sampai lanjutan")
st.write("**2. 4 Kemampuan Seimbang** → Membaca, Menulis, Mendengar, dan Berbicara.")
st.write("**3. Bentuk Karakter** → Disiplin, Percaya Diri, Bertanggung Jawab, dan Beretika.")
st.write("**4. Kenalkan Budaya Jepang** → Biar ga kaget sama etika di sana")
st.write("**5. Siap Karier & Studi** → Dukung rencana pendidikan/kerja")
st.write("**6. Lingkungan Nyaman** → Belajar aktif & menyenangkan.")
st.write("**7. Pendampingan Penuh** → Sensei siap bimbing sampai capai cita-cita.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="contact-box">', unsafe_allow_html=True)
st.header("📞 Mau Tanya-tanya Dulu?")
st.write("Chat admin kita aja. Konsultasi gratis kok 😄")
st.write("**Alamat**: Jl. Jenderal Sudirman No. 123, Brebes, Jawa Tengah")
st.write(f"**WhatsApp**: {NO_WA_ADMIN}")
pesan_wa = "Halo%20Admin%20AL%20MAHYRA%20JC,%20aku%20mau%20tanya%20tentang%20kursus%20Bahasa%20Jepang%20dong"
st.link_button("CHAT ADMIN", f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr><center style='font-size:14px'>© 2026 AL MAHYRA JAPAN CENTER. Lembaga Kursus Bahasa Jepang</center>", unsafe_allow_html=True)
