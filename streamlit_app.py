# ================= IMPORT =================

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px
import random
import time
import math
import json
import os
import hashlib
from datetime import datetime

# ================= PAGE CONFIG =================

st.set_page_config(

    page_title="ChemAssist Ultra",

    page_icon="🧪",

    layout="wide",

    initial_sidebar_state="expanded"
)

USER_FILE = "users.json"

if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ================= SESSION =================

if "login" not in st.session_state:
    st.session_state.login = False

if "history" not in st.session_state:
    st.session_state.history = []
    
if "username" not in st.session_state:
    st.session_state.username = ""

if "nama" not in st.session_state:
    st.session_state.nama = ""

st.markdown("""
<style>

/* ================= BACKGROUND ================= */

.stApp{
    background:linear-gradient(
        135deg,
        #F0F9FF,
        #E0F2FE,
        #BAE6FD,
        #7DD3FC
    ) !important;
}

.main{
    background: transparent !important;
}

.block-container{
    padding-top: 2rem;
}

/* ================= TITLE ================= */

.login-title{
    text-align:center;
    font-size:58px;
    font-weight:900;
    color:#1E3A8A;
    margin-bottom:5px;
}

.login-sub{
    text-align:center;
    color:#475569;
    font-size:18px;
    margin-bottom:35px;
}

/* ================= LOGIN BOX ================= */

.stTabs{
    background:rgba(255,255,255,0.92) !important;
    backdrop-filter:blur(20px);
    padding:35px !important;
    border-radius:30px !important;
    border:1px solid rgba(255,255,255,0.5);
    box-shadow:0 15px 40px rgba(37,99,235,0.15) !important;
}

button[data-baseweb="tab"]{
    font-size:16px !important;
    font-weight:700 !important;
}

/* ================= WELCOME ================= */

.login-box-title{
    text-align:center;
    font-size:32px;
    font-weight:800;
    color:#1E3A8A;
    margin-bottom:8px;
}

.login-box-sub{
    text-align:center;
    color:#64748B;
    margin-bottom:30px;
}

/* ================= INPUT ================= */

div[data-baseweb="input"]{
    background:white !important;
    border-radius:15px !important;
    border:2px solid #DBEAFE !important;
}

.stTextInput input{
    background:white !important;
    border:none !important;
    font-size:16px !important;
}

.stTextInput input:focus{
    box-shadow:none !important;
}

/* ================= BUTTON ================= */

.stButton button{
    width:100% !important;
    height:52px !important;
    border:none !important;
    border-radius:15px !important;

    font-size:16px !important;
    font-weight:700 !important;

    color:white !important;

    background:linear-gradient(
        90deg,
        #60A5FA,
        #2563EB
    ) !important;

    box-shadow:0 8px 20px rgba(37,99,235,0.25);
}

.stButton button:hover{
    transform:translateY(-2px);
}

/* ================= SUCCESS ERROR ================= */

.stSuccess,
.stError,
.stWarning{
    border-radius:12px !important;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"]{
    background:rgba(255,255,255,0.55);
    backdrop-filter:blur(20px);
    border-right:1px solid rgba(255,255,255,0.4);
}

/* ================= CARD ================= */

.card{
    background:rgba(255,255,255,0.7);
    backdrop-filter:blur(18px);
    border-radius:25px;
    padding:25px;
    margin-bottom:20px;
    border:1px solid rgba(255,255,255,0.4);
    box-shadow:0 8px 24px rgba(37,99,235,0.12);
}

/* ================= METRIC ================= */

.metric-box{
    background:rgba(255,255,255,0.75);
    backdrop-filter:blur(18px);
    border-radius:25px;
    padding:25px;
    text-align:center;
    box-shadow:0 8px 24px rgba(37,99,235,0.12);
}

.metric-box h2{
    font-size:40px;
    margin-bottom:5px;
}

.metric-box h3{
    color:#2563EB;
    font-size:32px;
    font-weight:800;
}

.metric-box p{
    color:#475569;
}

/* ================= HOME ================= */

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:900;
    color:#2563EB;
}

.subtitle{
    text-align:center;
    color:#1E40AF;
    font-size:18px;
}

/* ================= FEATURE ================= */

.feature-title{
    color:#2563EB;
    font-size:22px;
    font-weight:700;
}

.feature-desc{
    color:#475569;
    line-height:1.6;
}

/* ================= ABOUT ================= */

.tentang-box{
    background:rgba(255,255,255,0.7);
    backdrop-filter:blur(15px);
    border-radius:25px;
    padding:30px;
    border:1px solid rgba(255,255,255,0.4);
}

.tentang-box h2,
.tentang-box h3{
    color:#2563EB;
}

.tentang-box p,
.tentang-box li{
    color:#334155;
}

/* ================= CHEM ICON ================= */

.chem-bg{
    position:fixed;
    left:50px;
    top:250px;
    font-size:180px;
    opacity:0.08;
    z-index:0;
}

.chem-bg2{
    position:fixed;
    right:70px;
    bottom:80px;
    font-size:180px;
    opacity:0.08;
    z-index:0;
}

/* ================= SCROLLBAR ================= */

::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#60A5FA;
    border-radius:20px;
}

/* ================= LOGIN TABS ================= */

.stTabs{
    background:rgba(255,255,255,0.85);
    backdrop-filter:blur(20px);
    padding:30px;
    border-radius:25px;
    box-shadow:0 10px 30px rgba(37,99,235,0.15);
}

button[data-baseweb="tab"]{
    font-size:16px !important;
    font-weight:700 !important;
}

.login-box-title{
    text-align:center;
    font-size:28px;
    font-weight:800;
    color:#2563EB;
    margin-bottom:20px;
}

.login-box{

    background:rgba(255,255,255,0.55);

    padding:40px;

    border-radius:30px;

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,0.5);

    box-shadow:
        0 10px 30px rgba(37,99,235,0.20);

    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN PAGE =================

if not st.session_state.login:

    users = load_users()

    st.markdown("""
    <div class='login-title'>
        🧪 ChemAssist Ultra
    </div>

    <div class='login-sub'>
        Smart Chemical Analysis Platform
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown("""
        <div class="login-box">
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs([
            "🔐 Sign In",
            "📝 Sign Up"
        ])

        # ================= SIGN IN =================

        with tab1:

            st.markdown("""
            <div class='login-box-title'>
                Welcome Back 👋
            </div>
            """, unsafe_allow_html=True)

            username = st.text_input(
                "Username",
                key="login_username"
            )

            password = st.text_input(
                "Password",
                type="password",
                key="login_password"
            )

            if st.button(
                "🚀 Login",
                key="btn_login",
                use_container_width=True
            ):

                if username in users:

                    if users[username]["password"] == hash_password(password):

                        users[username]["last_login"] = (
                            datetime.now().strftime(
                                "%d-%m-%Y %H:%M:%S"
                            )
                        )

                        save_users(users)

                        st.session_state.login = True
                        st.session_state.username = username
                        st.session_state.nama = users[username]["nama"]

                        st.success("Login berhasil ✅")

                        time.sleep(1)

                        st.rerun()

                    else:

                        st.error("Password salah")

                else:

                    st.error("Username tidak ditemukan")

        # ================= SIGN UP =================

        with tab2:

            st.markdown("""
            <div class='login-box-title'>
                Create Account ✨
            </div>
            """, unsafe_allow_html=True)

            nama = st.text_input(
                "Nama Lengkap",
                key="signup_nama"
            )

            email = st.text_input(
                "Email",
                key="signup_email"
            )

            username_baru = st.text_input(
                "Username",
                key="signup_username"
            )

            password_baru = st.text_input(
                "Password",
                type="password",
                key="signup_password"
            )

            konfirmasi = st.text_input(
                "Konfirmasi Password",
                type="password",
                key="signup_konfirmasi"
            )

            if st.button(
                "📝 Daftar",
                key="btn_signup",
                use_container_width=True
            ):

                if username_baru in users:

                    st.error("Username sudah digunakan")

                elif password_baru != konfirmasi:

                    st.error(
                        "Konfirmasi password tidak cocok"
                    )

                elif (
                    nama == ""
                    or email == ""
                    or username_baru == ""
                    or password_baru == ""
                ):

                    st.warning(
                        "Semua data wajib diisi"
                    )

                else:

                    users[username_baru] = {
                        "nama": nama,
                        "email": email,
                        "password": hash_password(
                            password_baru
                        ),
                        "last_login": datetime.now().strftime(
                            "%d-%m-%Y %H:%M:%S"
                        )
                    }

                    save_users(users)

                    st.success(
                        "Akun berhasil dibuat 🎉"
                    )

                    time.sleep(1)

                    st.rerun()

        st.markdown("""
        </div>
        """, unsafe_allow_html=True)

    st.stop()
    
# ================= HEADER =================

st.markdown("""
<div class="logo">🧪</div>

<div class="main-title">
ChemAssist Ultra
</div>

<div class="subtitle">
Next Generation Chemistry Dashboard
</div>
""", unsafe_allow_html=True)

# ================= SESSION =================

if "direct_menu" not in st.session_state:
    st.session_state["direct_menu"] = "🏠 Home"

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
"ZnSO4":["Seng Sulfat","Garam","161.44 g/mol","Iritasi","Kristal putih","ZnSO4"],

"Na2SO4":["Natrium Sulfat","Garam","142.04 g/mol","Iritasi ringan","Kristal putih","Na2SO4"],
"HgCl2":["Merkuri(II) Klorida","Garam","271.50 g/mol","Sangat beracun","Kristal putih","HgCl2"],
"CHCl3":["Kloroform","Pelarut","119.38 g/mol","Beracun jika terhirup","Cairan bening","CHCl3"],
"CCl4":["Karbon Tetraklorida","Pelarut","153.82 g/mol","Toksik","Cairan bening","CCl4"],
"H2O2":["Hidrogen Peroksida","Oksidator","34.01 g/mol","Oksidator kuat","Cairan bening","H-O-O-H"],
"NaNO3":["Natrium Nitrat","Garam","85.00 g/mol","Oksidator","Kristal putih","NaNO3"],
"NH4Cl":["Amonium Klorida","Garam","53.49 g/mol","Iritasi","Kristal putih","NH4Cl"],
"NH4NO3":["Amonium Nitrat","Garam","80.04 g/mol","Oksidator","Kristal putih","NH4NO3"],
"CaCO3":["Kalsium Karbonat","Garam","100.09 g/mol","Iritasi ringan","Serbuk putih","CaCO3"],
"MgCl2":["Magnesium Klorida","Garam","95.21 g/mol","Iritasi ringan","Kristal putih","MgCl2"],
"Al2(SO4)3":["Aluminium Sulfat","Garam","342.15 g/mol","Iritasi","Kristal putih","Al2(SO4)3"],
"H3BO3":["Asam Borat","Asam lemah","61.83 g/mol","Iritasi ringan","Kristal putih","B(OH)3"],
"NaClO":["Natrium Hipoklorit","Oksidator","74.44 g/mol","Korosif","Cairan kuning pucat","NaClO"],
"CH3COCH3":["Aseton","Keton","58.08 g/mol","Mudah terbakar","Cairan bening","CH3-CO-CH3"],
"C6H12O6":["Glukosa","Karbohidrat","180.16 g/mol","Relatif aman","Kristal putih","C6H12O6"],
"C12H22O11":["Sukrosa","Karbohidrat","342.30 g/mol","Relatif aman","Kristal putih","C12H22O11"],
"FeSO4":["Besi(II) Sulfat","Garam","151.91 g/mol","Iritasi","Kristal hijau","FeSO4"],
"CuCl2":["Tembaga(II) Klorida","Garam","134.45 g/mol","Beracun","Kristal hijau","CuCl2"],
"Na3PO4":["Natrium Fosfat","Garam basa","163.94 g/mol","Iritasi","Serbuk putih","Na3PO4"],
"KNO3":["Kalium Nitrat","Garam","101.10 g/mol","Oksidator","Kristal putih","KNO3"]

}

# ================= NAVIGATION HELPER =================

def go_to(page_name):
    st.session_state.menu = page_name

if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Home"

# ================= SIDEBAR =================

with st.sidebar:

    if st.session_state.login:
        st.success(
            f"👤 {st.session_state.nama}"
        )
        
    users = load_users()

    if st.session_state.username in users:

        st.caption(
            f"🕒 Login terakhir: "
            f"{users[st.session_state.username]['last_login']}"
        )

    dark_mode = st.toggle("🌙 Dark Mode")

    if dark_mode:
        sidebar_bg = "#0F172A"
        nav_bg = "#1E293B"
        nav_text = "white"
    else:
        sidebar_bg = "#E0F2FE"
        nav_bg = "#FFFFFF"
        nav_text = "#0F172A"

    selected = option_menu(
        menu_title="✨ ChemAssist Menu",

        options=[
            "🏠 Home",
            "💧 Larutan",
            "⚗️ pH",
            "📚 Informasi Bahan Kimia",
            "🧪 Analisis Kimia",
            "ℹ️ Tentang"
        ],

        icons=[
            "house-fill",
            "droplet-fill",
            "eyedropper",
            "book-fill",
            "activity",
            "info-circle-fill"
        ],

        menu_icon="stars",

        default_index=[
            "🏠 Home",
            "💧 Larutan",
            "⚗️ pH",
            "📚 Informasi Bahan Kimia",
            "🧪 Analisis Kimia",
            "ℹ️ Tentang"
        ].index(st.session_state.menu),

        styles={

            "container": {
                "padding": "15px",
                "background-color": sidebar_bg,
                "border-radius": "20px",
            },

            "icon": {
                "color": "#38BDF8",
                "font-size": "20px"
            },

            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "8px",
                "padding": "12px",
                "border-radius": "14px",
                "background-color": nav_bg,
                "color": nav_text,
                "font-weight": "600",
                "--hover-color": "#334155",
            },

            "nav-link-selected": {
                "background": "linear-gradient(90deg,#38BDF8,#2563EB)",
                "color": "white",
                "font-weight": "bold",
            },
        }
    )

    st.markdown("---")

    if st.button("🚪 Logout"):
        st.session_state.login = False
        st.session_state.username = ""
        st.session_state.nama = ""
        
        st.rerun()

# ================= DARK MODE =================

if dark_mode:

    st.markdown("""
    <style>

    .stApp{
        background:linear-gradient(
        135deg,
        #020617,
        #0F172A,
        #111827
        ) !important;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"]{
        background:#0F172A !important;
    }

    section[data-testid="stSidebar"] > div{
        background:#0F172A !important;
    }

    section[data-testid="stSidebar"] *{
        color:white !important;
    }

    /* Card */
    .card{
        background:rgba(15,23,42,0.6) !important;
        border:1px solid rgba(255,255,255,0.08) !important;
        color:white !important;
    }

    /* Metric Home */
    .metric-box{
        color:white !important;
        background:rgba(15,23,42,0.6) !important;
        border:1px solid rgba(255,255,255,0.08) !important;
    }

    .metric-box h2{
        color:#38BDF8 !important;
    }

    .metric-box h3{
        color:white !important;
    }

    .metric-box p{
        color:#E2E8F0 !important;
    }

    /* Form */
    .stSelectbox label,
    .stNumberInput label,
    .stTextInput label,
    .stRadio label,
    .stSlider label{
        color:white !important;
        font-weight:600;
    }

    /* Isi selectbox & input tetap hitam */
    .stSelectbox div[data-baseweb="select"] *,
    .stNumberInput input{
        color:black !important;
    }

    /* Judul */
    h1,h2,h3,h4,h5,h6,p,span{
        color:white !important;
    }

    .metric-label{
        color:#E2E8F0 !important;
    }

    /* Halaman Tentang */
    .tentang-box,
    .tentang-box h2,
    .tentang-box h3,
    .tentang-box li,
    .tentang-box p{
        color:white !important;
    }

    </style>
    """, unsafe_allow_html=True)

menu = selected
# ================= HOME =================

if menu=="🏠 Home":

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown(f"""
        <div class='metric-box'>
        <h2>📚</h2>
        <h3>{len(db)}</h3>
        <p>Database Senyawa</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class='metric-box'>
        <h2>⚗️</h2>
        <h3>{len(data_ph)}</h3>
        <p>Data pH</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='metric-box'>
        <h2>🚀</h2>
        <h3>5.0</h3>
        <p>Modern Edition</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1,col2=st.columns(2)

    with col1:

        st.markdown("""
        <div class='card'>
            <div class='feature-title'>💧 Smart Solution Maker</div>
            <div class='feature-desc'>
            Perhitungan larutan otomatis dengan tampilan modern.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Buka Menu Larutan"):
            go_to("💧 Larutan")

        st.markdown("""
        <div class='card'>
            <div class='feature-title'>📚 Chemical Database</div>
            <div class='feature-desc'>
            Informasi senyawa lengkap dan interaktif.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📖 Informasi Kimia"):
            go_to("📚 Informasi Bahan Kimia")

    with col2:

        st.markdown("""
        <div class='card'>
            <div class='feature-title'>⚡ Smart pH Calculator</div>
            <div class='feature-desc'>
            Analisis pH cepat dengan sistem otomatis.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("⚗️ Kalkulator pH"):
            go_to("⚗️ pH")

        st.markdown("""
        <div class='card'>
            <div class='feature-title'>🧠 Chemical Analysis</div>
            <div class='feature-desc'>
            Analisis karakteristik senyawa modern.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🧪 Analisis Kimia"):
            go_to("🧪 Analisis Kimia")
        st.markdown("### 🚀 System Performance")
        
        progress=st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i+1)
        st.success("System Ready ✅")

# ================= LARUTAN =================

elif menu=="💧 Larutan":

    st.title("💧 Smart Solution Maker")

    if st.button("⬅ Kembali ke Home"):
        go_to("🏠 Home")

    senyawa = st.selectbox(
        "Pilih Senyawa",
        list(data_ph.keys()),
        format_func=lambda x: f"{data_ph[x]['nama']} ({x})"
    )

    info = data_ph[senyawa]

    st.info(f"""
🧪 Nama Senyawa : {info['nama']}

📌 Rumus Kimia : {senyawa}

⚖️ Mr : {info['Mr']} g/mol
""")

    metode = st.selectbox(
        "Pilih Jenis Perhitungan",
        ["Pembuatan Larutan", "Pengenceran"]
    )

    # ================= PEMBUATAN LARUTAN =================

    if metode == "Pembuatan Larutan":

        M = st.number_input("Konsentrasi Larutan (M)", 0.1)
        V = st.number_input("Volume Larutan (mL)", 100.0)

        if st.button("Hitung Massa Senyawa"):

            with st.spinner("Sedang menghitung..."):
                time.sleep(3)

            massa = (info['Mr'] * M * V) / 1000

            st.success(f"""
✅ Massa senyawa yang diperlukan:
{massa:.4f} gram
""")

            st.markdown(f"""
            <div style='
            background:rgba(255,255,255,0.7);
            padding:28px;
            border-radius:24px;
            border:1px solid #eee6ff;
            box-shadow:0 5px 18px rgba(200,200,255,.15);
            font-family:Segoe UI;
            color:#5b4b8a;
            line-height:2;
            font-size:18px;
            '>

            <h3 style='
            color:#7c6bb3;
            margin-bottom:18px;
            font-weight:700;
            '>
            🧪 Langkah Pembuatan Larutan
            </h3>

            <div style='font-size:17px;'>

            1️⃣ Timbang <b>{massa:.4f} gram</b> {info['nama']}<br>

            2️⃣ Larutkan dengan sedikit akuades<br>

            3️⃣ Masukkan ke labu takar <b>{V} mL</b><br>

            4️⃣ Tambahkan akuades hingga tanda batas<br>

            5️⃣ Homogenkan larutan

            </div>

            </div>
            """, unsafe_allow_html=True)

    # ================= PENGENCERAN =================

    else:

        M1 = st.number_input("Molaritas Awal (M)", 1.0)
        V1 = st.number_input("Volume Awal (mL)", 100.0)
        M2 = st.number_input("Molaritas Akhir (M)", 0.1)

        if st.button("Hitung Pengenceran"):

            if M2 >= M1:
                st.error("Molaritas akhir harus lebih kecil dari molaritas awal.")
            else:

                with st.spinner("Sedang menghitung..."):
                    time.sleep(3)

                V2 = (M1 * V1) / M2
                volume_air = V2 - V1

                st.success(f"""
✅ Volume akhir larutan:
{V2:.2f} mL
""")

                st.info(f"""
💧 Tambahkan sekitar {volume_air:.2f} mL akuades
ke dalam {V1:.2f} mL larutan stok untuk memperoleh
larutan {M2} M.
""")

                st.markdown(f"""
                <div style='
                background:rgba(255,255,255,0.7);
                padding:28px;
                border-radius:24px;
                border:1px solid #eee6ff;
                box-shadow:0 5px 18px rgba(200,200,255,.15);
                font-family:Segoe UI;
                color:#5b4b8a;
                line-height:2;
                font-size:18px;
                '>

                <h3 style='
                color:#7c6bb3;
                margin-bottom:18px;
                font-weight:700;
                '>
                💧 Langkah Pengenceran Larutan
                </h3>

                <div style='font-size:17px;'>

                1️⃣ Siapkan larutan stok {info['nama']} dengan konsentrasi <b>{M1} M</b><br>

                2️⃣ Pipet <b>{V1:.2f} mL</b> larutan stok<br>

                3️⃣ Masukkan ke dalam labu takar<br>

                4️⃣ Tambahkan akuades hingga volume mencapai <b>{V2:.2f} mL</b><br>

                5️⃣ Homogenkan larutan<br>

                6️⃣ Larutan <b>{M2} M</b> siap digunakan

                </div>

                </div>
                """, unsafe_allow_html=True)
# ================= PH =================

elif menu=="⚗️ pH":

    st.title("⚗️ Smart pH Calculator")

    if st.button("⬅ Kembali ke Home"):
        go_to("🏠 Home")

    senyawa=st.selectbox(
    "Pilih Senyawa",
    list(data_ph.keys()),
    format_func=lambda x:f"{data_ph[x]['nama']} ({x})"
    )

    info=data_ph[senyawa]

    st.info(f"""
🧪 Nama Senyawa : {info['nama']}

📌 Jenis : {info['jenis']}

⚖️ Mr : {info['Mr']} g/mol
""")

    C=st.number_input("Masukkan Konsentrasi (M)",0.01)

    if st.button("Hitung pH"):
        with st.spinner("Sedang menghitung..."):
            time.sleep(5)

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

        if ph <= 1:
            st.error("🔴 Sangat Asam")

        elif ph <= 3:
            st.warning("🟠 Asam")

        elif ph <= 6:
            st.info("🟡 Asam Lemah")

        elif ph == 7:
            st.success("🟢 Netral")

        elif ph <= 11:
            st.info("🔵 Basa Lemah")

        elif ph <= 13:
            st.warning("🟣 Basa")

        else:
            st.error("⚫ Sangat Basa")

# ================= INFORMASI BAHAN =================

elif menu=="📚 Informasi Bahan Kimia":
   
     st.title("📚 Informasi Bahan Kimia")
     
     if st.button("⬅ Kembali ke Home"):
        go_to("🏠 Home")
        
     cari=st.text_input("🔎 Cari nama atau rumus senyawa")

     hasil = [
         x for x in db
         if cari.lower() in x.lower()
         or cari.lower() in db[x][0].lower()
     ] if cari else list(db.keys())


     pilih=st.selectbox("Pilih Senyawa",hasil)

     data=db[pilih]

     st.markdown(f"""
<div class='card'>

<h3>🧪 Informasi Senyawa</h3>

<b>Nama Senyawa:</b> {data[0]}<br><br>

<b>Rumus Kimia:</b> {pilih}<br><br>

<b>Jenis:</b> {data[1]}<br><br>

<b>Mr:</b> {data[2]}<br><br>

<b>Bahaya:</b> {data[3]}<br><br>

<b>Bentuk/Fisik:</b> {data[4]}<br><br>

<b>Struktur Molekul:</b> {data[5]}

</div>
""", unsafe_allow_html=True)

# ================= ANALISIS KIMIA =================

elif menu=="🧪 Analisis Kimia":

    st.title("🧪 Smart Chemical Analysis")

    if st.button("⬅ Kembali ke Home"):
        go_to("🏠 Home")

    senyawa = st.selectbox(
        "Pilih Senyawa",
        list(db.keys())
    )

    data = db[senyawa]

    st.markdown(f"""
    <div class='info-box'>

    <h3>📊 Hasil Analisis Senyawa</h3>

    <b>🧪 Nama :</b> {data[0]}<br><br>

    <b>📌 Rumus :</b> {senyawa}<br><br>

    <b>⚗️ Jenis :</b> {data[1]}<br><br>

    <b>⚖️ Mr :</b> {data[2]}<br><br>

    <b>⚠️ Bahaya :</b> {data[3]}<br><br>

    <b>🧬 Struktur :</b> {data[5]}

    </div>
    """, unsafe_allow_html=True)

    st.subheader("🧪 Interpretasi Kimia")

    jenis = data[1]

    if jenis == "Asam kuat":
        interpretasi = "Asam kuat yang terionisasi hampir sempurna dalam air dan menghasilkan ion H⁺ dalam jumlah besar."

    elif jenis == "Asam lemah":
        interpretasi = "Asam lemah yang hanya terionisasi sebagian dalam air."

    elif jenis == "Basa kuat":
        interpretasi = "Basa kuat yang menghasilkan ion OH⁻ dalam jumlah besar."

    elif jenis == "Basa lemah":
        interpretasi = "Basa lemah yang hanya terionisasi sebagian dalam air."

    elif "Garam" in jenis:
        interpretasi = "Senyawa ionik yang tersusun dari kation dan anion."

    elif jenis == "Alkohol":
        interpretasi = "Mengandung gugus hidroksil (-OH) dan umum digunakan sebagai pelarut."

    elif jenis == "Keton":
        interpretasi = "Mengandung gugus karbonil (>C=O)."

    elif jenis == "Aromatik":
        interpretasi = "Mengandung cincin aromatik yang stabil karena resonansi."

    elif jenis == "Karbohidrat":
        interpretasi = "Merupakan sumber energi penting pada sistem biologis."

    elif jenis == "Amida":
        interpretasi = "Mengandung gugus fungsi amida (-CONH₂)."

    elif jenis == "Pelarut":
        interpretasi = "Digunakan untuk melarutkan berbagai senyawa kimia."

    elif jenis == "Oksidator":
        interpretasi = "Mampu mengoksidasi zat lain dengan menerima elektron."

    else:
        interpretasi = "Karakteristik kimia mengikuti gugus fungsi utamanya."

    st.info(interpretasi)
    
    st.subheader("🔬 Analisis Spesifik Senyawa")

    analisis_spesifik = {

"HCl":"Terionisasi sempurna dalam air menghasilkan ion H⁺ dan Cl⁻. Banyak digunakan sebagai titran dan pengatur pH.",

"H2SO4":"Asam diprotik kuat dengan sifat dehidrasi tinggi. Bereaksi eksotermik saat dicampur air.",

"HNO3":"Asam kuat sekaligus oksidator yang mampu mengoksidasi berbagai logam dan senyawa organik.",

"CH3COOH":"Asam lemah yang terionisasi sebagian dalam air dan sering digunakan sebagai pereaksi sintesis organik.",

"HF":"Meskipun tergolong asam lemah, memiliki bahaya tinggi karena dapat menembus jaringan dan bereaksi dengan kalsium tubuh.",

"H3BO3":"Asam lemah yang sering digunakan sebagai antiseptik dan bahan baku berbagai produk kimia.",

"NaOH":"Basa kuat yang terdisosiasi sempurna menghasilkan ion OH⁻ dan sering digunakan sebagai titran standar.",

"KOH":"Basa kuat yang umum digunakan pada industri sabun dan elektrolit baterai.",

"Ca(OH)2":"Basa kuat yang menghasilkan ion OH⁻ dalam larutan dan sering digunakan untuk pengolahan air.",

"NH3":"Basa lemah yang membentuk ion amonium dalam air dan banyak digunakan dalam industri pupuk.",

"NH4OH":"Basa lemah yang menghasilkan ion amonium dan ion hidroksida dalam larutan.",

"NaCl":"Garam yang terdisosiasi menghasilkan ion Na⁺ dan Cl⁻ dalam larutan.",

"KCl":"Garam yang menghasilkan ion kalium dan klorida dalam larutan serta banyak digunakan di laboratorium.",

"AgNO3":"Menghasilkan ion Ag⁺ yang digunakan dalam analisis argentometri dan pembentukan endapan halida.",

"CuSO4":"Sumber ion Cu²⁺ yang sering digunakan dalam analisis kualitatif dan pereaksi biuret.",

"FeCl3":"Digunakan sebagai pereaksi identifikasi fenol karena membentuk kompleks berwarna.",

"MgSO4":"Garam yang terdisosiasi menghasilkan ion magnesium dan sulfat dalam larutan.",

"Na2CO3":"Garam basa yang dapat meningkatkan pH larutan dan digunakan dalam berbagai proses industri.",

"NaHCO3":"Garam basa yang dapat bereaksi dengan asam menghasilkan gas karbon dioksida.",

"Pb(NO3)2":"Menghasilkan ion Pb²⁺ dalam larutan dan sering digunakan sebagai pereaksi analisis kimia.",

"ZnSO4":"Sumber ion Zn²⁺ yang digunakan dalam berbagai aplikasi laboratorium dan industri.",

"Na2SO4":"Garam yang terdisosiasi menghasilkan ion natrium dan sulfat dalam larutan.",

"HgCl2":"Sumber ion merkuri(II) yang bersifat sangat toksik dan memerlukan penanganan khusus.",

"NaNO3":"Garam yang mengandung ion nitrat dan digunakan dalam berbagai proses industri.",

"NH4Cl":"Garam amonium yang menghasilkan ion NH4⁺ dan Cl⁻ dalam larutan.",

"NH4NO3":"Garam yang mengandung ion amonium dan nitrat serta digunakan sebagai sumber nitrogen.",

"CaCO3":"Garam karbonat yang banyak ditemukan pada batu kapur dan berbagai material alami.",

"MgCl2":"Garam yang menghasilkan ion magnesium dan klorida dalam larutan.",

"Al2(SO4)3":"Digunakan dalam pengolahan air dan menghasilkan ion aluminium dalam larutan.",

"FeSO4":"Sumber ion Fe²⁺ yang digunakan dalam berbagai analisis dan proses industri.",

"CuCl2":"Sumber ion Cu²⁺ yang digunakan dalam sintesis dan analisis kimia.",

"Na3PO4":"Garam basa yang menghasilkan ion fosfat dan sering digunakan sebagai pengatur pH.",

"KNO3":"Garam yang mengandung ion kalium dan nitrat serta dikenal sebagai oksidator.",

"KMnO4":"Oksidator kuat yang digunakan sebagai titran pada permanganometri.",

"K2Cr2O7":"Oksidator kuat yang digunakan pada titrasi redoks dan mengandung kromium(VI) yang toksik.",

"H2O2":"Oksidator yang mudah terurai menghasilkan air dan oksigen.",

"NaClO":"Oksidator yang digunakan sebagai pemutih dan desinfektan serta dapat menghasilkan gas klorin jika bereaksi dengan asam.",

"CH3OH":"Alkohol sederhana yang sangat toksik dan dapat menyebabkan kebutaan bila tertelan.",

"C2H5OH":"Alkohol yang bercampur sempurna dengan air dan banyak digunakan sebagai pelarut serta antiseptik.",

"Acetone":"Pelarut organik volatil yang mudah menguap dan bercampur sempurna dengan air.",

"CH3COCH3":"Pelarut organik volatil yang mudah menguap dan bercampur sempurna dengan air.",

"Benzene":"Senyawa aromatik nonpolar yang stabil karena resonansi dan bersifat karsinogenik.",

"Toluene":"Turunan benzena yang banyak digunakan sebagai pelarut dan bahan baku sintesis organik.",

"CHCl3":"Pelarut organik dengan efek depresan sistem saraf pusat jika terhirup dalam jumlah besar.",

"CCl4":"Pelarut nonpolar yang bersifat hepatotoksik sehingga penggunaannya kini dibatasi.",

"Glucose":"Karbohidrat sederhana golongan monosakarida yang merupakan sumber energi utama bagi organisme hidup.",

"C6H12O6":"Karbohidrat sederhana golongan monosakarida yang merupakan sumber energi utama bagi organisme hidup.",

"Sucrose":"Karbohidrat golongan disakarida yang tersusun dari glukosa dan fruktosa.",

"C12H22O11":"Karbohidrat golongan disakarida yang tersusun dari glukosa dan fruktosa.",

"Urea":"Senyawa amida yang banyak digunakan sebagai bahan baku pupuk dan berbagai proses kimia."

}
    if senyawa in analisis_spesifik:
        st.success(analisis_spesifik[senyawa])
    else:
        st.info("Analisis spesifik senyawa belum tersedia. Analisis didasarkan pada golongan senyawanya.")

    st.subheader("📋 Kesimpulan")

    st.success(f"""
{data[0]} merupakan senyawa golongan {data[1].lower()}
dengan massa molekul relatif {data[2]}.

Berdasarkan data yang tersedia, senyawa ini memiliki tingkat bahaya
berupa {data[3].lower()} sehingga memerlukan penanganan yang sesuai
dengan prosedur keselamatan laboratorium.
""")
    
# ================= TENTANG =================

if menu == "ℹ️ Tentang":

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("""
    <div class="tentang-box">

    <h2>🧪 ChemAssist Pro</h2>

    <p>
    Aplikasi laboratorium kimia interaktif berbasis Python dan Streamlit.
    </p>

    <h3>🚀 Fitur Utama</h3>

    <ul>
        <li>Smart Solution Maker</li>
        <li>Smart pH Calculator</li>
        <li>Informasi Bahan Kimia</li>
        <li>Smart Chemical Analysis</li>
    </ul>

    <h3>👨‍💻 Teknologi</h3>

    <ul>
        <li>Python</li>
        <li>Streamlit</li>
    </ul>

    <h3>🎓 Dikembangkan Untuk</h3>

    <p>
    Praktikum dan pembelajaran kimia analitik,
    kimia dasar, serta perhitungan laboratorium.
    </p>

    <h3>👥 Creator Team</h3>

    <ul>
        <li><b>Adlina Dhiva Tsaniyah</b> (2560555)</li>
        <li><b>Davina Faiza Laksono</b> (2560605)</li>
        <li><b>Rachel Rafa Rashika</b> (2560738)</li>
        <li><b>Tantri Nirwana Bandiani</b> (2560795)</li>
    </ul>

    <h3>📌 Versi</h3>

    <p><b>ChemAssist Ultra v5.0</b></p>

    </div>
    """, unsafe_allow_html=True)
