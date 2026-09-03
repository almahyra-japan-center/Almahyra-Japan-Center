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

bg = get_base64('Background.jpg') # GANTI PAKE FOTO FUJI/SAKURA YA
logo = get_base64('logo.png')

bg_css = f"url(data:image/jpg;base64,{bg})" if bg else "linear-gradient(180deg, #FFF0F5 0%, #ffffff 100%)"
logo_html = f'<img src="data:image/png;base64,{logo}" width="180">' if logo else ""

# 2. CSS BARU - KOTAK PUTIH + GARIS
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
html, body, [class*="st-"] {{ font-family: 'Poppins', sans-serif; }}

.stApp {{ 
    background-image: {bg_css}; 
    background-size: cover; 
    background-attachment: fixed; 
    background-position: center;
}}
.block-container {{ padding-top: 1.5rem; padding-bottom: 2rem; max-width: 720px; }}
header {{ visibility: hidden; }}

h1 {{ color: #D32F2F!important; font-size: 2.2rem; font-weight: 700; text-align: center; line-height: 1.3; }}
h2 {{ color: #D32F2F!important; font-size: 1.5rem; font-weight: 700; border-bottom: 2px solid #FFCDD2; padding-bottom: 8px; margin-bottom: 15px; }}
h3 {{ color: #333!important; font-size: 1.1rem; font-weight: 600; }}
p, li {{ color: #111!important; font-size: 16px; line-height: 1.8; font-weight: 500; }}

/* INI KOTAK TIAP BAGIAN */
.section {{ 
    background: rgba(255,255,255,0.95); /* 95% PUTIH PEKAT */
    padding: 25px; 
    border-radius: 18px; 
    margin-bottom: 30px; /* JARAK 30PX BIAR BACKGROUND KELIATAN */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); 
    border: 1px solid rgba(0,0,0,0.05);
}}
.hero {{ text-align: center; padding: 20px 20px; }}

/* GARIS PEMBATAS */
.garis {{
    height: 2px;
    background: #FFCDD2; /* GARIS PINK TIPIS */
    margin: 0 0 30px 0;
}}

.stButton>button, .stLinkButton>button {{ background: linear-gradient(90deg, #D32F2F 0%, #E57373 100%); color: white; border-radius: 12px; font-weight: 600; border: none; padding: 12px 20px; font-size: 16px; width: 100%; transition: all 0.3s ease;}}
.stButton>button:hover, .stLinkButton>button:hover {{ transform: scale(1.03); }}
[data-testid="stTable"] {{ background: rgba(255,255,255,0.8); border-radius: 10px; overflow: hidden; }}
</style>
""", unsafe_allow_html=True)

# 3. DATA - TETEP
NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

# 4. SIDEBAR - TETEP
with st.sidebar:
    st.markdown(f"<div style='text-align:center'>{logo_html}</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#D32F2F'>AL MAHYRA JC</h3>", unsafe_allow_html=True)
    st.info("Area Login Siswa & Staf masih dalam tahap pengembangan ya 😊")
    st.button("🔐 Login Siswa", disabled=True, use_container_width=True)
    st.button("👨‍🏫 Login Staf/Admin", disabled=True, use_container_width=True)

# 5. ISI PUBLIK - UDAH DIBUANG GARIS YG DI X
st.markdown('<div class="section hero">', unsafe_allow_html=True)
st.markdown(f"<div style='text-align:center; margin-bottom:20px'>{logo_html}</div>", unsafe_allow_html=True)
st.header("AL MAHYRA JAPAN CENTER")
st.subheader("Belajar Bahasa Jepang, Santai Tapi Pasti 🇯🇵")
st.write("Halo! Pengen bisa Bahasa Jepang tapi bingung mulainya dari mana?") 
st.write("Sini gabung bareng kita 😊 Di AL MAHYRA belajarnya asik, materinya gampang, dan ada sensei yang sabar nemenin kamu.")
st.write("Mau buat hobi, nonton anime tanpa subtitle, atau persiapan ujian JLPT? Bisa banget!")
st.link_button("YUK DAFTAR KELAS BAHASA JEPANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="garis"></div>', unsafe_allow_html=True) # GARIS

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🏢 Kenalan Dulu Yuk sama Kami")
st.write("**AL MAHYRA JAPAN CENTER** itu lembaga kursus Bahasa Jepang di **Brebes**.")
st.write("Fokus kita cuma satu: **Bikin kamu jago Bahasa Jepang dari nol sampe lancar**.")
st.write("Metodenya? Santai, banyak praktek ngomong, dan ga ngebosenin deh pokoknya.")
st.write("Tenang aja, kita udah legal kok:")
st.write("✓ **NIB** : 1234567890123")
st.write("✓ **Akta Notaris** : No. 05 Tanggal 10 Januari 2024")
st.write("✓ **Terdaftar Resmi** di Kemenkumham RI")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="garis"></div>', unsafe_allow_html=True) # GARIS

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎯 Visi & Misi Kita")
st.subheader("VISI")
st.write("“Menjadi lembaga kursus Bahasa Jepang terpercaya yang membentuk generasi kompeten, berkarakter, dan siap meraih masa depan.”") # UDAH DIGANTI

st.subheader("MISI")
st.write("**1. Pembelajaran Berkualitas**") 
st.write("→ Sistematis dari dasar sampai lanjutan, materi disusun rapi biar gampang nangkep.")
st.write("**2. 4 Kemampuan Seimbang**") 
st.write("→ Kita latih bareng: Membaca, Menulis, Mendengar, dan Berbicara.")
st.write("**3. Bentuk Karakter**") 
st.write("→ Ga cuma pinter, tapi juga Disiplin, Percaya Diri, Bertanggung Jawab, dan Beretika.")
st.write("**4. Kenalkan Budaya Jepang**") 
st.write("→ Biar ga kaget, kita kenalin juga etika dan kehidupan masyarakat Jepang.")
st.write("**5. Siap Karier & Studi**") 
st.write("→ Kita dukung kamu yang punya rencana pendidikan, kerja, atau peluang di Jepang.")
st.write("**6. Lingkungan Nyaman**") 
st.write("→ Belajarnya aktif, interaktif, dan pastinya menyenangkan.")
st.write("**7. Pendampingan Penuh**") 
st.write("→ Ada sensei yang siap bimbing & kasih motivasi sampai kamu capai cita-cita.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="garis"></div>', unsafe_allow_html=True) # GARIS

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("👨‍🎓 Temen-temen yang Udah Gabung")
st.write("Yuk liat temen-temen yang udah mulai belajar bareng kita:")
st.table({
    "Nama": ["Ahmad Fauzi", "Siti Nurhaliza", "Budi Santoso"],
    "Umur": ["21 Tahun", "19 Tahun", "23 Tahun"],
    "Asal": ["Brebes", "Tegal", "Cirebon"]
})
st.caption("*Data langsung dari form pendaftaran ya")
st.markdown('</div>', unsafe_allow_html=True)

# UDAH DIHAPUS GARIS YG DI X 1
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📝 Kelas Baru Buka Lho!")
st.write("Kuotanya terbatas. Jangan sampe ketinggalan ya.")
st.link_button("DAFTAR SEKARANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

# UDAH DIHAPUS GARIS YG DI X 2
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📞 Mau Tanya-tanya Dulu?")
st.write("Chat admin kita aja. Konsultasi gratis kok 😄")
st.write("**Alamat**: Jl. Jenderal Sudirman No. 123, Brebes, Jawa Tengah")
st.write(f"**WhatsApp**: {NO_WA_ADMIN}")
pesan_wa = "Halo%20Admin%20AL%20MAHYRA%20JC,%20aku%20mau%20tanya%20tentang%20kursus%20Bahasa%20Jepang%20dong"
st.link_button("CHAT ADMIN", f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="garis"></div>', unsafe_allow_html=True) # GARIS

st.markdown('<div class="section hero">', unsafe_allow_html=True)
st.header("🚀 Yuk Mulai Sekarang!")
st.write("Bahasa Jepang itu gampang kalau ada temennya. Dan temennya ya kita 😊")
st.link_button("GAS IKUT KELAS", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr><center style='font-size:14px; color:#555'>© 2026 AL MAHYRA JAPAN CENTER. Lembaga Kursus Bahasa Jepang</center>", unsafe_allow_html=True)
