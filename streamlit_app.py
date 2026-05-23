import streamlit as st
import math
import time
import random
from datetime import datetime

# ================= CONFIG =================

st.set_page_config(
    page_title="ChemAssist Pro",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

button[kind="header"]{
display:none;
}

</style>
""", unsafe_allow_html=True)

# ================= STYLE =================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

html, body, [class*="css"]{
    font-family:'Segoe UI',sans-serif;
}

.stApp{
    background:
    radial-gradient(circle at top left,#1e3c72 0%,#2a5298 25%,#0f172a 100%);
    color:white;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.glass{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(14px);
    border:1px solid rgba(255,255,255,0.12);
    border-radius:28px;
    padding:28px;
    box-shadow:0 8px 30px rgba(0,0,0,0.25);
    margin-bottom:20px;
}

.hero{
    padding:55px;
    border-radius:30px;
    background:linear-gradient(135deg,#4facfe,#00f2fe);
    color:white;
    text-align:center;
    box-shadow:0 10px 30px rgba(0,0,0,.35);
    margin-bottom:25px;
}

.hero-title{
    font-size:54px;
    font-weight:800;
    margin-bottom:10px;
}

.hero-sub{
    font-size:19px;
    opacity:0.95;
}

.card{
    background:rgba(255,255,255,0.09);
    border:1px solid rgba(255,255,255,0.12);
    backdrop-filter:blur(10px);
    border-radius:24px;
    padding:24px;
    transition:0.35s;
    box-shadow:0 5px 20px rgba(0,0,0,0.18);
    margin-bottom:18px;
}

.card:hover{
    transform:translateY(-6px) scale(1.02);
    box-shadow:0 12px 28px rgba(0,0,0,.25);
}

.feature-title{
    font-size:22px;
    font-weight:700;
    color:white;
}

.feature-desc{
    color:#dbeafe;
    font-size:15px;
}

.stButton>button{
    width:100%;
    height:54px;
    border:none;
    border-radius:16px;
    font-size:16px;
    font-weight:700;
    background:linear-gradient(135deg,#00c6ff,#0072ff);
    color:white;
    transition:0.3s;
    box-shadow:0 4px 15px rgba(0,114,255,.4);
}

.stButton>button:hover{
    transform:scale(1.02);
    background:linear-gradient(135deg,#36d1dc,#5b86e5);
}

.stTextInput>div>div>input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"]{
    border-radius:16px !important;
}

.metric-box{
    background:rgba(255,255,255,0.08);
    padding:18px;
    border-radius:22px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.08);
}

.sidebar .sidebar-content{
    background:#0f172a;
}

hr{
    border:1px solid rgba(255,255,255,0.1);
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

# ================= SIDEBAR =================

menu=st.sidebar.radio(
"🧪 ChemAssist Pro",
["Home","Larutan","pH","Informasi Bahan Kimia","Analisis Kimia","Tentang"],
index=["Home","Larutan","pH","Informasi Bahan Kimia","Analisis Kimia","Tentang"].index(
st.session_state.page
)
)

st.session_state.page=menu

# ================= HOME =================

if menu=="Home":

    jam=datetime.now().strftime("%H:%M")

    st.markdown(f"""
    <div class='hero'>
        <div class='hero-title'>🧪 ChemAssist Pro</div>
        <div class='hero-sub'>
        Smart Chemistry Assistant • Modern Laboratory Experience
        <br><br>
        ⏰ {jam}
        </div>
    </div>
    """, unsafe_allow_html=True)

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
            st.session_state.page="Larutan"
            st.rerun()

        st.markdown("""
        <div class='card'>
            <div class='feature-title'>📚 Chemical Database</div>
            <div class='feature-desc'>
            Informasi senyawa lengkap dan interaktif.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📖 Informasi Kimia"):
            st.session_state.page="Informasi Bahan Kimia"
            st.rerun()

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
            st.session_state.page="pH"
            st.rerun()

        st.markdown("""
        <div class='card'>
            <div class='feature-title'>🧠 Chemical Analysis</div>
            <div class='feature-desc'>
            Analisis karakteristik senyawa modern.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🧪 Analisis Kimia"):
            st.session_state.page="Analisis Kimia"
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
            with st.spinner("Sedang menghitung..."):
                time.sleep(5)

            massa=(info['Mr']*M*V)/1000

            st.success(f"""
✅ Massa senyawa yang diperlukan:
{massa:.4f} gram
""")

            st.code(f"""
Langkah Pembuatan Larutan

1. Timbang {massa:.4f} gram {info['nama']}
2. Larutkan dengan sedikit akuades
3. Masukkan ke labu ukur {V} mL
4. Tambahkan akuades hingga tanda batas
5. Homogenkan larutan
""")

    else:

        M1=st.number_input("Molaritas Awal",1.0)
        V1=st.number_input("Volume Awal (mL)",100.0)
        M2=st.number_input("Molaritas Akhir",0.1)

        if st.button("Hitung Pengenceran"):
            with st.spinner("Sedang menghitung..."):
                time.sleep(5)

            V2=(M1*V1)/M2

            st.success(f"""
✅ Volume akhir larutan:
{V2:.2f} mL
""")

# ================= PH =================

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

elif menu=="Informasi Bahan Kimia":

    st.title("📚 Informasi Bahan Kimia")

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    cari=st.text_input("🔎 Cari nama atau rumus senyawa")

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

⚠️ Bahaya : {data[3]}

🎨 Bentuk/Fisik : {data[4]}

🧬 Struktur Molekul : {data[5]}
""")

# ================= ANALISIS KIMIA =================

elif menu=="Analisis Kimia":

    st.title("🧪 Smart Chemical Analysis")

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    senyawa=st.selectbox(
    "Pilih Senyawa",
    list(db.keys())
    )

    data=db[senyawa]

    st.markdown(f"""
<div class='info-box'>

<h3>📊 Hasil Analisis Senyawa</h3>

<b>🧪 Nama :</b> {data[0]} <br><br>

<b>📌 Rumus :</b> {senyawa} <br><br>

<b>⚗️ Jenis :</b> {data[1]} <br><br>

<b>⚖️ Mr :</b> {data[2]} <br><br>

<b>⚠️ Bahaya :</b> {data[3]} <br><br>

<b>🧬 Struktur :</b> {data[5]}

</div>
""", unsafe_allow_html=True)

    st.subheader("📈 Interpretasi Kimia")

    if "Asam" in data[1]:

        st.success("""
Senyawa ini bersifat asam dan menghasilkan ion H+ dalam larutan.
Digunakan pada analisis laboratorium dan industri kimia.
""")

    elif "Basa" in data[1]:

        st.info("""
Senyawa ini bersifat basa dan menghasilkan ion OH- dalam larutan.
Umumnya digunakan untuk netralisasi dan industri.
""")

    elif "Garam" in data[1]:

        st.warning("""
Senyawa ini termasuk golongan garam hasil reaksi asam dan basa.
""")

    else:

        st.write("""
Senyawa ini memiliki karakteristik kimia khusus berdasarkan gugus fungsinya.
""")

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

<h4>🚀 Fitur Utama</h4>

<ul>
<li>Smart Solution Maker</li>
<li>Smart pH Calculator</li>
<li>Informasi Bahan Kimia</li>
<li>Smart Chemical Analysis</li>
</ul>

<h4>👨‍💻 Teknologi</h4>

<ul>
<li>Python</li>
<li>Streamlit</li>
</ul>

</div>
""", unsafe_allow_html=True)
