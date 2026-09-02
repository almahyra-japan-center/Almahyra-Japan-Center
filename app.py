import streamlit as st
import streamlit.components.v1 as components # <-- INI PENTING

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", layout="wide")

NAMA_LOGO = "logo.png"
NO_WA_ADMIN = "6287816094321" 

st.sidebar.title("🇯🇵 AL MAHYRA JC")
try:
    st.sidebar.image(NAMA_LOGO, use_container_width=True)
except:
    pass 
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Profil", "Jadwal & Biaya", "Pendaftaran", "Visi & Misi", "Kontak"])

if menu == "Pendaftaran":
    st.header("📝 Form Pendaftaran Online")
    st.write("Isi data di bawah ini. Otomatis masuk ke Google Sheet")
    
    # INI KODE UNTUK NAMPILIN FORM GOOGLE KAMU
    components.iframe(
        "https://docs.google.com/forms/d/e/fxVaphmsYLKhRF9x6/viewform?embedded=true", 
        height=800, 
        width=700
    )
    
    st.markdown("---")
    st.write("Setelah submit form, klik tombol di bawah untuk konfirmasi ke WA Admin")
    
    pesan_wa = "Halo Admin AL MAHYRA JC, saya baru saja mengisi formulir pendaftaran online."
    link_wa = f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}"
    st.link_button("📲 KONFIRMASI VIA WA ADMIN", link_wa, type="primary")
