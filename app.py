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

# BALIK KE LOGO.PNG
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
    padding: 0 !important;
    max-width: 100% !important;
}}

[data-testid="stHeader"] {{ display: none; }}

/* BAR PUTIH BUAT LOGO */
.logo-bar {{
    position: sticky;
    top: 0;
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    background: white;
    padding: 25px 0; /* SEDENG GA KELEBARAN */
    text-align: center;
    z-index: 9999;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}}
.logo-bar img {{
    height: 250px; /* GEDE TAPI MASIH RAPI */
    width: auto;
    max-width: 90%;
}}

/* KONTEN TENGAH KECIL */
.content-wrapper {{
    padding: 2rem 1rem;
    max-width: 700px;
    margin: 0 auto;
    text-align: center;
}}

h1, h2, h3 {{ 
    color: #B22222; 
    font-weight: 700; 
    font-size: 1.4rem; 
    text-shadow: 1px 1px 3px rgba(255,255,255,0.9); 
    margin-bottom: 0.8rem;
}}
p, li {{ 
    color: #222; 
    font-size: 15px; 
    font-weight: 400; 
    line-height: 1.6; 
    text-shadow: 1px 1px 2px rgba(255,255,255,0.8); 
    margin-bottom: 0.8rem;
}}

[data-testid="stSidebar"] {{ background: #B22222; }}
[data-testid="stSidebar"] * {{ color: white; font-weight: bold; }}
</style>
""", unsafe_allow_html=True)


if logo_base64:
    st.markdown(f'<div class="logo-bar"><img src="{logo_base64}"></div>', unsafe_allow_html=True)


NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)
