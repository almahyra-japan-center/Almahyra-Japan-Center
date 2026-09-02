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
        return ""

bg = get_base64('Background.jpg') 
logo = get_base64('logo.png')

bg_css = f"url(data:image/jpg;base64,{bg})" if bg else "#FFF5F5"
logo_html = f'<img src="data:image/png;base64,{logo}" width="180">' if logo else ""

# 2. CSS
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
html, body, [class*="st-"] {{ font-family: 'Poppins', sans-serif; }}
.stApp {{ background-image: {bg_css}; background-size: cover; background-attachment: fixed; }}
.block-container {{ padding-top: 1rem; padding-bottom: 2rem; max-width: 700px; }}
header {{ visibility: hidden; }}

h1 {{ color: #B22222!important; font-size: 2.2rem; font-weight: 700; text-align: center; line-height: 1.3; }}
h2 {{ color: #B22222!important; font-size: 1.5rem; font-weight: 600; border-left: 4px solid #B22222; padding-left: 12px; margin-bottom: 15px; }}
h3 {{ color: #262730!important; font-size: 1.1rem; font-weight: 600; }}
p, li {{ color: #333!important; font-size: 16px; line-height: 1.7; }}
.section {{ background: rgba(255,255,255,0.95); padding: 25px; border-radius: 15px; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.06);}}
.hero {{ text-align: center; padding: 20px 20px; }}
.contact-box {{ background: #B22222; color: white; padding: 25px; border-radius: 15px; text-align: center; }}
.contact-box p {{ color: white!important; }}
.stButton>button, .stLinkButton>button {{ background: #B22222; color: white; border-radius: 10px; font-weight: 600; border: none; padding: 12px 20px; font-size: 16px; width: 100%; }}
.stButton>button:hover, .stLinkButton>button:hover {{ background: #8B0000; }}
</style>
""", unsafe_allow_html=True)

# 3. DATA
NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

# 4. SIDEBAR
with st.sidebar:
    st.markdown(f"<div style='text-align:center'>{logo_html}</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#B22222'>AL MAHYRA JC</h3>", unsafe_allow_html=True)
    st.info("Area Login Siswa & Staf masih dalam tahap pengembangan ya 😊")
    st.button("🔐 Login Siswa", disabled=True, use_container_width=True)
    st.button("👨‍🏫 Login Staf/Admin", disabled=True, use_container_width=True)

# 5. ISI PUBLIK - BAHASA SANTAI + MENJEMBATANI
st.markdown('<div class="section hero">', unsafe_allow_html=True)
st.markdown(f"<div style='text-align:center; margin-bottom:20px'>{logo_html}</div>", unsafe_allow_html=True)
st.header("AL MAHYRA JAPAN CENTER")
st.subheader("Langkah Pertama ke Jepang Dimulai dari Bahasa 🇯🇵") # UDAH DIGANTI
st.write("Halo! Punya mimpi mau kerja, magang, atau kuliah ke Jepang?") 
st.write("Nah, syarat utamanya pasti bisa Bahasa Jepang dulu dong 😊")
st.write("Yuk mulai dari sini. Belajarnya santai, materi gampang dipahami, dan ada sensei yang siap nemenin kamu sampe lulus JLPT.")
st.link_button("YUK MULAI BELAJAR BARENG KAMI", LINK_GOOGLE_FORM, use_container_width=True, type="primary") # TOMBOL DIUBAH
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🏢 Kenalan Dulu Yuk sama Kami")
st.write("**AL MAHYRA JAPAN CENTER** itu lembaga kursus Bahasa Jepang di **Brebes**. Tugas kita cuma 1: **nemenin kamu jago Bahasa Jepang**.")
st.write("Soal mau kerja, magang, atau kuliah nanti, kita siap jadi jembatan dan ngasih info sebisa kita ya. Tapi keputusan dan rejeki tetap ditangan kamu 🙏")
st.write("Tenang aja, kita udah legal kok:")
st.write("✓ **NIB** : 1234567890123")
st.write("✓ **Akta Notaris** : No. 05 Tanggal 10 Januari 2024")
st.write("✓ **Terdaftar Resmi** di Kemenkumham RI")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎯 Visi & Misi Kita")
st.subheader("VISI")
st.write("Menjadi tempat belajar Bahasa Jepang yang nyaman, supaya teman-teman lebih siap meraih mimpi berkarir atau kuliah ke Jepang.")
st.subheader("MISI")
st.write("1. **Belajar Santai tapi Serius**: Ngajarin Bahasa Jepang dari nol dengan cara yang mudah dan menyenangkan.")
st.write("2. **Bekali Skill**: Ga cuma bahasa, kita juga sharing tentang budaya dan etika kerja di Jepang biar kamu lebih siap.")
st.write("3. **Jadi Teman Belajar**: Kita dampingi proses belajarmu. Semangat bareng-bareng ya 😊")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("👨‍🎓 Temen-temen yang Udah Gabung Belajar")
st.write("Alhamdulillah udah banyak yang mulai langkah pertamanya bareng kita:")
st.table({
    "Nama": ["Ahmad Fauzi", "Siti Nurhaliza", "Budi Santoso"],
    "Umur": ["21 Tahun", "19 Tahun", "23 Tahun"],
    "Asal": ["Brebes", "Tegal", "Cirebon"]
})
st.caption("*Data langsung dari form pendaftaran ya")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📝 Kelas Baru Buka Lho!")
st.write("Daripada nunggu lama, mending mulai dari sekarang. Kuota terbatas ya.")
st.link_button("DAFTAR KELAS BAHASA JEPANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="contact-box">', unsafe_allow_html=True)
st.header("📞 Mau Tanya-tanya Dulu?")
st.write("Boleh banget! Chat admin kita aja. Sharing santai dulu juga boleh 😄")
st.write("**Alamat**: Jl. Jenderal Sudirman No. 123, Brebes, Jawa Tengah")
st.write(f"**WhatsApp**: {NO_WA_ADMIN}")
pesan_wa = "Halo%20Admin%20AL%20MAHYRA%20JC,%20aku%20mau%20tanya%20tentang%20kursus%20Bahasa%20Jepang%20dong"
st.link_button("CHAT ADMIN", f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section hero">', unsafe_allow_html=True)
st.header("🚀 Siap Mulai Belajar?")
st.write("Ingat, 1000 langkah dimulai dari langkah pertama. Langkah pertamamu ke Jepang ya belajar bahasanya dulu.")
st.link_button("GAS BELAJAR SEKARANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr><center style='font-size:14px'>© 2026 AL MAHYRA JAPAN CENTER. Fokus di Bahasa Jepang 🙏</center>", unsafe_allow_html=True)
