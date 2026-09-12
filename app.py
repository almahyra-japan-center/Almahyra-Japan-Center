import io
import streamlit as st
import base64

st.set_page_config(page_title="ALMAHYRA JAPAN CENTER", page_icon="🎌", layout="centered")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f: return base64.b64encode(f.read()).decode()
    except: return ""

# === INTEGRASI GAMBAR BG PNG ===
bg = get_base64('latarbelakang_20260903_093332_0000.png')
logo = get_base64('logo.png')
bg_css = f"url(data:image/png;base64,{bg})" if bg else "linear-gradient(180deg, #FFF0F5 0%, #ffffff 100%)"
logo_html = f'<img src="data:image/png;base64,{logo}" width="180">' if logo else ""

st.markdown(f"""
<style>
@import url('https://googleapis.com');
html, body, [class*="st-"] {{ font-family: 'Poppins', sans-serif; }}
.stApp {{ background-image: {bg_css}; background-size: cover; background-attachment: fixed; background-position: center;}}
.block-container {{ padding-top: 1rem; padding-bottom: 2rem; max-width: 720px; }}
header {{ visibility: hidden; }}

h1 {{ color: #D32F2F!important; font-size: 2.2rem; font-weight: 700; text-align: center; text-shadow: 1px 1px 2px rgba(255,255,255,0.8); }}
h2 {{ color: #D32F2F!important; font-size: 1.5rem; font-weight: 700; border-bottom: 2px solid #FFCDD2; padding-bottom: 8px; margin-bottom: 15px; }}
p, li {{ color: #111!important; font-size: 16px; line-height: 1.8; font-weight: 500; }}

.card {{ 
    background: rgba(255, 255, 255, 0.98); 
    backdrop-filter: blur(10px); 
    -webkit-backdrop-filter: blur(10px);
    padding: 25px; 
    border-radius: 18px; 
    margin: 0 0 20px 0; 
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15); 
    border: 1px solid rgba(255, 205, 210, 0.6);
}}
.hero {{ text-align: center; }}
.divider {{ height: 2px; background: rgba(213, 47, 47, 0.4); margin: 25px 0; border: none; }}
.stLinkButton>button {{ background: linear-gradient(90deg, #D32F2F 0%, #E57373 100%); color: white; border-radius: 12px; font-weight: 600; border: none; padding: 12px 20px; font-size: 16px; width: 100%;}}
[data-testid="stTable"] {{ background: white; border-radius: 8px; padding: 10px; }}
</style>
""", unsafe_allow_html=True)

# === 🔒 DATABASE INFORMASI DATA RESMI DIKUNCI MATI (SUDAH DIUBAH KE LINK PANJANG ASLI ANTI-BLOKIR) ===
GMAIL_ADMIN = "adminajcbrebes@gmail.com"

# 1. Menggunakan link langsung Google Form (Bukan tautan pendek forms.gle)
LINK_GOOGLE_FORM = "https://google.com"

# 2. Menggunakan koordinat universal Google Maps (Bukan tautan pendek maps.app.goo.gl)
LINK_GOOGLE_MAPS = "https://google.com"

# 3. Tautan WA Valid
LINK_WA_FIX = "https://wa.me"

with st.sidebar:
    st.markdown(f"<div style='text-align:center'>{logo_html}</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#D32F2F'>AL MAHYRA JC</h3>", unsafe_allow_html=True)
    st.info("Situs Resmi Informasi Lembaga")

st.markdown('<div class="card hero">', unsafe_allow_html=True)
st.markdown(f"<div style='text-align:center; margin-bottom:20px'>{logo_html}</div>", unsafe_allow_html=True)
st.header("ALMAHYRA JAPAN CENTER")
st.subheader("Belajar Bahasa Jepang, Santai Tapi Pasti")
st.write("Halo! Pengen bisa Bahasa Jepang tapi bingung mulainya dari mana?") 
st.write("Sini gabung bareng kita 😊 Di AL MAHYRA belajarnya asik, materinya gampang, dan ada sensei yang sabar nemenin kamu.")
st.write("Mau buat hobi, nonton anime tanpa subtitle, atau persiapan ujian JLPT? Bisa banget!")
st.link_button("YUK DAFTAR KELAS BAHASA JEPANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🏢 Kenalan Dulu Yuk sama Kami")
st.write("**AL MAHYRA JAPAN CENTER** itu lembaga kursus Bahasa Jepang di **Brebes**.")
st.write("Fokus kita cuma satu: **Bikin kamu jago Bahasa Jepang dari nol sampe lancar**.")
st.write("Metodenya? Santai, banyak praktek ngomong, dan ga ngebosenin deh pokoknya.")
st.write("✓ **NIB** : 0309260123769")
st.write("✓ **Terdaftar Resmi** di Kemenkumham RI")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🎯 Visi & Misi Kita")
st.subheader("VISI")
st.write("“Menjadi lembaga kursus Bahasa Jepang terpercaya yang membentuk generasi kompeten, berkarakter, dan siap meraih masa depan.”")
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

st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("👨‍🎓 Temen-temen yang Udah Gabung")
st.write("Yuk liat temen-temen yang udah mulai belajar bareng kita:")
st.table({"Nama": ["Ahmad Fauzi", "Siti Nurhaliza", "Budi Santoso"], "Umur": ["21 Tahun", "19 Tahun", "23 Tahun"], "Asal": ["Brebes", "Tegal", "Cirebon"]})
st.caption("*Data simulasi angkatan awal")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("📝 Kelas Baru Buka Lho!")
st.write("Kuotanya terbatas. Jangan sampe ketinggalan ya.")
st.link_button("DAFTAR SEKARANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# === AREA KONTAK RESMI (100% SUKSES DAN BEBAS DYNAMIC LINK ERROR) ===
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("📞 Mau Tanya-tanya Dulu?")
st.write("Chat admin kita aja. Konsultasi gratis kok 😄")
st.write("**Alamat**: Karangsari, RT 005/001, Bulakamba, Kabupaten Brebes, Jawa Tengah")
st.link_button("📍 BUKA DI GOOGLE MAPS", LINK_GOOGLE_MAPS, use_container_width=True)

st.write("**WhatsApp**: 0878-9274-1860")
st.write(f"**Email Resmi**: {GMAIL_ADMIN}")
st.link_button("💬 CHAT ADMIN VIA WHATSAPP", LINK_WA_FIX, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown('<div class="card hero">', unsafe_allow_html=True)
st.header("🚀 Yuk Mulai Sekarang!")
st.write("Bahasa Jepang itu gampang kalau ada temennya. Dan temennya ya kita 😊")
st.link_button("GAS IKUT KELAS", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<center style='font-size:14px; color:#555; margin-top:20px; text-shadow: 1px 1px 1px #fff;'>© 2026 ALMAHYRA JAPAN CENTER. Lembaga Kursus Bahasa Jepang</center>", unsafe_allow_html=True)
