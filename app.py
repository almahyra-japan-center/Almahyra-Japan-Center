import streamlit as st
import base64
import os

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# BACKGROUND
try:
    if os.path.exists('Baground.jpg'):
        bin_str = get_base64_of_bin_file('Baground.jpg')
        bg_image = f"url(data:image/jpg;base64,{bin_str})"
    else:
        bg_image = "linear-gradient(180deg, #FFF5F5 0%, #ffffff 100%)"
except:
    bg_image = "linear-gradient(180deg, #FFF5F5 0%, #ffffff 100%)"

# LOGO.PNG
logo_base64 = ""
if os.path.exists('logo.png'):
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

.block-container {{
    background: transparent;
    padding-top: 1rem !important;
    padding-left: 2rem !important; /* KASIH SPACE DARI MERAH */
    padding-right: 2rem !important;
    max-width: 900px !important;
    margin: 0 auto !important;
}}

[data-testid="stHeader"] {{ display: none; }}

/* BAR PUTIH BUAT LOGO - GEDEIN */
.logo-bar {{
    position: sticky;
    top: 0;
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    background: white;
    padding: 20px 0;
    text-align: center;
    z-index: 9999;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}}
.logo-bar img {{
    height: 180px; /* LOGO DIGEDEIN LAGI */
    width: auto;
}}

/* TEXT DIKECILIN KAYAK DI VIDEO */
h1 {{ font-size: 1.8rem; color: #B22222; font-weight: 700; text-align: left; margin-bottom: 0.5rem; }} /* "Selamat Datang" */
h2 {{ font-size: 1.4rem; color: #333; font-weight: 600; text-align: left; margin-bottom: 1rem; }} /* "Wujudkan Mimpimu" */
h3 {{ font-size: 1.2rem; color: #B22222; font-weight: 600; }}
p, li {{ 
    color: #222; 
    font-size: 15px; /* KECILIN LAGI */
    font-weight: 400; 
    line-height: 1.6; 
    text-align: left; /* RATA KIRI BIAR GA MEPET */
    text-shadow: 1px 1px 2px rgba(255,255,255,0.7); 
    margin-bottom: 0.8rem;
}}

[data-testid="stSidebar"] {{ background: #B22222; width: 16rem !important; }}
[data-testid="stSidebar"] * {{ color: white; font-weight: bold; }}
</style>
""", unsafe_allow_html=True)


if logo_base64:
    st.markdown(f'<div class="logo-bar"><img src="{logo_base64}"></div>', unsafe_allow_html=True)


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
    st.write("**AL MAHYRA JAPAN CENTER** adalah lembaga kursus Bahasa Jepang yang berfokus pada persiapan kerja, magang, dan kuliah ke Jepang.")
