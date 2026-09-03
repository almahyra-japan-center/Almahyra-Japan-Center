import streamlit as st
import base64

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="centered")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f: return base64.b64encode(f.read()).decode()
    except: return ""

bg = get_base64('latarbelakang_20260903_093332_0000.png') 
logo = get_base64('logo.png')
bg_css = f"url(data:image/png;base64,{bg})" if bg else "linear-gradient(180deg, #FFF0F5 0%, #ffffff 100%)"
logo_html = f'<img src="data:image/png;base64,{logo}" width="110">' if logo else ""

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&display=swap');
html, body, [class*="st-"] {{ font-family: 'Poppins', sans-serif; }}

.stApp {{ 
    background-image: {bg_css}; 
    background-size: cover; 
    background-attachment: fixed; 
    background-position: center;
}}

.block-container {{ padding-top: 2rem; padding-bottom: 2rem; max-width: 700px; }}
header {{ visibility: hidden; }}

/* HEADER */
.hero-header {{
    display: flex; align-items: center; gap: 15px;
    background: rgba(255,255,255,0.95); /* 95% PEKAT */
    padding: 18px 20px; border-radius: 18px;
    margin-bottom: 40px; /* JARAK JAUH */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}}
.hero-text h1 {{ color: #C62828!important; font-size: 1.7rem; font-weight: 800; margin: 0; }}
.hero-text p {{ color: #333!important; font-size: 1rem; font-weight: 600; margin: 4px 0 0 0; }}

/* INI KOTAK TIAP PESAN - BENER2 KOTAK */
.section {{ 
    background: rgba(255,255,255,0.95); /* 95% PEKAT BIAR KEBACA */
    padding: 25px; 
    border-radius: 18px; 
    margin-bottom: 40px; /* KASIH JARAK 40PX = BACKGROUND KELIATAN LEBAR */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); 
    border: 1px solid rgba(0,0,0,0.05);
}}
h2 {{ color: #C62828!important; font-size: 1.5rem; font-weight: 800; margin-bottom: 15px; }}
p, li {{ color: #111!important; font-size: 16px; line-height: 1.8; font-weight: 600; }} /* TULISAN TEBEL */

/* KOTAK MERAH */
.contact-box {{ 
    background: #C62828; /* MERAH SOLID */
    color: white; padding: 25px; border-radius: 18px; text-align: center; 
    margin-bottom: 40px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}}
.contact-box p {{ color: white!important; font-weight: 600; }}
.contact-box h2 {{ color: white!important; }}

.stLinkButton>button {{ background: #C62828; color: white; border-radius: 12px; font-weight: 700; border: none; padding: 14px 20px; font-size: 16px; width: 100%;}}
</style>
""", unsafe_allow_html=True)

NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

# HEADER
st.markdown('<div class="hero-header">', unsafe_allow_html=True) 
st.markdown(f"<div>{logo_html}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='hero-text'><h1>AL MAHYRA JAPAN CENTER</h1><p>Belajar Bahasa Jepang, Santai Tapi Pasti 🇯🇵</p></div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# KOTAK 1
st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("Halo! Pengen bisa Bahasa Jepang tapi bingung mulainya dari mana? Sini gabung bareng kita 😊")
st.link_button("YUK DAFTAR KELAS", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

# KOTAK 2 - INI YG KAMU LINGKARI
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🏢 Kenalan Dulu Yuk sama Kami")
st.write("**AL MAHYRA JAPAN CENTER** itu lembaga kursus Bahasa Jepang di **Brebes**.")
st.write("Fokus kita: **Bikin kamu jago Bahasa Jepang dari nol sampe lancar**.")
st.write("✓ **NIB** : 1234567890123")
st.write("✓ **Akta Notaris** : No. 05 Tanggal 10 Januari 2024")
st.markdown('</div>', unsafe_allow_html=True)

# KOTAK 3
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎯 Visi & Misi Kita")
st.write("**VISI**: Menjadi lembaga kursus Bahasa Jepang terpercaya...")
st.write("**MISI**: 1. Pembelajaran Berkualitas 2. 4 Kemampuan Seimbang ...")
st.markdown('</div>', unsafe_allow_html=True)

# KOTAK 4 CONTACT
st.markdown('<div class="contact-box">', unsafe_allow_html=True)
st.header("📞 Mau Tanya-tanya Dulu?")
st.write("Chat admin kita aja. Konsultasi gratis kok 😄")
st.write(f"**WhatsApp**: {NO_WA_ADMIN}")
pesan_wa = "Halo%20Admin%20AL%20MAHYRA%20JC,%20aku%20mau%20tanya%20tentang%20kursus%20Bahasa%20Jepang%20dong"
st.link_button("CHAT ADMIN", f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
