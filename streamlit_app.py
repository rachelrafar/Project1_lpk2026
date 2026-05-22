import streamlit as st
import math
import time
import random

# ================= CONFIG =================

st.set_page_config(
    page_title="ChemAssist Pro",
    page_icon="🧪",
    layout="centered"
)

# ================= STYLE =================

st.markdown("""
<style>

html, body, [class*="css"]{
font-family:'Segoe UI',sans-serif;
}

.stApp{
background:linear-gradient(to bottom,#edf4ff,#ffffff);
}

.header{
padding:40px;
border-radius:30px;
background:white;
text-align:center;
box-shadow:0px 6px 20px rgba(0,0,0,.12);
margin-bottom:25px;
}

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

.info-box{
padding:20px;
background:white;
border-radius:20px;
box-shadow:0px 4px 12px rgba(0,0,0,.1);
margin-top:10px;
}

.stButton>button{
width:100%;
height:52px;
border-radius:14px;
font-size:16px;
font-weight:bold;
border:none;
}

.stCode{
font-family:'Segoe UI',sans-serif !important;
font-size:15px !important;
border-radius:15px;
}

code{
font-family:'Segoe UI',sans-serif !important;
}

.home-title{
font-size:45px;
font-weight:bold;
color:#003366;
}

.home-sub{
font-size:18px;
color:#666666;
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

"HBr":{"nama":"Asam Bromida","jenis":"Asam kuat","valensi":1,"Mr":80.91},

"HI":{"nama":"Asam Iodida","jenis":"Asam kuat","valensi":1,"Mr":127.91},

"CH3COOH":{"nama":"Asam Asetat","jenis":"Asam lemah","Ka":1.8e-5,"Mr":60.05},

"HF":{"nama":"Asam Fluorida","jenis":"Asam lemah","Ka":6.8e-4,"Mr":20.01},

"HCOOH":{"nama":"Asam Format","jenis":"Asam lemah","Ka":1.8e-4,"Mr":46.03},

"H3PO4":{"nama":"Asam Fosfat","jenis":"Asam lemah","Ka":7.5e-3,"Mr":98.00},

"H2CO3":{"nama":"Asam Karbonat","jenis":"Asam lemah","Ka":4.3e-7,"Mr":62.03},

"NaOH":{"nama":"Natrium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":40.00},

"KOH":{"nama":"Kalium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":56.11},

"Ba(OH)2":{"nama":"Barium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":171.34},

"Ca(OH)2":{"nama":"Kalsium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":74.09},

"Sr(OH)2":{"nama":"Stronsium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":121.63},

"NH3":{"nama":"Amonia","jenis":"Basa lemah","Kb":1.8e-5,"Mr":17.03},

"NH4OH":{"nama":"Amonium Hidroksida","jenis":"Basa lemah","Kb":1.8e-5,"Mr":35.05},

"CH3NH2":{"nama":"Metilamina","jenis":"Basa lemah","Kb":4.4e-4,"Mr":31.06},

"C2H5NH2":{"nama":"Etilamina","jenis":"Basa lemah","Kb":5.6e-4,"Mr":45.08}

}

# ================= INFORMASI BAHAN KIMIA =================

db={

"HCl":[
"Asam Klorida",
"Asam kuat",
"36.46 g/mol",
"Korosif dan menyebabkan iritasi",
"Cairan bening",
"Digunakan dalam laboratorium dan industri"
],

"H2SO4":[
"Asam Sulfat",
"Asam kuat",
"98.08 g/mol",
"Sangat korosif",
"Cairan kental bening",
"Digunakan dalam aki dan industri pupuk"
],

"HNO3":[
"Asam Nitrat",
"Asam kuat",
"63.01 g/mol",
"Oksidator kuat",
"Cairan bening kekuningan",
"Digunakan untuk pembuatan pupuk"
],

"HClO4":[
"Asam Perklorat",
"Asam kuat",
"100.46 g/mol",
"Korosif dan oksidator",
"Cairan bening",
"Digunakan pada analisis kimia"
],

"HBr":[
"Asam Bromida",
"Asam kuat",
"80.91 g/mol",
"Korosif",
"Cairan bening",
"Digunakan dalam sintesis kimia"
],

"HI":[
"Asam Iodida",
"Asam kuat",
"127.91 g/mol",
"Korosif",
"Cairan bening",
"Digunakan sebagai pereaksi"
],

"CH3COOH":[
"Asam Asetat",
"Asam lemah",
"60.05 g/mol",
"Iritasi mata dan kulit",
"Cairan bening",
"Bahan utama cuka"
],

"HF":[
"Asam Fluorida",
"Asam lemah",
"20.01 g/mol",
"Sangat beracun",
"Cairan bening",
"Digunakan untuk etsa kaca"
],

"HCOOH":[
"Asam Format",
"Asam lemah",
"46.03 g/mol",
"Korosif",
"Cairan tidak berwarna",
"Digunakan pada industri tekstil"
],

"H3PO4":[
"Asam Fosfat",
"Asam lemah",
"98.00 g/mol",
"Iritasi kulit",
"Cairan bening",
"Digunakan pada minuman ringan"
],

"H2CO3":[
"Asam Karbonat",
"Asam lemah",
"62.03 g/mol",
"Iritasi ringan",
"Cairan",
"Terdapat pada minuman bersoda"
],

"NaOH":[
"Natrium Hidroksida",
"Basa kuat",
"40.00 g/mol",
"Korosif",
"Padatan putih",
"Digunakan untuk pembuatan sabun"
],

"KOH":[
"Kalium Hidroksida",
"Basa kuat",
"56.11 g/mol",
"Korosif",
"Padatan putih",
"Digunakan pada baterai alkali"
],

"Ba(OH)2":[
"Barium Hidroksida",
"Basa kuat",
"171.34 g/mol",
"Berbahaya jika tertelan",
"Padatan putih",
"Digunakan pada laboratorium"
],

"Ca(OH)2":[
"Kalsium Hidroksida",
"Basa kuat",
"74.09 g/mol",
"Iritasi",
"Serbuk putih",
"Digunakan pada kapur"
],

"Sr(OH)2":[
"Stronsium Hidroksida",
"Basa kuat",
"121.63 g/mol",
"Iritasi kulit",
"Padatan putih",
"Digunakan dalam industri gula"
],

"NH3":[
"Amonia",
"Basa lemah",
"17.03 g/mol",
"Gas beracun",
"Gas tidak berwarna",
"Digunakan pada pupuk"
],

"NH4OH":[
"Amonium Hidroksida",
"Basa lemah",
"35.05 g/mol",
"Iritasi paru-paru",
"Cairan bening",
"Digunakan pada pembersih"
],

"CH3NH2":[
"Metilamina",
"Basa lemah",
"31.06 g/mol",
"Beracun",
"Gas tidak berwarna",
"Digunakan pada sintesis organik"
],

"C2H5NH2":[
"Etilamina",
"Basa lemah",
"45.08 g/mol",
"Mudah terbakar",
"Cairan tidak berwarna",
"Digunakan pada industri farmasi"
],

"NaCl":[
"Natrium Klorida",
"Garam",
"58.44 g/mol",
"Relatif aman",
"Kristal putih",
"Garam dapur"
],

"KCl":[
"Kalium Klorida",
"Garam",
"74.55 g/mol",
"Iritasi ringan",
"Kristal putih",
"Digunakan pada pupuk"
],

"AgNO3":[
"Perak Nitrat",
"Garam",
"169.87 g/mol",
"Oksidator",
"Kristal putih",
"Digunakan pada fotografi"
],

"CuSO4":[
"Tembaga Sulfat",
"Garam",
"159.61 g/mol",
"Beracun",
"Kristal biru",
"Digunakan pada fungisida"
],

"FeCl3":[
"Besi(III) Klorida",
"Garam",
"162.20 g/mol",
"Korosif",
"Kristal coklat",
"Digunakan untuk etsa PCB"
],

"MgSO4":[
"Magnesium Sulfat",
"Garam",
"120.37 g/mol",
"Iritasi ringan",
"Kristal putih",
"Dikenal sebagai garam inggris"
],

"Na2CO3":[
"Natrium Karbonat",
"Garam basa",
"105.99 g/mol",
"Iritasi kulit",
"Serbuk putih",
"Digunakan pada deterjen"
],

"NaHCO3":[
"Natrium Bikarbonat",
"Garam basa",
"84.01 g/mol",
"Relatif aman",
"Serbuk putih",
"Digunakan pada baking soda"
],

"C2H5OH":[
"Etanol",
"Alkohol",
"46.07 g/mol",
"Mudah terbakar",
"Cairan bening",
"Digunakan sebagai antiseptik"
],

"CH3OH":[
"Metanol",
"Alkohol",
"32.04 g/mol",
"Beracun",
"Cairan bening",
"Digunakan sebagai pelarut"
],

"Acetone":[
"Aseton",
"Keton",
"58.08 g/mol",
"Sangat mudah terbakar",
"Cairan bening",
"Digunakan sebagai pelarut"
]

}

# ================= SIDEBAR =================

menu=st.sidebar.radio(
"🧪 ChemAssist Pro",
["Home","Larutan","pH","Informasi Bahan Kimia","Mini Quiz","Tentang"],
index=["Home","Larutan","pH","Informasi Bahan Kimia","Mini Quiz","Tentang"].index(
st.session_state.page
)
)

st.session_state.page=menu

# ================= HOME =================

if menu=="Home":

    st.markdown("""
    <div class='header'>
    <div class='home-title'>🧪 ChemAssist Pro</div>
    <div class='home-sub'>
    Membuat analisis kimia menjadi lebih mudah, interaktif, dan menyenangkan
    </div>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    c1.metric("📚 Database",f"{len(db)} Senyawa")
    c2.metric("⚗️ Sistem pH",f"{len(data_ph)} Data")
    c3.metric("🚀 Version","4.0")

    st.markdown("## 🔥 Main Features")

    a,b,c=st.columns(3)

    with a:

        st.markdown("""
        <div class='card'>
        <h3>💧 Smart Solution Maker</h3>
        <p>Membantu pembuatan larutan dan pengenceran secara otomatis</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Menu Larutan"):
            st.session_state.page="Larutan"
            st.rerun()

    with b:

        st.markdown("""
        <div class='card'>
        <h3>⚗️ Smart pH Calculator</h3>
        <p>Perhitungan pH cepat untuk asam dan basa</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Kalkulator pH"):
            st.session_state.page="pH"
            st.rerun()

    with c:

        st.markdown("""
        <div class='card'>
        <h3>📚 Informasi Bahan Kimia</h3>
        <p>Database senyawa lengkap dengan informasi penting</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Informasi Bahan"):
            st.session_state.page="Informasi Bahan Kimia"
            st.rerun()
