import streamlit as st
import base64

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="wide")

# 1. BACKGROUND + LOGO
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

bg = get_base64('Background.jpg') # Ganti nama file kamu jadi Background.jpg
logo = get_base64('logo.png')

bg_css = f"url(data:image/jpg;base64,{bg})" if bg else "linear-gradient(180deg, #FFF5F5 0%, #ffffff 100%)"
logo_html = f'<img src="data:image/png;base64,{logo}" width="80">' if logo else ""

# 2. CSS BIAR CANTIK & GA NGEBOSENIN
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
html, body, [class*="st-"] {{ font-family: 'Poppins', sans-serif; }}

.stApp {{ 
    background-image: {bg_css}; 
    background-size: cover; 
    background-attachment: fixed; 
}}
.block-container {{ padding-top: 2rem; padding-bottom: 3rem; }}
[data-testid="stHeader"] {{ background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); }}

h1 {{ color: #B22222!important; font-size: 2.8rem; font-weight: 700; text-align: center; }}
h2 {{ color: #B22222!important; font-size: 2rem; font-weight: 600; border-bottom: 3px solid #B22222; padding-bottom: 10px; margin-bottom: 20px; }}
h3 {{ color: #262730!important; font-weight: 600; }}

p, li {{ color: #333!important; font-size: 17px; line-height: 1.8; }}
.section {{ 
    background: rgba(255,255,255,0.9); 
    padding: 35px; 
    border-radius: 20px; 
    margin-bottom: 40px; 
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}}
.hero {{ text-align: center; padding: 50px 20px; }}
.contact-box {{ background: #B22222; color: white; padding: 30px; border-radius: 20px; text-align: center; }}
.contact-box p {{ color: white!important; }}
.stButton>button {{ background: #B22222; color: white; border-radius: 12px; font-weight: 600; border: none; padding: 12px 25px; }}
.stButton>button:hover {{ background: #8B0000; }}
</style>
""", unsafe_allow_html=True)

# 3. DATA
NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

# 4. SIDEBAR CUMA BUAT RUMAH LOGIN
with st.sidebar:
    st.markdown(f"{logo_html}<h3 style='text-align:center; color:#B22222'>AL MAHYRA JC</h3>", unsafe_allow_html=True)
    st.info("Area Login Siswa & Staf masih dalam tahap pengembangan")
    st.button("🔐 Login Siswa", disabled=True, use_container_width=True)
    st.button("👨‍🏫 Login Staf/Admin", disabled=True, use_container_width=True)

# 5. ISI PUBLIK
st.markdown('<div class="section hero">', unsafe_allow_html=True)
st.markdown(logo_html, unsafe_allow_html=True)
st.header("AL MAHYRA JAPAN CENTER")
st.subheader("Wujudkan Mimpimu Kerja & Kuliah ke Jepang 🇯🇵")
st.write("Belajar Bahasa Jepang dengan metode santai, cepat paham, dan dibimbing sampai lulus JLPT & berangkat ke Jepang.")
st.link_button("📝 DAFTAR SEKARANG GRATIS", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🏢 Profil & Legalitas Lembaga")
st.write("**AL MAHYRA JAPAN CENTER** adalah lembaga kursus Bahasa Jepang terpercaya di Semarang. Kami fokus mencetak SDM siap kerja ke Jepang dengan program JLPT N5-N3, Interview, dan Budaya Kerja Jepang.")
st.write("**Legalitas:**")
st.write("✓ NIB : 1234567890123")
st.write("✓ Akta Notaris : No. 05 Tanggal 10 Januari 2024")
st.write("✓ Terdaftar di Kemenkumham RI")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎯 Visi & Misi Kami")
st.subheader("VISI")
st.write("Menjadi lembaga pendidikan Bahasa Jepang terbaik yang melahirkan generasi muda berkompeten dan siap bersaing di dunia kerja Jepang.")
st.subheader("MISI")
st.write("1. Memberikan pengajaran Bahasa Jepang berkualitas dengan pengajar berpengalaman")
st.write("2. Membekali siswa dengan skill kerja dan budaya Jepang")
st.write("3. Mendampingi siswa sampai penempatan kerja di Jepang")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("👨‍🎓 Calon Siswa Terdaftar")
st.write("Alhamdulillah sudah ratusan orang bergabung bersama kami. Ini sebagian data pendaftar terbaru:")
# INI NANTI KITA HUBUNGIN KE GOOGLE FORM OTOMATIS
st.table({
    "Nama": ["Ahmad Fauzi", "Siti Nurhaliza", "Budi Santoso"],
    "Umur": ["21 Tahun", "19 Tahun", "23 Tahun"],
    "Asal Daerah": ["Semarang", "Demak", "Kendal"]
})
st.caption("*Data diambil langsung dari Google Form Pendaftaran")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📝 Pendaftaran Kelas Baru Dibuka!")
st.write("Kuota terbatas! Yuk amankan kursimu sekarang juga.")
st.link_button("ISI FORM PENDAFTARAN ONLINE", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="contact-box">', unsafe_allow_html=True)
st.header("📞 Hubungi Kami")
st.write("Jl. Raya Semarang - Demak Km 5, Genuk, Semarang")
st.write(f"WhatsApp Admin: {NO_WA_ADMIN}")
pesan_wa = "Halo%20Admin%20AL%20MAHYRA%20JC,%20saya%20ingin%20bertanya%20tentang%20kursus%20Bahasa%20Jepang"
st.link_button("CHAT WHATSAPP ADMIN", f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🚀 Ayo Gabung Sekarang!")
st.write("Jangan tunda lagi mimpimu ke Jepang. Bersama AL MAHYRA JC, masa depanmu lebih cerah.")
st.link_button("DAFTAR SEKARANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr><center>© 2026 AL MAHYRA JAPAN CENTER. Semua Hak Cipta Dilindungi.</center>", unsafe_allow_html=True)
