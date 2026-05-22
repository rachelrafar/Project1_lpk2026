import streamlit as st
import math
import time
import pandas as pd

# ================= CONFIG =================

st.set_page_config(
    page_title="ChemAssist Pro",
    page_icon="🧪",
    layout="centered"
)

# ================= STYLE =================

st.markdown("""
<style>

.stApp{
background:linear-gradient(to bottom,#eef4ff,#ffffff);
}

.header{
padding:30px;
border-radius:25px;
background:white;
text-align:center;
box-shadow:0px 5px 18px rgba(0,0,0,.1);
margin-bottom:20px;
}

.card{
padding:18px;
background:white;
border-radius:20px;
box-shadow:0px 4px 12px rgba(0,0,0,.1);
text-align:center;
margin-bottom:15px;
}

.info-box{
padding:18px;
background:white;
border-radius:20px;
box-shadow:0px 4px 12px rgba(0,0,0,.1);
margin-top:10px;
}

.stButton>button{
width:100%;
height:50px;
border-radius:14px;
font-size:16px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ================= SESSION =================

if "page" not in st.session_state:
    st.session_state.page="Home"

# ================= DATA pH =================

data_ph={

"HCl":{"nama":"Asam Klorida","jenis":"Asam kuat","valensi":1,"Mr":36.46},
"H2SO4":{"nama":"Asam Sulfat","jenis":"Asam kuat","valensi":2,"Mr":98.08},
"HNO3":{"nama":"Asam Nitrat","jenis":"Asam kuat","valensi":1,"Mr":63.01},
"HClO4":{"nama":"Asam Perklorat","jenis":"Asam kuat","valensi":1,"Mr":100.46},

"CH3COOH":{"nama":"Asam Asetat","jenis":"Asam lemah","Ka":1.8e-5,"Mr":60.05},
"HF":{"nama":"Asam Fluorida","jenis":"Asam lemah","Ka":6.8e-4,"Mr":20.01},
"HCOOH":{"nama":"Asam Format","jenis":"Asam lemah","Ka":1.8e-4,"Mr":46.03},
"H3PO4":{"nama":"Asam Fosfat","jenis":"Asam lemah","Ka":7.5e-3,"Mr":98.00},
"H2CO3":{"nama":"Asam Karbonat","jenis":"Asam lemah","Ka":4.3e-7,"Mr":62.03},

"NaOH":{"nama":"Natrium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":40.00},
"KOH":{"nama":"Kalium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":56.11},
"Ba(OH)2":{"nama":"Barium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":171.34},
"Ca(OH)2":{"nama":"Kalsium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":74.09},

"NH3":{"nama":"Amonia","jenis":"Basa lemah","Kb":1.8e-5,"Mr":17.03},
"NH4OH":{"nama":"Amonium Hidroksida","jenis":"Basa lemah","Kb":1.8e-5,"Mr":35.05},
"CH3NH2":{"nama":"Metilamina","jenis":"Basa lemah","Kb":4.4e-4,"Mr":31.06},
"C2H5NH2":{"nama":"Etilamina","jenis":"Basa lemah","Kb":5.6e-4,"Mr":45.08}

}

# ================= DATABASE =================

db={

"HCl":["Asam Klorida","Asam kuat","36.46 g/mol","Korosif dan menyebabkan iritasi"],
"H2SO4":["Asam Sulfat","Asam kuat","98.08 g/mol","Sangat korosif"],
"HNO3":["Asam Nitrat","Asam kuat","63.01 g/mol","Oksidator kuat"],
"HClO4":["Asam Perklorat","Asam kuat","100.46 g/mol","Korosif dan oksidator kuat"],

"CH3COOH":["Asam Asetat","Asam lemah","60.05 g/mol","Iritasi mata"],
"HF":["Asam Fluorida","Asam lemah","20.01 g/mol","Sangat beracun"],
"HCOOH":["Asam Format","Asam lemah","46.03 g/mol","Korosif"],
"H3PO4":["Asam Fosfat","Asam lemah","98.00 g/mol","Iritasi kulit"],

"NaOH":["Natrium Hidroksida","Basa kuat","40.00 g/mol","Korosif"],
"KOH":["Kalium Hidroksida","Basa kuat","56.11 g/mol","Korosif"],
"Ba(OH)2":["Barium Hidroksida","Basa kuat","171.34 g/mol","Berbahaya bila tertelan"],
"Ca(OH)2":["Kalsium Hidroksida","Basa kuat","74.09 g/mol","Iritasi saluran napas"],

"NH3":["Amonia","Basa lemah","17.03 g/mol","Gas beracun"],
"NH4OH":["Amonium Hidroksida","Basa lemah","35.05 g/mol","Iritasi paru-paru"],

"NaCl":["Natrium Klorida","Garam","58.44 g/mol","Relatif aman"],
"KCl":["Kalium Klorida","Garam","74.55 g/mol","Iritasi ringan"],
"AgNO3":["Perak Nitrat","Garam","169.87 g/mol","Oksidator"],
"CuSO4":["Tembaga Sulfat","Garam","159.61 g/mol","Beracun bagi organisme air"],

"C2H5OH":["Etanol","Alkohol","46.07 g/mol","Mudah terbakar"],
"CH3OH":["Metanol","Alkohol","32.04 g/mol","Beracun"],
"Acetone":["Aseton","Keton","58.08 g/mol","Sangat mudah terbakar"],

"Benzene":["Benzena","Aromatik","78.11 g/mol","Karsinogen"],
"Toluene":["Toluena","Aromatik","92.14 g/mol","Beracun"],

"Glucose":["Glukosa","Karbohidrat","180.16 g/mol","Relatif aman"]

}

# ================= SIDEBAR =================

menu=st.sidebar.radio(
"🧪 ChemAssist Pro",
["Home","Larutan","pH","Database","Reaksi","Konversi","Quiz","Tentang"],
index=["Home","Larutan","pH","Database","Reaksi","Konversi","Quiz","Tentang"].index(
st.session_state.page
)
)

st.session_state.page=menu

# ================= HOME =================

if menu=="Home":

    st.markdown("""
    <div class='header'>
    <h1>🧪 ChemAssist Pro</h1>
    <p>Smart Laboratory Chemistry Assistant</p>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    c1.metric("📚 Database",f"{len(db)} Senyawa")
    c2.metric("⚗️ Sistem pH",f"{len(data_ph)} Data")
    c3.metric("🚀 Version","11.0")

    st.balloons()

    a,b=st.columns(2)

    with a:

        if st.button("💧 Smart Solution Maker"):
            st.session_state.page="Larutan"
            st.rerun()

        if st.button("📚 Chemical Database"):
            st.session_state.page="Database"
            st.rerun()

        if st.button("🔄 Konversi Kimia"):
            st.session_state.page="Konversi"
            st.rerun()

    with b:

        if st.button("⚗️ Smart pH Calculator"):
            st.session_state.page="pH"
            st.rerun()

        if st.button("🔬 Prediksi Reaksi"):
            st.session_state.page="Reaksi"
            st.rerun()

        if st.button("🧠 Quiz Kimia"):
            st.session_state.page="Quiz"
            st.rerun()

# ================= LARUTAN =================

elif menu=="Larutan":

    st.title("💧 Smart Solution Maker")

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    senyawa=st.selectbox(
    "Pilih Senyawa",
    list(data_ph.keys()),
    format_func=lambda x:f"{data_ph[x]['nama']} ({x})"
    )

    info=data_ph[senyawa]

    st.info(f"""
Nama Senyawa : {info['nama']}
Rumus Kimia : {senyawa}
Mr : {info['Mr']} g/mol
""")

    M=st.number_input("Konsentrasi (M)",0.1)
    V=st.number_input("Volume (mL)",100.0)

    if st.button("Hitung Massa"):

        with st.spinner("Menghitung massa senyawa..."):
            time.sleep(1)

        massa=(info['Mr']*M*V)/1000

        st.success(f"""
✅ Massa yang diperlukan:
{massa:.4f} gram
""")

        st.code(f"""
1. Timbang {massa:.4f} gram {info['nama']}
2. Larutkan dengan sedikit akuades
3. Pindahkan ke labu ukur
4. Tambahkan akuades hingga volume {V} mL
5. Homogenkan larutan
""")

# ================= pH =================

elif menu=="pH":

    st.title("⚗️ Smart pH Calculator")

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    senyawa=st.selectbox(
    "Pilih Senyawa",
    list(data_ph.keys()),
    format_func=lambda x:f"{data_ph[x]['nama']} ({x})"
    )

    info=data_ph[senyawa]

    st.info(f"""
Nama : {info['nama']}
Jenis : {info['jenis']}
Mr : {info['Mr']} g/mol
""")

    C=st.number_input("Masukkan Konsentrasi (M)",0.01)

    if st.button("Hitung pH"):

        with st.spinner("Menghitung pH..."):
            time.sleep(1)

        if "Asam kuat" in info["jenis"]:

            ph=-math.log10(C*info["valensi"])

        elif "Basa kuat" in info["jenis"]:

            poh=-math.log10(C*info["valensi"])
            ph=14-poh

        elif "Asam lemah" in info["jenis"]:

            H=math.sqrt(info["Ka"]*C)
            ph=-math.log10(H)

        else:

            OH=math.sqrt(info["Kb"]*C)
            poh=-math.log10(OH)
            ph=14-poh

        st.metric("📊 Nilai pH",f"{ph:.2f}")

        st.progress(int((ph/14)*100))

        if ph < 7:

            st.error("🔴 Larutan Bersifat ASAM")

        elif ph > 7:

            st.success("🔵 Larutan Bersifat BASA")

        else:

            st.info("🟢 Larutan Bersifat NETRAL")

# ================= DATABASE =================

elif menu=="Database":

    st.title("📚 Chemical Database")

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    cari=st.text_input("🔎 Cari Senyawa")

    hasil=[
    x for x in db
    if cari.lower() in x.lower()
    or cari.lower() in db[x][0].lower()
    ] if cari else list(db.keys())

    pilih=st.selectbox("Pilih Senyawa",hasil)

    data=db[pilih]

    st.success(f"""
🧪 Nama Senyawa : {data[0]}

📌 Rumus Kimia : {pilih}

⚗️ Jenis : {data[1]}

⚖️ Mr : {data[2]}

⚠️ Bahaya :
{data[3]}
""")

    if st.button("📋 Tampilkan Semua Database"):

        tabel=pd.DataFrame(db).T
        tabel.columns=["Nama","Jenis","Mr","Bahaya"]

        st.dataframe(tabel)

# ================= REAKSI =================

elif menu=="Reaksi":

    st.title("🔬 Prediksi Reaksi Kimia")

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    reaksi=st.text_input("Masukkan Reaksi")

    if st.button("Prediksi"):

        if "HCl + NaOH" in reaksi:

            st.success("""
HCl + NaOH → NaCl + H₂O

Jenis Reaksi:
Netralisasi Asam Basa
""")

        elif "H2SO4 + KOH" in reaksi:

            st.success("""
H₂SO₄ + 2KOH → K₂SO₄ + 2H₂O

Jenis Reaksi:
Netralisasi
""")

        elif "AgNO3 + NaCl" in reaksi:

            st.success("""
AgNO₃ + NaCl → AgCl + NaNO₃

Jenis Reaksi:
Pengendapan
""")

        else:

            st.warning("Reaksi belum tersedia di database")

# ================= KONVERSI =================

elif menu=="Konversi":

    st.title("🔄 Konversi Kimia")

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    pilihan=st.selectbox(
    "Pilih Konversi",
    ["Gram ke Mol","Mol ke Gram","ppm ke mg/L"]
    )

    if pilihan=="Gram ke Mol":

        gram=st.number_input("Massa (gram)",1.0)
        mr=st.number_input("Mr",1.0)

        if st.button("Konversi"):

            mol=gram/mr

            st.success(f"Jumlah mol = {mol:.4f} mol")

    elif pilihan=="Mol ke Gram":

        mol=st.number_input("Mol",1.0)
        mr=st.number_input("Mr Senyawa",1.0)

        if st.button("Hitung Gram"):

            gram=mol*mr

            st.success(f"Massa = {gram:.4f} gram")

    else:

        ppm=st.number_input("ppm",1.0)

        if st.button("Konversi ppm"):

            st.success(f"{ppm} ppm = {ppm} mg/L")

# ================= QUIZ =================

elif menu=="Quiz":

    st.title("🧠 Quiz Kimia")

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    st.subheader("Asam kuat adalah...")

    jawaban=st.radio(
    "Pilih jawaban",
    ["NaCl","HCl","NH3","CH3COOH"]
    )

    if st.button("Cek Jawaban"):

        if jawaban=="HCl":

            st.success("✅ Jawaban Benar!")

            st.balloons()

        else:

            st.error("❌ Jawaban Salah")

# ================= TENTANG =================

elif menu=="Tentang":

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("""
<div class='info-box'>

### 🧪 ChemAssist Pro

Aplikasi laboratorium kimia interaktif berbasis Python dan Streamlit.

### 🚀 Fitur Unggulan

- Smart Solution Maker
- Smart pH Calculator
- Chemical Database
- Prediksi Reaksi Kimia
- Konversi Kimia
- Quiz Kimia Interaktif
- Progress indikator pH
- Tampilan modern dan interaktif

### 🎓 Tujuan

Membantu pembelajaran dan praktikum kimia secara digital.

</div>
""", unsafe_allow_html=True)
