import streamlit as st
import base64

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="centered")

# 1. BACKGROUND DOANG
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f: return base64.b64encode(f.read()).decode()
    except: return ""

bg = get_base64('latarbelakang_20260903_093332_0000.png') 
logo = get_base64('logo.png')

st.markdown(f"""
<style>
.stApp {{ 
    background-image: url(data:image/png;base64,{bg}); 
    background-size: cover; 
    background-attachment: fixed; 
}}

/* INI KOTAKNYA - SIMPLE */
.box {{
    background: white; /* PUTIH SOLID BIAR GA RUSAK */
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px; /* KASIH JARAK */
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}}

h1, h2 {{ color: #D32F2F; }}
p {{ color: #000; font-size: 16px; }} /* HITAM PEKAT */

/* GARIS PEMBATAS */
.garis {{
    height: 2px;
    background: #FFCDD2;
    margin: 25px 0;
}}
</style>
""", unsafe_allow_html=True)

NO_WA = "6281234567890"
LINK_DAFTAR = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

# HEADER
st.markdown(f'<div class="box">', unsafe_allow_html=True)
col1, col2 = st.columns([1,4])
with col1: st.image(f"data:image/png;base64,{logo}", width=100)
with col2: 
    st.markdown("<h1>AL MAHYRA JAPAN CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<p>Belajar Bahasa Jepang, Santai Tapi Pasti 🇯🇵</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# KOTAK 1
st.markdown('<div class="box">', unsafe_allow_html=True)
st.write("Halo! Pengen bisa Bahasa Jepang? Sini gabung 😊")
st.link_button("DAFTAR SEKARANG", LINK_DAFTAR, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="garis"></div>', unsafe_allow_html=True) # GARIS

# KOTAK 2
st.markdown('<div class="box">', unsafe_allow_html=True)
st.header("🏢 Kenalan Dulu Yuk")
st.write("**AL MAHYRA JAPAN CENTER** lembaga kursus di **Brebes**.")
st.write("✓ NIB : 1234567890123")
st.write("✓ Akta : No. 05 Tanggal 10 Januari 2024")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="garis"></div>', unsafe_allow_html=True) # GARIS

# KOTAK 3
st.markdown('<div class="box">', unsafe_allow_html=True)
st.header("🎯 Visi & Misi")
st.write("**VISI**: Menjadi lembaga terpercaya...")
st.write("**MISI**: 1. Pembelajaran Berkualitas 2. 4 Kemampuan...")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="garis"></div>', unsafe_allow_html=True) # GARIS

# KOTAK 4 - SESUAI GAMBAR
st.markdown('<div class="box">', unsafe_allow_html=True)
st.header("👨‍🎓 Temen-temen yang Udah Gabung")
st.table({"Nama": ["Ahmad Fauzi", "Siti Nurhaliza"], "Umur": ["21 Tahun", "19 Tahun"], "Asal": ["Brebes", "Tegal"]})
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="garis"></div>', unsafe_allow_html=True) # GARIS

# KOTAK 5 - UDAH GA MERAH
st.markdown('<div class="box">', unsafe_allow_html=True)
st.header("📞 Mau Tanya-tanya Dulu?")
st.write(f"WhatsApp: {NO_WA}")
st.link_button("CHAT ADMIN", f"https://wa.me/{NO_WA}", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
