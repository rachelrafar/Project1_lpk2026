import streamlit as st
import math
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

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
border-radius:22px;
background:white;
text-align:center;
box-shadow:0px 5px 18px rgba(0,0,0,.1);
margin-bottom:20px;
}

.card{
padding:18px;
background:white;
border-radius:18px;
box-shadow:0px 4px 12px rgba(0,0,0,.1);
text-align:center;
transition:0.3s;
}

.card:hover{
transform:scale(1.02);
}

.stButton>button{
width:100%;
border-radius:12px;
height:50px;
font-size:16px;
font-weight:bold;
}

.info-box{
padding:18px;
background:white;
border-radius:18px;
box-shadow:0px 4px 12px rgba(0,0,0,.1);
margin-top:10px;
}

.big-font{
font-size:18px;
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
"HBr":{"nama":"Asam Bromida","jenis":"Asam kuat","valensi":1,"Mr":80.91},
"HI":{"nama":"Asam Iodida","jenis":"Asam kuat","valensi":1,"Mr":127.91},
"HNO3":{"nama":"Asam Nitrat","jenis":"Asam kuat","valensi":1,"Mr":63.01},
"H2SO4":{"nama":"Asam Sulfat","jenis":"Asam kuat","valensi":2,"Mr":98.08},
"HClO4":{"nama":"Asam Perklorat","jenis":"Asam kuat","valensi":1,"Mr":100.46},

"NaOH":{"nama":"Natrium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":40.00},
"KOH":{"nama":"Kalium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":56.11},
"LiOH":{"nama":"Litium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":23.95},
"Ba(OH)2":{"nama":"Barium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":171.34},
"Ca(OH)2":{"nama":"Kalsium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":74.09},

"CH3COOH":{"nama":"Asam Asetat","jenis":"Asam lemah","Ka":1.8e-5,"Mr":60.05},
"HF":{"nama":"Asam Fluorida","jenis":"Asam lemah","Ka":6.8e-4,"Mr":20.01},
"HCOOH":{"nama":"Asam Format","jenis":"Asam lemah","Ka":1.8e-4,"Mr":46.03},
"HCN":{"nama":"Asam Sianida","jenis":"Asam lemah","Ka":4.9e-10,"Mr":27.03},
"H2CO3":{"nama":"Asam Karbonat","jenis":"Asam lemah","Ka":4.3e-7,"Mr":62.03},
"H3PO4":{"nama":"Asam Fosfat","jenis":"Asam lemah","Ka":7.5e-3,"Mr":98.00},
"H2S":{"nama":"Asam Sulfida","jenis":"Asam lemah","Ka":1e-7,"Mr":34.08},
"C6H8O7":{"nama":"Asam Sitrat","jenis":"Asam lemah","Ka":7.4e-4,"Mr":192.12},
"H2C2O4":{"nama":"Asam Oksalat","jenis":"Asam lemah","Ka":5.9e-2,"Mr":90.03},

"NH3":{"nama":"Amonia","jenis":"Basa lemah","Kb":1.8e-5,"Mr":17.03},
"NH4OH":{"nama":"Amonium Hidroksida","jenis":"Basa lemah","Kb":1.8e-5,"Mr":35.05},
"CH3NH2":{"nama":"Metilamina","jenis":"Basa lemah","Kb":4.4e-4,"Mr":31.06},
"C2H5NH2":{"nama":"Etilamina","jenis":"Basa lemah","Kb":5.6e-4,"Mr":45.08},
"C5H5N":{"nama":"Piridina","jenis":"Basa lemah","Kb":1.7e-9,"Mr":79.10},

}

# ================= DATABASE =================

db={

"HCl":["Asam Klorida","Asam kuat","36.46 g/mol","Korosif dan iritasi"],
"H2SO4":["Asam Sulfat","Asam kuat","98.08 g/mol","Sangat korosif"],
"HNO3":["Asam Nitrat","Asam kuat","63.01 g/mol","Oksidator kuat"],
"NaOH":["Natrium Hidroksida","Basa kuat","40.00 g/mol","Menyebabkan luka bakar"],
"KOH":["Kalium Hidroksida","Basa kuat","56.11 g/mol","Korosif"],
"NH3":["Amonia","Basa lemah","17.03 g/mol","Gas beracun"],
"NH4OH":["Amonium Hidroksida","Basa lemah","35.05 g/mol","Iritasi paru-paru"],
"CH3COOH":["Asam Asetat","Asam lemah","60.05 g/mol","Iritasi mata"],
"HF":["Asam Fluorida","Asam lemah","20.01 g/mol","Sangat beracun"],
"HCOOH":["Asam Format","Asam lemah","46.03 g/mol","Korosif"],
"H3PO4":["Asam Fosfat","Asam lemah","98.00 g/mol","Iritasi kulit"],
"C6H8O7":["Asam Sitrat","Asam lemah","192.12 g/mol","Iritasi ringan"],
"NaCl":["Natrium Klorida","Garam","58.44 g/mol","Relatif aman"],
"KCl":["Kalium Klorida","Garam","74.55 g/mol","Iritasi ringan"],
"AgNO3":["Perak Nitrat","Garam","169.87 g/mol","Oksidator"],
"CuSO4":["Tembaga Sulfat","Garam","159.61 g/mol","Beracun bagi air"],
"FeCl3":["Besi(III) Klorida","Garam","162.20 g/mol","Korosif"],
"MgSO4":["Magnesium Sulfat","Garam","120.37 g/mol","Iritasi ringan"],
"Na2CO3":["Natrium Karbonat","Garam basa","105.99 g/mol","Iritasi kulit"],
"NaHCO3":["Natrium Bikarbonat","Garam basa","84.01 g/mol","Relatif aman"],
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
["Home","Larutan","pH","Database","Reaksi","Tentang"],
index=["Home","Larutan","pH","Database","Reaksi","Tentang"].index(
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
    """,unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    c1.metric("📚 Database",f"{len(db)} Senyawa")
    c2.metric("⚗️ pH System",f"{len(data_ph)} Data")
    c3.metric("🚀 Version","8.0")

    a,b,c=st.columns(3)

    with a:
        st.markdown("""
        <div class='card'>
        <h3>💧 Smart Solution</h3>
        <p>Perhitungan larutan otomatis</p>
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Menu Larutan"):
            st.session_state.page="Larutan"
            st.rerun()

    with b:
        st.markdown("""
        <div class='card'>
        <h3>⚗️ Smart pH</h3>
        <p>Kalkulator pH interaktif</p>
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Kalkulator pH"):
            st.session_state.page="pH"
            st.rerun()

    with c:
        st.markdown("""
        <div class='card'>
        <h3>📚 Database</h3>
        <p>Informasi bahan kimia</p>
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Database"):
            st.session_state.page="Database"
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

    st.markdown(f"""
<div class='info-box'>
<b>Nama Senyawa:</b> {info['nama']}<br>
<b>Rumus Kimia:</b> {senyawa}<br>
<b>Mr:</b> {info['Mr']} g/mol
</div>
""", unsafe_allow_html=True)

    M=st.number_input("Konsentrasi (M)",0.1)
    V=st.number_input("Volume (mL)",100.0)

    if st.button("Hitung Massa"):

        massa=(info['Mr']*M*V)/1000

        st.success(f"""
✅ Massa senyawa yang diperlukan:
{massa:.4f} gram
""")

        st.info(f"""
📋 Prosedur Pembuatan Larutan:

1. Timbang {massa:.4f} gram {info['nama']}
2. Larutkan dengan sedikit akuades
3. Masukkan ke labu ukur {V} mL
4. Tambahkan akuades hingga tanda batas
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

    st.markdown(f"""
<div class='info-box'>
<b>Nama:</b> {info['nama']}<br>
<b>Rumus:</b> {senyawa}<br>
<b>Jenis:</b> {info['jenis']}<br>
<b>Mr:</b> {info['Mr']} g/mol
</div>
""", unsafe_allow_html=True)

    C=st.number_input("Masukkan Konsentrasi (M)",0.01)

    if st.button("Hitung pH"):

        if "Asam kuat"==info["jenis"]:
            ph=-math.log10(C*info["valensi"])

        elif "Basa kuat"==info["jenis"]:
            poh=-math.log10(C*info["valensi"])
            ph=14-poh

        elif "Asam lemah"==info["jenis"]:
            H=math.sqrt(info["Ka"]*C)
            ph=-math.log10(H)

        else:
            OH=math.sqrt(info["Kb"]*C)
            poh=-math.log10(OH)
            ph=14-poh

        st.metric("📊 Nilai pH",f"{ph:.2f}")

        # grafik pH
        fig, ax = plt.subplots(figsize=(8,1))
        ax.barh(["pH"], [ph])
        ax.set_xlim(0,14)
        st.pyplot(fig)

        if ph < 7:
            st.error("Larutan bersifat ASAM")

        elif ph > 7:
            st.success("Larutan bersifat BASA")

        else:
            st.info("Larutan NETRAL")

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

    st.markdown(f"""
<div class='info-box'>

### 🧪 Informasi Senyawa

- Nama Senyawa : {data[0]}
- Rumus Kimia : {pilih}
- Jenis Senyawa : {data[1]}
- Mr : {data[2]}

### ⚠️ Bahaya

{data[3]}

</div>
""", unsafe_allow_html=True)

# ================= REAKSI =================

elif menu=="Reaksi":

    st.title("⚗️ Prediksi Reaksi Kimia")

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    reaksi=st.text_input("Masukkan reaksi")

    if st.button("Prediksi Reaksi"):

        if "HCl + NaOH" in reaksi:
            st.success("""
HCl + NaOH → NaCl + H₂O

Jenis reaksi:
Netralisasi Asam-Basa
""")

        elif "H2SO4 + KOH" in reaksi:
            st.success("""
H₂SO₄ + 2KOH → K₂SO₄ + 2H₂O

Jenis reaksi:
Netralisasi
""")

        else:
            st.warning("Reaksi belum tersedia di database")

# ================= TENTANG =================

elif menu=="Tentang":

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("""
<div class='info-box'>

### 🧪 ChemAssist Pro

Aplikasi laboratorium kimia interaktif berbasis Python dan Streamlit.

### 🚀 Fitur Utama

- Kalkulator pH otomatis
- Smart solution maker
- Database senyawa kimia
- Prediksi reaksi kimia
- Grafik indikator pH
- Export data laboratorium

### 👨‍💻 Teknologi

- Python
- Streamlit
- Matplotlib
- Pandas

### 🎓 Tujuan

Membantu praktikum dan pembelajaran kimia secara digital dan interaktif.

</div>
""", unsafe_allow_html=True)
