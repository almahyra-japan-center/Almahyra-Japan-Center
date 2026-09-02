import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AL MAHYRA JAPAN CENTER", layout="wide")

NAMA_LOGO = "logo.png"
NO_WA_ADMIN = "6287816094321" 

st.sidebar.title("🇯🇵 AL MAHYRA JC")
try:
    st.sidebar.image(NAMA_LOGO, use_container_width=True)
except:
    pass 
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Tentang Kami", "Jadwal & Biaya", "Pendaftaran", "Kontak"])

if menu == "Beranda":
    try:
        st.image(NAMA_LOGO, width=250)
    except:
        pass
    st.title("AL MAHYRA JAPAN CENTER")
    st.subheader("Lembaga Kursus Bahasa Jepang")
    st.markdown("### Yuk belajar bahasa jepang dari dasar bersama kami!")
    st.write("Bergabunglah jadi keluarga besar kami dan wujudkan mimpimu ke Jepang")
    st.success("🔥 Pendaftaran Gelombang Oktober 2026 Dibuka!")
    st.link_button("💬 Chat Admin WA", f"https://wa.me/{NO_WA_ADMIN}")

elif menu == "Tentang Kami":
    st.header("Tentang AL MAHYRA JAPAN CENTER")
    try:
        st.image(NAMA_LOGO, width=150)
    except:
        pass
    
    st.subheader("Profil")
    st.write("AL MAHYRA JAPAN CENTER adalah lembaga kursus Bahasa Jepang yang fokus mengajarkan dari tingkat dasar N5 hingga tingkat lanjutan N1 dengan metode mudah, sistematis, dan menyenangkan.")
    st.write("Kami berlokasi di Desa Karangsari, Kec. Bulakamba, Kab. Brebes")
    
    st.divider()
    
    st.subheader("Visi")
    st.info("Menjadi lembaga kursus Bahasa Jepang yang terpercaya dan berkualitas dalam membentuk generasi yang kompeten, berkarakter, dan siap meraih masa depan melalui penguasaan Bahasa Jepang.")
    
    st.subheader("Misi")
    st.write("1. Menyelenggarakan pembelajaran Bahasa Jepang yang sistematis dan menyenangkan")
    st.write("2. Membekali peserta dengan kemampuan bahasa untuk studi, kerja, dan budaya Jepang")
    st.write("3. Menumbuhkan semangat disiplin, kerja keras, dan rasa tanggung jawab")

elif menu == "Jadwal & Biaya":
    st.header("📅 Jadwal & Biaya Kursus")
    st.info("Fokus: JLPT N5 - N1 | Kerja ke Jepang | Kuliah ke Jepang")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("KELAS REGULER")
        st.write("**Durasi:** 4 Bulan / Level")
        st.write("**Pertemuan:** 3x Seminggu, 2 Jam")
        st.write("**Jam:** Pagi 08.00-10.00 | Sore 15.00-17.00 | Malam 19.00-21.00")
        st.success("**Biaya:** Rp 800.000 / Level")
        st.write("Sudah termasuk: Modul, Seragam, Ujian Internal")
    
    with col2:
        st.subheader("KELAS INTENSIF MAGANG/TG")
        st.write("**Durasi:** 6 Bulan N4-N3")
        st.write("**Pertemuan:** 5x Seminggu, 3 Jam")
        st.write("**Jam:** 08.00-11.00")
        st.success("**Biaya:** Rp 1.500.000 / Paket")
        st.write("Bonus: Bimbingan Dokumen + Interview")
    
    st.divider()
    st.subheader("🎁 Fasilitas")
    st.write("✅ Pengajar Bersertifikat JLPT N1")
    st.write("✅ Kelas Max 15 Orang")
    st.write("✅ Simulasi Ujian JLPT Gratis")
    st.write("✅ Bimbingan sampai Berangkat ke Jepang")
    
    st.warning("**Catatan:** Biaya pendaftaran awal Rp 200.000")
    st.link_button("💬 Tanya Jadwal Terdekat", f"https://wa.me/{NO_WA_ADMIN}")

elif menu == "Pendaftaran":
    st.header("📝 Form Pendaftaran Online")
    st.write("Isi data di bawah ini. Otomatis masuk ke Google Sheet")
    
    # FORM GOOGLE KAMU
    components.iframe(
        "https://docs.google.com/forms/d/e/fxVaphmsYLKhRF9x6/viewform?embedded=true", 
        height=800, 
        width=700
    )
    
    st.markdown("---")
    st.write("Setelah submit form, klik tombol di bawah untuk konfirmasi ke WA Admin")
    
    # TOMBOL WA
    pesan_wa = "Halo Admin AL MAHYRA JC, saya baru saja mengisi formulir pendaftaran online."
    link_wa = f"https://wa.me/{NO_WA_ADMIN}?text={pesan_wa}"
    st.link_button("📲 KONFIRMASI VIA WA ADMIN", link_wa, type="primary")

elif menu == "Kontak":
    st.header("Informasi Kontak")
    try:
        st.image(NAMA_LOGO, width=120)
    except:
        pass
    st.write("📍 **Alamat**: Desa Karangsari RT 005/01, Kec. Bulakamba, Kab. Brebes")
    st.write("📞 **WhatsApp Admin**: 0878-1609-4321")
    st.write("📅 **Pendaftaran**: Dibuka setiap awal bulan")
    st.link_button("💬 Chat Sekarang", f"https://wa.me/{NO_WA_ADMIN}")
