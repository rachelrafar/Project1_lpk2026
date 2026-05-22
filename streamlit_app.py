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

# ================= HIDE KEYBOARD DOUBLE =================

st.markdown("""
<style>

[data-testid="collapsedControl"] svg {
display: none !important;
}

[data-testid="collapsedControl"] {
background: transparent !important;
border: none !important;
width: 0px !important;
height: 0px !important;
padding: 0px !important;
margin: 0px !important;
min-width: 0px !important;
min-height: 0px !important;
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

.header{
padding:45px;
border-radius:30px;
background:linear-gradient(135deg,#0f4c81,#4da8ff);
text-align:center;
box-shadow:0px 6px 20px rgba(0,0,0,.15);
margin-bottom:25px;
color:white;
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
background:linear-gradient(90deg,#0f4c81,#4da8ff);
color:white;
font-family:'Segoe UI',sans-serif !important;
}

.home-title{
font-size:48px;
font-weight:bold;
}

.home-sub{
font-size:18px;
opacity:0.95;
}

.feature-title{
font-size:20px;
font-weight:bold;
color:#0f4c81;
}

</style>
""", unsafe_allow_html=True)

# ================= SESSION =================

if "page" not in st.session_state:
    st.session_state.page="Home"

# ================= DATA PH =================

data_ph={

"HCl":{"nama":"Asam Klorida","jenis":"Asam kuat","valensi":1,"Mr":36.46},
"H2SO4":{"nama":"Asam Sulfat","jenis":"Asam kuat","valensi":2,"Mr":98.08},
"HNO3":{"nama":"Asam Nitrat","jenis":"Asam kuat","valensi":1,"Mr":63.01},
"HClO4":{"nama":"Asam Perklorat","jenis":"Asam kuat","valensi":1,"Mr":100.46},
"HBr":{"nama":"Asam Bromida","jenis":"Asam kuat","valensi":1,"Mr":80.91},
"HI":{"nama":"Asam Iodida","jenis":"Asam kuat","valensi":1,"Mr":127.91},
"HClO3":{"nama":"Asam Klorat","jenis":"Asam kuat","valensi":1,"Mr":84.46},
"HClO":{"nama":"Asam Hipoklorit","jenis":"Asam lemah","Ka":3e-8,"Mr":52.46},
"CH3COOH":{"nama":"Asam Asetat","jenis":"Asam lemah","Ka":1.8e-5,"Mr":60.05},
"HF":{"nama":"Asam Fluorida","jenis":"Asam lemah","Ka":6.8e-4,"Mr":20.01},
"HCOOH":{"nama":"Asam Format","jenis":"Asam lemah","Ka":1.8e-4,"Mr":46.03},
"H3PO4":{"nama":"Asam Fosfat","jenis":"Asam lemah","Ka":7.5e-3,"Mr":98.00},
"H2CO3":{"nama":"Asam Karbonat","jenis":"Asam lemah","Ka":4.3e-7,"Mr":62.03},
"HCN":{"nama":"Asam Sianida","jenis":"Asam lemah","Ka":4.9e-10,"Mr":27.03},
"H2S":{"nama":"Asam Sulfida","jenis":"Asam lemah","Ka":1e-7,"Mr":34.08},

"NaOH":{"nama":"Natrium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":40.00},
"KOH":{"nama":"Kalium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":56.11},
"Ba(OH)2":{"nama":"Barium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":171.34},
"Ca(OH)2":{"nama":"Kalsium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":74.09},
"Sr(OH)2":{"nama":"Stronsium Hidroksida","jenis":"Basa kuat","valensi":2,"Mr":121.63},
"LiOH":{"nama":"Litium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":23.95},
"RbOH":{"nama":"Rubidium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":102.47},

"NH3":{"nama":"Amonia","jenis":"Basa lemah","Kb":1.8e-5,"Mr":17.03},
"NH4OH":{"nama":"Amonium Hidroksida","jenis":"Basa lemah","Kb":1.8e-5,"Mr":35.05},
"CH3NH2":{"nama":"Metilamina","jenis":"Basa lemah","Kb":4.4e-4,"Mr":31.06},
"C2H5NH2":{"nama":"Etilamina","jenis":"Basa lemah","Kb":5.6e-4,"Mr":45.08},
"C5H5N":{"nama":"Piridina","jenis":"Basa lemah","Kb":1.7e-9,"Mr":79.10},
"Al(OH)3":{"nama":"Aluminium Hidroksida","jenis":"Basa lemah","Kb":1e-9,"Mr":78.00}

}

# ================= DATABASE =================

db={

"HCl":["Asam Klorida","Asam kuat","36.46 g/mol","Korosif","Cairan bening","H-Cl"],
"H2SO4":["Asam Sulfat","Asam kuat","98.08 g/mol","Sangat korosif","Cairan kental","HO-SO2-OH"],
"HNO3":["Asam Nitrat","Asam kuat","63.01 g/mol","Oksidator kuat","Cairan bening","O=N(OH)=O"],
"CH3COOH":["Asam Asetat","Asam lemah","60.05 g/mol","Iritasi kulit","Cairan bening","CH3-COOH"],
"HF":["Asam Fluorida","Asam lemah","20.01 g/mol","Sangat beracun","Cairan bening","H-F"]

}

# ================= SIDEBAR =================

menu=st.sidebar.radio(
"🧪 ChemAssist Pro",
["Home","Larutan","pH","Informasi Bahan Kimia","Analisis Kimia","Tentang"],
index=["Home","Larutan","pH","Informasi Bahan Kimia","Analisis Kimia","Tentang"].index(
st.session_state.page
)
)

st.session_state.page=menu
