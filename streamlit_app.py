import streamlit as st
import math
import random

# ================= CONFIG =================

st.set_page_config(
    page_title="ChemAssist Pro",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= FIX SIDEBAR =================

st.markdown("""
<style>

[data-testid="collapsedControl"]{
display:none !important;
visibility:hidden !important;
}

header{
visibility:hidden;
}

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ================= STYLE =================

st.markdown("""
<style>

html, body, [class*="css"], .stMarkdown, .stText, p, div, span, label{
font-family:'Segoe UI',sans-serif !important;
}

.stApp{
background:linear-gradient(to bottom,#edf4ff,#ffffff);
}

section[data-testid="stSidebar"]{
background:#f4f7fc;
}

/* HEADER */

.header{
padding:45px;
border-radius:30px;
background:linear-gradient(135deg,#0f4c81,#4da8ff);
text-align:center;
box-shadow:0px 6px 20px rgba(0,0,0,.15);
margin-bottom:25px;
color:white;
}

.home-title{
font-size:56px;
font-weight:bold;
}

.home-sub{
font-size:20px;
opacity:0.95;
}

/* CARD */

.card{
padding:22px;
background:white;
border-radius:22px;
box-shadow:0px 4px 15px rgba(0,0,0,.10);
text-align:center;
margin-bottom:15px;
transition:0.3s;
}

.card:hover{
transform:scale(1.03);
}

/* METRIC */

.metric-box{
padding:20px;
background:white;
border-radius:20px;
text-align:center;
box-shadow:0px 4px 12px rgba(0,0,0,.08);
}

/* BUTTON */

.stButton>button{
width:100%;
height:52px;
border-radius:14px;
font-size:16px;
font-weight:bold;
border:none;
background:linear-gradient(90deg,#0f4c81,#4da8ff);
color:white;
font-family:'Segoe UI',sans-serif !important;
}

/* INFO */

.info-box{
padding:20px;
background:white;
border-radius:20px;
box-shadow:0px 4px 12px rgba(0,0,0,.08);
margin-top:10px;
}

.feature-title{
font-size:20px;
font-weight:bold;
color:#0f4c81;
}

</style>
""", unsafe_allow_html=True)

# ================= DATA PH =================

data_ph={

"HCl":{"nama":"Asam Klorida","jenis":"Asam kuat","valensi":1,"Mr":36.46},
"H2SO4":{"nama":"Asam Sulfat","jenis":"Asam kuat","valensi":2,"Mr":98.08},
"HNO3":{"nama":"Asam Nitrat","jenis":"Asam kuat","valensi":1,"Mr":63.01},
"HClO4":{"nama":"Asam Perklorat","jenis":"Asam kuat","valensi":1,"Mr":100.46},
"HBr":{"nama":"Asam Bromida","jenis":"Asam kuat","valensi":1,"Mr":80.91},
"HI":{"nama":"Asam Iodida","jenis":"Asam kuat","valensi":1,"Mr":127.91},

"CH3COOH":{"nama":"Asam Asetat","jenis":"Asam lemah","Ka":1.8e-5,"Mr":60.05},
"HF":{"nama":"Asam Fluorida","jenis":"Asam lemah","Ka":6.8e-4,"Mr":20.01},
"HCOOH":{"nama":"Asam Format","jenis":"Asam lemah","Ka":1.8e-4,"Mr":46.03},
"H3PO4":{"nama":"Asam Fosfat","jenis":"Asam lemah","Ka":7.5e-3,"Mr":98.00},
"H2CO3":{"nama":"Asam Karbonat","jenis":"Asam lemah","Ka":4.3e-7,"Mr":62.03},
"HCN":{"nama":"Asam Sianida","jenis":"Asam lemah","Ka":4.9e-10,"Mr":27.03},

"NaOH":{"nama":"Natrium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":40.00},
"KOH":{"nama":"Kalium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":56.11},
"Ba(OH)2":{"nama":"Barium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":171.34},
"Ca(OH)2":{"nama":"Kalsium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":74.09},
"LiOH":{"nama":"Litium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":23.95},

"NH3":{"nama":"Amonia","jenis":"Basa lemah","Kb":1.8e-5,"Mr":17.03},
"NH4OH":{"nama":"Amonium Hidroksida","jenis":"Basa lemah","Kb":1.8e-5,"Mr":35.05},
"CH3NH2":{"nama":"Metilamina","jenis":"Basa lemah","Kb":4.4e-4,"Mr":31.06},
"C2H5NH2":{"nama":"Etilamina","jenis":"Basa lemah","Kb":5.6e-4,"Mr":45.08},
"C5H5N":{"nama":"Piridina","jenis":"Basa lemah","Kb":1.7e-9,"Mr":79.10}

}

# ================= DATABASE =================

db={

"HCl":["Asam Klorida","Asam kuat","36.46 g/mol","Korosif","Cairan bening","H-Cl"],
"H2SO4":["Asam Sulfat","Asam kuat","98.08 g/mol","Sangat korosif","Cairan kental","HO-SO2-OH"],
"HNO3":["Asam Nitrat","Asam kuat","63.01 g/mol","Oksidator kuat","Cairan bening","O=N(OH)=O"],
"CH3COOH":["Asam Asetat","Asam lemah","60.05 g/mol","Iritasi kulit","Cairan bening","CH3-COOH"],
"HF":["Asam Fluorida","Asam lemah","20.01 g/mol","Sangat beracun","Cairan bening","H-F"],
"NaOH":["Natrium Hidroksida","Basa kuat","40.00 g/mol","Korosif","Padatan putih","Na-OH"],
"KOH":["Kalium Hidroksida","Basa kuat","56.11 g/mol","Korosif","Padatan putih","K-OH"],
"Ca(OH)2":["Kalsium Hidroksida","Basa kuat","74.09 g/mol","Iritasi","Serbuk putih","Ca-(OH)2"],
"NH3":["Amonia","Basa lemah","17.03 g/mol","Gas beracun","Gas tidak berwarna","NH3"],
"NH4OH":["Amonium Hidroksida","Basa lemah","35.05 g/mol","Iritasi paru","Cairan bening","NH4OH"],

"NaCl":["Natrium Klorida","Garam","58.44 g/mol","Relatif aman","Kristal putih","Na-Cl"],
"KCl":["Kalium Klorida","Garam","74.55 g/mol","Iritasi ringan","Kristal putih","K-Cl"],
"AgNO3":["Perak Nitrat","Garam","169.87 g/mol","Oksidator","Kristal putih","Ag-NO3"],
"CuSO4":["Tembaga Sulfat","Garam","159.61 g/mol","Beracun","Kristal biru","Cu-SO4"],
"FeCl3":["Besi(III) Klorida","Garam","162.20 g/mol","Korosif","Kristal coklat","Fe-Cl3"],
"MgSO4":["Magnesium Sulfat","Garam","120.37 g/mol","Iritasi ringan","Kristal putih","Mg-SO4"],
"Na2CO3":["Natrium Karbonat","Garam basa","105.99 g/mol","Iritasi","Serbuk putih","Na2-CO3"],
"NaHCO3":["Natrium Bikarbonat","Garam basa","84.01 g/mol","Relatif aman","Serbuk putih","Na-HCO3"],
"C2H5OH":["Etanol","Alkohol","46.07 g/mol","Mudah terbakar","Cairan bening","CH3-CH2-OH"],
"CH3OH":["Metanol","Alkohol","32.04 g/mol","Beracun","Cairan bening","CH3-OH"],

"Acetone":["Aseton","Keton","58.08 g/mol","Mudah terbakar","Cairan bening","CH3-CO-CH3"],
"Benzene":["Benzena","Aromatik","78.11 g/mol","Karsinogen","Cairan bening","C6H6"],
"Toluene":["Toluena","Aromatik","92.14 g/mol","Beracun","Cairan bening","C6H5-CH3"],
"Glucose":["Glukosa","Karbohidrat","180.16 g/mol","Relatif aman","Kristal putih","C6H12O6"],
"Sucrose":["Sukrosa","Karbohidrat","342.30 g/mol","Relatif aman","Kristal putih","C12H22O11"],
"Urea":["Urea","Amida","60.06 g/mol","Iritasi ringan","Kristal putih","NH2-CO-NH2"],
"KMnO4":["Kalium Permanganat","Oksidator","158.04 g/mol","Oksidator kuat","Kristal ungu","KMnO4"],
"K2Cr2O7":["Kalium Dikromat","Oksidator","294.18 g/mol","Toksik","Kristal oranye","K2Cr2O7"],
"Pb(NO3)2":["Timbal Nitrat","Garam","331.20 g/mol","Beracun","Kristal putih","Pb(NO3)2"],
"ZnSO4":["Seng Sulfat","Garam","161.44 g/mol","Iritasi","Kristal putih","ZnSO4"]

}

# ================= SIDEBAR =================

menu=st.sidebar.radio(
"🧪 ChemAssist Pro",
["Home","Larutan","pH","Informasi Bahan Kimia","Analisis Kimia","Tentang"]
)

# ================= HOME =================

if menu=="Home":

    st.markdown("""
    <div class='header'>
    <div class='home-title'>🧪 ChemAssist Pro</div>
    <div class='home-sub'>
    Membuat analisis kimia menjadi lebih mudah, modern, interaktif, dan menyenangkan
    </div>
    </div>
    """, unsafe_allow_html=True)

    a,b,c=st.columns(3)

    with a:
        st.markdown("""
        <div class='metric-box'>
        <h2>📚 30+</h2>
        <p>Informasi Senyawa</p>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class='metric-box'>
        <h2>⚗️ 20+</h2>
        <p>Data pH Senyawa</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class='metric-box'>
        <h2>🚀 4.0</h2>
        <p>Application Version</p>
        </div>
        """, unsafe_allow_html=True)

# ================= LARUTAN =================

elif menu=="Larutan":

    st.title("💧 Smart Solution Maker")

    senyawa=st.selectbox(
        "Pilih Senyawa",
        list(data_ph.keys()),
        format_func=lambda x:f"{data_ph[x]['nama']} ({x})"
    )

    info=data_ph[senyawa]

    st.info(f"""
🧪 Nama Senyawa : {info['nama']}

📌 Rumus Kimia : {senyawa}

⚖️ Mr : {info['Mr']} g/mol
""")

    metode=st.selectbox(
        "Pilih Jenis Perhitungan",
        ["Pembuatan Larutan","Pengenceran"]
    )

    if metode=="Pembuatan Larutan":

        M=st.number_input("Konsentrasi Larutan (M)",0.1)
        V=st.number_input("Volume Larutan (mL)",100.0)

        if st.button("Hitung Massa Senyawa"):

            massa=(info['Mr']*M*V)/1000

            st.success(f"Massa senyawa yang diperlukan = {massa:.4f} gram")

    else:

        M1=st.number_input("Molaritas Awal",1.0)
        V1=st.number_input("Volume Awal (mL)",100.0)
        M2=st.number_input("Molaritas Akhir",0.1)

        if st.button("Hitung Pengenceran"):

            V2=(M1*V1)/M2

            st.success(f"Volume akhir larutan = {V2:.2f} mL")

# ================= PH =================

elif menu=="pH":

    st.title("⚗️ Smart pH Calculator")

    senyawa=st.selectbox(
        "Pilih Senyawa",
        list(data_ph.keys()),
        format_func=lambda x:f"{data_ph[x]['nama']} ({x})"
    )

    info=data_ph[senyawa]

    C=st.number_input("Masukkan Konsentrasi (M)",0.01)

    if st.button("Hitung pH"):

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

        st.metric("Nilai pH",f"{ph:.2f}")

        if ph<=1:
            st.error("🔴 Sangat Asam")

        elif ph<=3:
            st.warning("🟠 Asam")

        elif ph<=6:
            st.info("🟡 Asam Lemah")

        elif ph==7:
            st.success("🟢 Netral")

        elif ph<=11:
            st.info("🔵 Basa Lemah")

        elif ph<=13:
            st.warning("🟣 Basa")

        else:
            st.error("⚫ Sangat Basa")

# ================= INFORMASI BAHAN =================

elif menu=="Informasi Bahan Kimia":

    st.title("📚 Informasi Bahan Kimia")

    pilih=st.selectbox("Pilih Senyawa",list(db.keys()))

    data=db[pilih]

    st.success(f"""
🧪 Nama Senyawa : {data[0]}

📌 Rumus Kimia : {pilih}

⚗️ Jenis : {data[1]}

⚖️ Mr : {data[2]}

⚠️ Bahaya : {data[3]}

🎨 Bentuk/Fisik : {data[4]}

🧬 Struktur Molekul : {data[5]}
""")

# ================= ANALISIS =================

elif menu=="Analisis Kimia":

    st.title("🧪 Smart Chemical Analysis")

    fakta=random.choice([
        "Larutan asam kuat terionisasi sempurna di dalam air.",
        "NaOH merupakan salah satu basa kuat paling umum di laboratorium.",
        "H2SO4 digunakan pada baterai kendaraan.",
        "Etanol digunakan sebagai antiseptik.",
        "pH menentukan tingkat keasaman larutan."
    ])

    st.info(f"🧠 Fakta Kimia : {fakta}")

# ================= TENTANG =================

elif menu=="Tentang":

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("""
<div class='info-box'>

<h3>🧪 ChemAssist Pro</h3>

Aplikasi laboratorium kimia interaktif berbasis Python dan Streamlit.

</div>
""", unsafe_allow_html=True)
