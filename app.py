import streamlit as st
import sqlite3
import base64
import os
import time
import random
import string
from datetime import datetime

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="wide")

# 1. KONEK DATABASE + BUAT 3 TABEL
conn = sqlite3.connect('almahyra.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, role TEXT, nama TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS absensi
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, nama TEXT,
              waktu TEXT, kelas TEXT, kode TEXT, tanggal TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS kode_absen
             (kelas TEXT PRIMARY KEY, kode TEXT, waktu_generate TEXT)''')
c.execute("INSERT OR IGNORE INTO users VALUES ('admin','admin123','ADMIN','Admin ALMAHYRA')")
c.execute("INSERT OR IGNORE INTO users VALUES ('staf1','staf123','STAF','Bpk. Guru')")
c.execute("INSERT OR IGNORE INTO users VALUES ('murid1','murid123','MURID','Ahmad Siswa')")
conn.commit()

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    bin_str = get_base64_of_bin_file('Background.jpg')
    bg_image = f"url(data:image/jpg;base64,{bin_str})"
except:
    bg_image = "linear-gradient(180deg, #FFF5F5 0%, #ffffff 100%)"

try:
    logo_bin_str = get_base64_of_bin_file('logo.png')
    logo_base64 = f"data:image/png;base64,{logo_bin_str}"
except:
    logo_base64 = ""

# CSS UDAH FIX WARNA & LAYOUT
st.markdown(f"""
<style>
.stApp {{ background-image: {bg_image}; background-size: cover; background-attachment: fixed; }}
.block-container {{ background: transparent; padding-top: 6rem!important; padding-bottom: 3rem!important; max-width: 100%!important; }}
[data-testid="stHeader"] {{ background: white; height: 100px; position: fixed; top: 0; width: 100%; z-index: 999; }}
[data-testid="stHeader"] img {{ height: 80px!important; }}
h1 {{ color: #B22222!important; font-size: 2.5rem; text-align: center; }}
h2 {{ color: #262730!important; font-weight: 700; border-left: 4px solid #B22222; padding-left: 10px; }}
p, label, div[data-testid="stTextInput"] label {{ color: #262730!important; }} /* INI BIKIN TEXT JADI HITAM BIAR KEBACA */
.kode-box {{ background: #B22222; color: white; font-size: 48px; font-weight: bold; text-align: center; padding: 20px; border-radius: 15px; letter-spacing: 10px; margin: 20px 0; }}
[data-testid="stSidebar"] {{ background: #B22222; }}
[data-testid="stSidebar"] * {{ color: white; font-weight: bold; }}
.section {{ margin-bottom: 40px; padding: 25px; background: rgba(255,255,255,0.9); border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
.contact-box {{ background: #B22222; color: white; padding: 20px; border-radius: 10px; text-align: center; }}
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.logo(logo_base64, link=None)

NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['role'] = "PUBLIK"
    st.session_state['nama'] = "Tamu"

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

def generate_kode(kelas):
    kode_baru = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    waktu = datetime.now().strftime("%H:%M:%S")
    c.execute("REPLACE INTO kode_absen (kelas, kode, waktu_generate) VALUES (?,?,?)", (kelas, kode_baru, waktu))
    conn.commit()
    return kode_baru, waktu

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
                menu = st.radio("Menu Staf/Admin", ["📅 Generate Kode", "📊 Rekap Absen"])
            elif role == "MURID":
                menu = st.radio("Menu Murid", ["📅 Jadwal", "✅ Input Kode Absen"])
            st.divider()
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state['logged_in'] = False
                st.session_state['role'] = "PUBLIK"
                st.session_state['nama'] = "Tamu"
                st.rerun()
            return menu
    return None

menu_internal = sidebar()

if not st.session_state['logged_in']:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Selamat Datang di AL MAHYRA JC 👋")
    st.subheader("Wujudkan Mimpimu Bekerja & Kuliah ke Jepang Bersama Kami")
    st.link_button("📝 DAFTAR SEKARANG", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("🏢 Profil Lembaga")
    st.write("**AL MAHYRA JAPAN CENTER** adalah lembaga kursus Bahasa Jepang terpercaya di Semarang. Kami fokus mencetak SDM siap kerja ke Jepang dengan program JLPT N5-N3, Interview, dan Budaya Kerja Jepang.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("📝 Pendaftaran Dibuka!")
    st.write("Isi form di bawah ini untuk daftar kelas baru")
    st.link_button("ISI FORM PENDAFTARAN ONLINE", LINK_GOOGLE_FORM, use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

    # INI KOTAK KONTAK YG HILANG TADI UDAH AKU BALIKIN
    st.markdown('<div class="contact-box">', unsafe_allow_html=True)
    st.header("📞 Hubungi Kami")
    st.write("Jl. Raya Semarang - Demak Km 5, Semarang")
    st.write(f"WhatsApp Admin: {NO_WA_ADMIN}")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    role = st.session_state['role']
    st.title(f"Dashboard {role}")

    if role == "STAF" or role == "ADMIN":
        if menu_internal == "📅 Generate Kode":
            st.header("📅 Generate Kode Absen")
            kelas = st.selectbox("Pilih Kelas", ["N5 Pagi", "N5 Sore", "N4 Pagi", "N4 Sore"])
            data_kode = c.execute("SELECT * FROM kode_absen WHERE kelas=?", (kelas,)).fetchone()
            if data_kode:
                st.markdown(f'<div class="kode-box">{data_kode[1]}</div>', unsafe_allow_html=True)
                st.info(f"Kode Aktif untuk {kelas}. Digenerate jam: {data_kode[2]}")
            else:
                st.warning("Belum ada kode untuk kelas ini. Silakan generate dulu")
            if st.button("GENERATE KODE BARU", use_container_width=True, type="primary"):
                kode_baru, waktu = generate_kode(kelas)
                st.success(f"Kode baru {kode_baru} berhasil dibuat!")
                st.rerun()

        if menu_internal == "📊 Rekap Absen":
            st.header("📊 Rekap Absensi")
            data = c.execute("SELECT tanggal, waktu, kelas, nama, username, kode FROM absensi ORDER BY tanggal DESC, waktu DESC").fetchall()
            st.dataframe(data, use_container_width=True)

    if role == "MURID":
        if menu_internal == "📅 Jadwal":
            st.header("📅 Jadwal Kelas Anda")
            st.info("Jadwal bisa berubah. Hubungi staf jika ada perubahan")
            st.table({
                "Hari": ["Senin - Jumat", "Senin - Jumat", "Sabtu"],
                "Kelas": ["N5 Pagi", "N5 Sore", "N4 Intensif"],
                "Jam": ["08:00 - 11:00", "13:00 - 16:00", "09:00 - 15:00"]
            })

        if menu_internal == "✅ Input Kode Absen":
            st.header("✅ Input Kode Absensi Mandiri")
            st.write("Minta KODE 6 digit ke Staf, lalu masukkan di bawah ini")
            kelas_murid = st.selectbox("Pilih Kelas Anda", ["N5 Pagi", "N5 Sore", "N4 Pagi", "N4 Sore"])
            kode_input = st.text_input("Masukkan Kode dari Staf", placeholder="Contoh: A7B9C1").upper()
            if st.button("ABSEN SEKARANG", use_container_width=True, type="primary"):
                if kode_input:
                    today = datetime.now().strftime("%Y-%m-%d")
                    cek = c.execute("SELECT * FROM absensi WHERE username=? AND tanggal=?", (st.session_state['username'], today)).fetchone()
                    if cek:
                        st.error("Kamu sudah absen hari ini!")
                    else:
                        data_kode = c.execute("SELECT kode FROM kode_absen WHERE kelas=?", (kelas_murid,)).fetchone()
                        if data_kode and data_kode[0] == kode_input:
                            waktu = datetime.now().strftime("%H:%M:%S")
                            c.execute("INSERT INTO absensi (username, nama, waktu, kelas, kode, tanggal) VALUES (?,?,?,?,?,?)",
                                      (st.session_state['username'], st.session_state['nama'], waktu, kelas_murid, kode_input, today))
                            conn.commit()
                            st.success(f"Absen Berhasil! Jam {waktu}")
                            st.balloons()
                        else:
                            st.error("Kode Salah! Minta kode yg terbaru ke Staf")
                else:
                    st.warning("Masukkan kode dulu")
