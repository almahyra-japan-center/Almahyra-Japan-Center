import streamlit as st
import sqlite3
import base64
import os
from datetime import datetime

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", page_icon="🎌", layout="wide")

# 1. KONEK DATABASE
conn = sqlite3.connect('almahyra.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, role TEXT, nama TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS absensi
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, nama TEXT,
              waktu TEXT, kelas TEXT, bukti BLOB, kode TEXT, tanggal TEXT)''')
c.execute("INSERT OR IGNORE INTO users VALUES ('admin','admin123','ADMIN','Admin ALMAHYRA')")
c.execute("INSERT OR IGNORE INTO users VALUES ('staf1','staf123','STAF','Bpk. Guru')")
c.execute("INSERT OR IGNORE INTO users VALUES ('murid1','murid123','MURID','Ahmad Siswa')")
conn.commit()

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

bin_str = get_base64_of_bin_file('Background.jpg')
bg_image = f"url(data:image/jpg;base64,{bin_str})" if bin_str else "#ffffff"

logo_bin_str = get_base64_of_bin_file('logo.png')
logo_base64 = f"data:image/png;base64,{logo_bin_str}" if logo_bin_str else ""

# CSS SIMPLE AJA BIAR GA ERROR
st.markdown(f"""
<style>
.stApp {{ background-image: {bg_image}; background-size: cover; }}
.block-container {{ padding-top: 2rem; }}
[data-testid="stHeader"] {{ background: white; }}
h1 {{ color: #B22222; }}
.section {{ background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.logo(logo_base64)

NO_WA_ADMIN = "6281234567890"
LINK_GOOGLE_FORM = "https://forms.gle/gQ4QZz8yGmmTUc8y5"

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login(role_login):
    st.subheader(f"Login {role_login}")
    username = st.text_input("Username", key=f"user_{role_login}")
    password = st.text_input("Password", type="password", key=f"pass_{role_login}")
    if st.button("Login", key=f"btn_{role_login}"):
        c.execute("SELECT * FROM users WHERE username=? AND password=? AND role=?", (username, password, role_login))
        user = c.fetchone()
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = user[0]
            st.session_state['role'] = user[2]
            st.session_state['nama'] = user[3]
            st.rerun()
        else:
            st.error("Login gagal")

def sidebar():
    with st.sidebar:
        st.title("AL MAHYRA JC")
        if not st.session_state['logged_in']:
            tab1, tab2 = st.tabs(["Login Siswa", "Login Staf"])
            with tab1: login("MURID")
            with tab2: login("STAF")
        else:
            st.write(f"Halo, {st.session_state['nama']}")
            if st.button("Logout"):
                st.session_state['logged_in'] = False
                st.rerun()

sidebar()

if not st.session_state['logged_in']:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Selamat Datang di AL MAHYRA JC")
    st.link_button("DAFTAR", LINK_GOOGLE_FORM)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    role = st.session_state['role']
    st.title(f"Dashboard {role}")

    if role == "STAF":
        st.subheader("Upload Bukti Absen Staf")
        uploaded = st.file_uploader("Upload Foto", type=["jpg","png"])
        if uploaded and st.button("Simpan"):
            st.success("Tersimpan")

    if role == "MURID":
        st.subheader("Upload Bukti Absen Murid")
        uploaded = st.file_uploader("Upload Foto Selfie", type=["jpg","png"])
        if uploaded and st.button("Absen"):
            st.success("Absen Berhasil")
