import streamlit as st
import sqlite3
import base64
import os
import qrcode
import io
import time
from datetime import datetime
from PIL import Image

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="wide")

# 1. KONEK DATABASE + TABEL ABSEN
conn = sqlite3.connect('almahyra.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, role TEXT, nama TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS absensi
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, nama TEXT,
              waktu TEXT, kelas TEXT, token TEXT, tanggal TEXT)''')
c.execute("INSERT OR IGNORE INTO users VALUES ('admin','admin123','ADMIN','Admin ALMAHYRA')")
c.execute("INSERT OR IGNORE INTO users VALUES ('staf1','staf123','STAF','Bpk. Guru')")
c.execute("INSERT OR IGNORE INTO users VALUES ('murid1','murid123','MURID','Ahmad Siswa')")
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

# 3. FUNGSI LOGIN DIPISAH 2
def login(role_login):
    st.subheader(f"🔐 Login Area {role_login}")
    username = st.text_input("Username", key=f"user_{role_login}")
    password = st.text_input("Password", type="password", key=f"pass_{role_login}")
    if st.button("Login", use_container_width=True, type="primary", key=f"btn_{role_login}"):
        c.execute("SELECT * FROM users WHERE username=? AND password=? AND role=?", (username, password, role_login))
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

# 4. FUNGSI GENERATE QR
def generate_qr(kelas):
    token = f"ALMAHYRA-{kelas}-{int(time.time())}" # token ganti tiap detik
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(token)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf)
    return buf.getvalue(), token

# 5. SIDEBAR
def sidebar():
    with st.sidebar:
        st.title("🎌 AL MAHYRA JC")

        if not st.session_state['logged_in']:
            st.info("Silakan login untuk akses area khusus")
            tab1, tab2 = st.tabs(["👨‍🎓 Login Siswa", "👨‍🏫 Login Staf"])

            with tab1: login("MURID"); st.caption("Contoh: murid1 / murid123")
            with tab2: login("STAF"); st.caption("Contoh: staf1 / staf123 | admin / admin123")

        else:
            st.success(f"Halo, {st.session_state['nama']}")
            st.caption(f"Role: {st.session_state['role']}")
            st.divider()

            role = st.session_state['role']
            if role == "ADMIN" or role == "STAF":
                menu = st.radio("Menu Staf/Admin", ["📅 Generate QR", "📊 Rekap Absen", "👨‍🎓 Data Siswa"])
                if role == "ADMIN":
                    menu = st.radio("Menu Admin", ["📊 Dashboard", "📅 Generate QR", "📊 Rekap Absen", "👨‍🎓 Manajemen Siswa"])
            elif role == "MURID":
                menu = st.radio("Menu Murid", ["📅 Jadwal", "📚 Materi", "✅ Scan QR Absen", "📝 Ujian"])

            st.divider()
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state['logged_in'] = False
                st.session_state['role'] = "PUBLIK"
                st.session_state['nama'] = "Tamu"
                st.rerun()
            return menu
    return None

# 6. LOGIKA UTAMA
menu_internal = sidebar()

# ===== BAGIAN 1: PUBLIK =====
if not st.session_state['logged_in']:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Selamat Datang di AL MAHYRA JC 👋")
    st.subheader("Wujudkan Mimpimu Bekerja & Kuliah ke Jepang Bersama Kami")
    st.link_button("📝 DAFTAR SEKARANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("🏢 Profil Lembaga")
    st.write("**AL MAHYRA JAPAN CENTER** adalah lembaga kursus Bahasa Jepang...")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("📝 Pendaftaran Dibuka!")
    st.link_button("ISI FORM PENDAFTARAN ONLINE", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== BAGIAN 2: INTERNAL =====
else:
    role = st.session_state['role']
    st.title(f"Dashboard {role}")

    # MENU STAF & ADMIN
    if role == "STAF" or role == "ADMIN":
        if menu_internal == "📅 Generate QR":
            st.header("📅 Generate QR Absen")
            kelas = st.selectbox("Pilih Kelas", ["N5 Pagi", "N5 Sore", "N4 Pagi", "N4 Sore"])

            if st.button("GENERATE QR SEKARANG", use_container_width=True, type="primary"):
                img_bytes, token = generate_qr(kelas)
                st.session_state['qr_token'] = token
                st.session_state['qr_kelas'] = kelas
                st.session_state['qr_time'] = datetime.now().strftime("%H:%M:%S")

            if 'qr_token' in st.session_state:
                st.image(Image.open(io.BytesIO(img_bytes)), width=300)
                st.success(f"QR untuk kelas {st.session_state['qr_kelas']} berhasil dibuat!")
                st.info(f"Token: {st.session_state['qr_token']}")
                st.warning("QR ini valid. Suruh murid scan sekarang. Token ganti tiap kali generate baru")

        if menu_internal == "📊 Rekap Absen":
            st.header("📊 Rekap Absensi")
            data = c.execute("SELECT * FROM absensi ORDER BY tanggal DESC, waktu DESC").fetchall()
            st.dataframe(data, use_container_width=True)

    # MENU MURID
    if role == "MURID":
        if menu_internal == "✅ Scan QR Absen":
            st.header("✅ Scan QR Absensi Mandiri")
            st.write("Minta QR ke Staf, lalu scan di bawah ini")

            token_input = st.text_input("Masukkan Kode QR dari Staf", placeholder="Tempel token QR di sini")

            if st.button("ABSEN SEKARANG", use_container_width=True, type="primary"):
                if token_input:
                    # Cek udah absen hari ini belum
                    today = datetime.now().strftime("%Y-%m-%d")
                    cek = c.execute("SELECT * FROM absensi WHERE username=? AND tanggal=?", (st.session_state['username'], today)).fetchone()
                    if cek:
                        st.error("Kamu sudah absen hari ini!")
                    else:
                        waktu = datetime.now().strftime("%H:%M:%S")
                        c.execute("INSERT INTO absensi (username, nama, waktu, kelas, token, tanggal) VALUES (?,?,?,?,?,?)",
                                  (st.session_state['username'], st.session_state['nama'], waktu, "N5 Pagi", token_input, today))
                        conn.commit()
                        st.success(f"Absen Berhasil! Jam {waktu}")
                        st.balloons()
                else:
                    st.warning("Masukkan kode QR dulu")
