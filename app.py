import streamlit as st
import sqlite3
import base64
import os

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="wide")

# 1. KONEK DATABASE
conn = sqlite3.connect('almahyra.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, role TEXT, nama TEXT)''')
c.execute("INSERT OR IGNORE INTO users VALUES ('admin','admin123','ADMIN','Admin ALMAHYRA')")
c.execute("INSERT OR IGNORE INTO users VALUES ('staf','staf123','STAF','Bpk. Guru')")
c.execute("INSERT OR IGNORE INTO users VALUES ('murid','murid123','MURID','Ahmad Siswa')")
conn.commit()

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    bin_str = get_base64_of_bin_file('Baground.jpg')
    bg_image = f"url(data:image/jpg;base64,{bin_str})"
except:
    bg_image = "linear-gradient(180deg, #FFF5F5 0%, #ffffff 100%)"

try:
    logo_bin_str = get_base64_of_bin_file('logo.png')
    logo_base64 = f"data:image/png;base64,{logo_bin_str}"
except:
    logo_base64 = ""

st.markdown(f"""
<style>
.stApp {{ background-image: {bg_image}; background-size: cover; background-attachment: fixed; }}
.block-container {{ background: transparent; padding-top: 120px!important; padding-left: 2.5rem!important; max-width: 800px!important; }}
[data-testid="stHeader"] {{ background: white; height: 100px; }}
[data-testid="stHeader"] img {{ height: 80px!important; }}
h1 {{ color: #B22222!important; font-size: 2.5rem; text-align: center; }}
h2 {{ color: #262730!important; font-weight: 700; border-left: 4px solid #B22222; padding-left: 10px; }}
p, li {{ color: #31333F!important; font-size: 16px; line-height: 1.7; }}
[data-testid="stSidebar"] {{ background: #B22222; }}
[data-testid="stSidebar"] * {{ color: white; font-weight: bold; }}
.section {{ margin-bottom: 60px; }}
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.logo(logo_base64, link=None)

NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

# 2. SET SESSION STATE AWAL
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['role'] = "PUBLIK"
    st.session_state['nama'] = "Tamu"

# 3. FUNGSI LOGIN
def login():
    st.subheader("🔐 Login Area")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login", use_container_width=True, type="primary"):
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = user[0]
            st.session_state['role'] = user[2]
            st.session_state['nama'] = user[3]
            st.success(f"Selamat datang {user[3]}!")
            st.rerun()
        else:
            st.error("Username atau Password salah")

# 4. SIDEBAR HANYA UNTUK LOGIN
def sidebar():
    with st.sidebar:
        st.title("🎌 AL MAHYRA JC")

        if not st.session_state['logged_in']:
            st.info("Silakan login untuk akses area khusus")
            login()
        else:
            st.success(f"Halo, {st.session_state['nama']}")
            st.caption(f"Role: {st.session_state['role']}")
            st.divider()

            role = st.session_state['role']
            if role == "ADMIN":
                menu = st.radio("Menu Admin", ["📊 Dashboard", "👨‍🎓 Manajemen Siswa", "💰 Keuangan"])
            elif role == "STAF":
                menu = st.radio("Menu Staf", ["📅 Generate QR", "👨‍🎓 Data Siswa"])
            elif role == "MURID":
                menu = st.radio("Menu Murid", ["📅 Jadwal", "📚 Materi", "✅ Absen QR", "📝 Ujian"])

            st.divider()
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state['logged_in'] = False
                st.session_state['role'] = "PUBLIK"
                st.session_state['nama'] = "Tamu"
                st.rerun()
            return menu
    return None

# 5. LOGIKA UTAMA
menu_internal = sidebar()

# ===== BAGIAN 1: PUBLIK - 1 HALAMAN SCROLL =====
if not st.session_state['logged_in']:
    # SECTION 1: BERANDA / SAMBUTAN
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Selamat Datang di AL MAHYRA JC 👋")
    st.subheader("Wujudkan Mimpimu Bekerja & Kuliah ke Jepang Bersama Kami")
    st.write("Belajar Bahasa Jepang dengan metode santai, cepat paham, dan dibimbing sampai lulus JLPT & berangkat ke Jepang.")
    st.link_button("📝 DAFTAR SEKARANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

    # SECTION 2: PROFIL LEMBAGA
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("🏢 Profil Lembaga")
    st.write("**AL MAHYRA JAPAN CENTER** adalah lembaga kursus Bahasa Jepang yang berfokus pada persiapan kerja, magang, dan kuliah ke Jepang. Kami berlokasi di **Brebes, Jawa Tengah** dan membuka kelas Online & Offline.")
    st.image("https://via.placeholder.com/800x400.png?text=Foto+Gedung+AL+MAHYRA", caption="Kantor AL MAHYRA JC Brebes")
    st.markdown('</div>', unsafe_allow_html=True)

    # SECTION 3: VISI MISI
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("🎯 Visi & Misi")
    st.subheader("VISI")
    st.write("Menjadi lembaga kursus Bahasa Jepang terpercaya yang membentuk generasi kompeten, berkarakter, dan siap meraih masa depan di Jepang.")
    st.subheader("MISI")
    st.write("1. Pembelajaran Berkualitas: Sistematis dari dasar sampai lanjutan")
    st.write("2. 4 Kemampuan Seimbang: Membaca, menulis, mendengar, dan berbicara")
    st.write("3. Bentuk Karakter: Disiplin, percaya diri, dan beretika")
    st.markdown('</div>', unsafe_allow_html=True)

    # SECTION 4: PROGRAM
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("📚 Program Unggulan Kami")
    col1, col2, col3 = st.columns(3)
    with col1: st.subheader("Program Kerja"); st.write("Persiapan TG/SSW + JLPT")
    with col2: st.subheader("Program Magang"); st.write("Bimbingan lolos seleksi")
    with col3: st.subheader("Program Kuliah"); st.write("Persiapan JLPT & EJU")
    st.markdown('</div>', unsafe_allow_html=True)

    # SECTION 5: PENDAFTARAN
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("📝 Pendaftaran Dibuka!")
    st.write("Daftar sekarang dan dapatkan promo biaya pendaftaran!")
    st.link_button("ISI FORM PENDAFTARAN ONLINE", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

    # SECTION 6: KONTAK
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("📞 Hubungi Kami")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Admin")
        pesan_wa = "Halo%20Admin%20AL%20MAHYRA%20JC,%20saya%20ingin%20bertanya..."
        st.link_button("CHAT WHATSAPP", f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}", use_container_width=True)
    with col2:
        st.subheader("Alamat")
        st.write("Brebes, Jawa Tengah, Indonesia")
        st.write("Senin - Sabtu: 08.00 - 17.00")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== BAGIAN 2: INTERNAL - SETELAH LOGIN =====
else:
    role = st.session_state['role']
    st.title(f"Dashboard {role}")

    if role == "ADMIN":
        if menu_internal == "📊 Dashboard": st.header("📊 Dashboard Admin - Grafik & Ringkasan")
        if menu_internal == "👨‍🎓 Manajemen Siswa": st.header("👨‍🎓 Manajemen Siswa - Tambah/Edit/Hapus")
        if menu_internal == "💰 Keuangan": st.header("💰 Manajemen Keuangan - RAHASIA")

    if role == "STAF":
        if menu_internal == "📅 Generate QR": st.header("📅 Generate QR Absen")
        if menu_internal == "👨‍🎓 Data Siswa": st.header("👨‍🎓 Data Siswa")

    if role == "MURID":
        if menu_internal == "📅 Jadwal": st.header("📅 Jadwal Kelas Kamu")
        if menu_internal == "📚 Materi": st.header("📚 Materi Pelajaran")
        if menu_internal == "✅ Absen QR": st.header("✅ Scan QR Absensi")
        if menu_internal == "📝 Ujian": st.header("📝 Ujian Online JLPT")
