import streamlit as st
import sqlite3
import base64
import os

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="wide")

# 1. KONEK DATABASE SEDERHANA
conn = sqlite3.connect('almahyra.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users 
             (username TEXT PRIMARY KEY, password TEXT, role TEXT, nama TEXT)''')
# Akun contoh. Nanti bisa dihapus
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
.block-container {{ background: rgba(255,255,255,0.9); padding: 2rem!important; max-width: 800px!important; margin: 2rem auto!important; border-radius: 12px; }}
[data-testid="stHeader"] {{ background: white; height: 100px; }}
[data-testid="stHeader"] img {{ height: 80px!important; }}
h1, h2 {{ color: #262730!important; }} p {{ color: #31333F!important; }}
[data-testid="stSidebar"] {{ background: #B22222; }}
[data-testid="stSidebar"] * {{ color: white; font-weight: bold; }}
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.logo(logo_base64, link=None)

# 2. FUNGSI LOGIN
def login():
    st.title("🔐 Login AL MAHYRA JC")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = user[0]
            st.session_state['role'] = user[2]
            st.session_state['nama'] = user[3]
            st.rerun()
        else:
            st.error("Username atau Password salah")

# 3. SIDEBAR DINAMIS SESUAI ROLE
def sidebar():
    role = st.session_state['role']
    nama = st.session_state['nama']
    
    with st.sidebar:
        st.title(f"🎌 Halo, {nama}")
        st.caption(f"Role: {role}")
        
        if role == "ADMIN":
            menu = st.radio("Menu Admin", ["📊 Dashboard", "👨‍🎓 Manajemen Siswa", "💰 Manajemen Keuangan", "📚 Manajemen Materi", "🚪 Logout"])
        elif role == "STAF":
            menu = st.radio("Menu Staf", ["📅 Generate QR Absen", "👨‍🎓 Data Siswa", "💵 Lihat Kas", "📢 Pengumuman", "🚪 Logout"])
        elif role == "MURID":
            menu = st.radio("Menu Murid", ["📅 Jadwal Kelas", "📚 Materi", "✅ Absen QR", "📝 Ujian Online", "💳 Bayar SPP", "🚪 Logout"])
        else: # PUBLIK
            menu = st.radio("Menu", ["🏠 Profil Lembaga", "📚 Program", "📝 Pendaftaran", "📞 Kontak", "🔐 Login"])
        
        if menu == "🚪 Logout":
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()
        return menu

# 4. LOGIKA UTAMA
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    menu = sidebar() # Menu Publik
    if menu == "🔐 Login":
        login()
    else:
        # ISI MENU PUBLIK KAMU YG LAMA DI SINI
        st.header("🏠 Profil Lembaga")
        st.write("Ini halaman publik. Visi, Misi, Legalitas, Foto Gedung")
else:
    menu = sidebar() # Menu sesuai role
    role = st.session_state['role']
    
    if role == "ADMIN":
        if menu == "📊 Dashboard": st.header("📊 Dashboard Admin - Grafik & Ringkasan")
        if menu == "👨‍🎓 Manajemen Siswa": st.header("👨‍🎓 Manajemen Siswa - Tambah/Edit/Hapus")
        if menu == "💰 Manajemen Keuangan": st.header("💰 Manajemen Keuangan - Paling Rahasia")
    
    if role == "STAF":
        if menu == "📅 Generate QR Absen": st.header("📅 Generate QR Absen")
        if menu == "👨‍🎓 Data Siswa": st.header("👨‍🎓 Lihat Data Siswa")
    
    if role == "MURID":
        if menu == "📅 Jadwal Kelas": st.header("📅 Jadwal Kelas Kamu")
        if menu == "📚 Materi": st.header("📚 Materi Pelajaran PDF/Video")
        if menu == "✅ Absen QR": st.header("✅ Scan QR Absensi Mandiri")
        if menu == "📝 Ujian Online": st.header("📝 Simulasi Ujian JLPT")
        if menu == "💳 Bayar SPP": st.header("💳 Liat Tagihan & Upload Bukti")
