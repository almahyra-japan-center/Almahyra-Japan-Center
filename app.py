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
.block-container {{ background: transparent; padding-top: 120px!important; padding-left: 2.5rem!important; max-width: 750px!important; }}
[data-testid="stHeader"] {{ background: white; height: 100px; }}
[data-testid="stHeader"] img {{ height: 80px!important; }}
h1, h2 {{ color: #262730!important; font-weight: 700; }}
p, li {{ color: #31333F!important; font-size: 16px; font-weight: 400; line-height: 1.7; }}
[data-testid="stSidebar"] {{ background: #B22222; }}
[data-testid="stSidebar"] * {{ color: white; font-weight: bold; }}
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
    st.title("🔐 Login Area Khusus")
    st.info("Area ini khusus Murid, Staf, dan Admin AL MAHYRA JC")
    st.write("Contoh: admin/admin123 | staf/staf123 | murid/murid123")
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

# 4. SIDEBAR DINAMIS
def sidebar():
    role = st.session_state['role']
    nama = st.session_state['nama']

    with st.sidebar:
        if role == "PUBLIK":
            st.title("🎌 AL MAHYRA JC")
        else:
            st.title(f"🎌 Halo, {nama}")
            st.caption(f"Role: {role}")

        # MENU PUBLIK SELALU MUNCUL DI ATAS
        st.subheader("Menu Publik")
        menu_publik = st.radio("Navigasi",
            ["🏠 Beranda", "🏢 Profil Lembaga", "📚 Program", "📝 Pendaftaran", "📞 Kontak", "🔐 Login Area"],
            key="menu_publik", label_visibility="collapsed")

        if st.session_state['logged_in']:
            st.divider()
            st.subheader(f"Menu {role}")
            if role == "ADMIN":
                menu_internal = st.radio("Navigasi Admin", ["📊 Dashboard", "👨‍🎓 Manajemen Siswa", "💰 Keuangan", "🚪 Logout"], key="menu_admin", label_visibility="collapsed")
            elif role == "STAF":
                menu_internal = st.radio("Navigasi Staf", ["📅 Generate QR", "👨‍🎓 Data Siswa", "🚪 Logout"], key="menu_staf", label_visibility="collapsed")
            elif role == "MURID":
                menu_internal = st.radio("Navigasi Murid", ["📅 Jadwal", "📚 Materi", "✅ Absen QR", "📝 Ujian", "🚪 Logout"], key="menu_murid", label_visibility="collapsed")

            if menu_internal == "🚪 Logout":
                st.session_state['logged_in'] = False
                st.session_state['role'] = "PUBLIK"
                st.session_state['nama'] = "Tamu"
                st.rerun()
            return menu_publik, menu_internal

        return menu_publik, None

# 5. LOGIKA UTAMA
menu_publik, menu_internal = sidebar()

# ===== BAGIAN 1: MENU PUBLIK - BEBAS DIAKSES =====
if menu_publik == "🏠 Beranda":
    st.header("Selamat Datang! 👋")
    st.write("Terima kasih sudah berkunjung ke website resmi kami.")
    st.subheader("Wujudkan Mimpimu Bekerja & Kuliah ke Jepang Bersama Kami")
    st.write("Belajar Bahasa Jepang dengan metode santai, cepat paham, dan dibimbing sampai lulus JLPT.")

elif menu_publik == "🏢 Profil Lembaga":
    st.header("🏢 Profil Lembaga")
    st.write("**AL MAHYRA JAPAN CENTER** adalah lembaga kursus Bahasa Jepang yang berfokus pada persiapan kerja, magang, dan kuliah ke Jepang. Kami berlokasi di **Brebes, Jawa Tengah**")
    st.subheader("🎯 Visi & Misi")
    st.markdown("**VISI**")
    st.write("Menjadi lembaga kursus Bahasa Jepang terpercaya yang membentuk generasi kompeten, berkarakter, dan siap meraih masa depan di Jepang.")
    st.markdown("**MISI**")
    st.write("1. **Pembelajaran Berkualitas**: Sistematis dari dasar sampai lanjutan")
    st.write("2. **4 Kemampuan Seimbang**: Membaca, menulis, mendengar, dan berbicara")
    st.subheader("📜 Legalitas")
    st.write("SK/NIB: Akan ditampilkan di sini")
    st.subheader("👨‍🏫 Tim Pengajar")
    st.write("Foto dan nama guru akan ditampilkan di sini")

elif menu_publik == "📚 Program":
    st.header("📚 Program Kami")
    st.write("Program Kerja, Magang, Kuliah ke Jepang")

elif menu_publik == "📝 Pendaftaran":
    st.header("📝 Pendaftaran Dibuka!")
    st.write("Silakan daftar melalui form online di bawah ini:")
    st.link_button("KLIK UNTUK DAFTAR ONLINE", LINK_GOOGLE_FORM, use_container_width=True, type="primary")

elif menu_publik == "📞 Kontak":
    st.header("📞 Hubungi Admin")
    st.write("Ada pertanyaan? Langsung hubungi kami:")
    pesan_wa = "Halo%20Admin%20AL%20MAHYRA%20JC,%20saya%20ingin%20bertanya..."
    st.link_button("CHAT ADMIN VIA WHATSAPP", f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}", use_container_width=True)
    st.write(f"Alamat: Brebes, Jawa Tengah, Indonesia")

elif menu_publik == "🔐 Login Area":
    if not st.session_state['logged_in']:
        login()
    else:
        st.success(f"Anda sudah login sebagai {st.session_state['nama']}")

# ===== BAGIAN 2: MENU INTERNAL - HARUS LOGIN DULU =====
if st.session_state['logged_in'] and menu_internal:
    role = st.session_state['role']
    st.divider()

    if role == "ADMIN":
        if menu_internal == "📊 Dashboard": st.header("📊 Dashboard Admin")
        if menu_internal == "👨‍🎓 Manajemen Siswa": st.header("👨‍🎓 Manajemen Siswa")
        if menu_internal == "💰 Keuangan": st.header("💰 Manajemen Keuangan - RAHASIA")

    if role == "STAF":
        if menu_internal == "📅 Generate QR": st.header("📅 Generate QR Absen")
        if menu_internal == "👨‍🎓 Data Siswa": st.header("👨‍🎓 Data Siswa")

    if role == "MURID":
        if menu_internal == "📅 Jadwal": st.header("📅 Jadwal Kelas Kamu")
        if menu_internal == "📚 Materi": st.header("📚 Materi Pelajaran")
        if menu_internal == "✅ Absen QR": st.header("✅ Scan QR Absensi")
        if menu_internal == "📝 Ujian": st.header("📝 Ujian Online JLPT")
