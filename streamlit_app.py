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

# ================= DATA =================

data_ph={

"HCl":{"nama":"Asam Klorida","jenis":"Asam kuat","valensi":1,"Mr":36.46},
"H2SO4":{"nama":"Asam Sulfat","jenis":"Asam kuat","valensi":2,"Mr":98.08},
"HNO3":{"nama":"Asam Nitrat","jenis":"Asam kuat","valensi":1,"Mr":63.01},
"CH3COOH":{"nama":"Asam Asetat","jenis":"Asam lemah","Ka":1.8e-5,"Mr":60.05},
"HF":{"nama":"Asam Fluorida","jenis":"Asam lemah","Ka":6.8e-4,"Mr":20.01},
"HCOOH":{"nama":"Asam Format","jenis":"Asam lemah","Ka":1.8e-4,"Mr":46.03},
"H3PO4":{"nama":"Asam Fosfat","jenis":"Asam lemah","Ka":7.5e-3,"Mr":98.00},
"NaOH":{"nama":"Natrium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":40.00},
"KOH":{"nama":"Kalium Hidroksida","jenis":"Basa kuat","valensi":1,"Mr":56.11},
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
"CH3COOH":["Asam Asetat","Asam lemah","60.05 g/mol","Iritasi mata"],
"HF":["Asam Fluorida","Asam lemah","20.01 g/mol","Sangat beracun"],
"HCOOH":["Asam Format","Asam lemah","46.03 g/mol","Korosif"],
"H3PO4":["Asam Fosfat","Asam lemah","98.00 g/mol","Iritasi kulit"],
"NaOH":["Natrium Hidroksida","Basa kuat","40.00 g/mol","Korosif"],
"KOH":["Kalium Hidroksida","Basa kuat","56.11 g/mol","Korosif"],
"Ca(OH)2":["Kalsium Hidroksida","Basa kuat","74.09 g/mol","Iritasi"],
"NH3":["Amonia","Basa lemah","17.03 g/mol","Gas beracun"],
"NH4OH":["Amonium Hidroksida","Basa lemah","35.05 g/mol","Iritasi paru-paru"],
"NaCl":["Natrium Klorida","Garam","58.44 g/mol","Relatif aman"],
"KCl":["Kalium Klorida","Garam","74.55 g/mol","Iritasi ringan"],
"AgNO3":["Perak Nitrat","Garam","169.87 g/mol","Oksidator"],
"CuSO4":["Tembaga Sulfat","Garam","159.61 g/mol","Beracun"],
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
["Home","Larutan","pH","Database","Mini Quiz","Tentang"],
index=["Home","Larutan","pH","Database","Mini Quiz","Tentang"].index(
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
        <h3>📚 Chemical Database</h3>
        <p>Database senyawa lengkap dengan informasi penting</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Database"):
            st.session_state.page="Database"
            st.rerun()

    st.markdown("## ✨ Kenapa ChemAssist Pro?")

    st.info("""
✅ Mempermudah praktikum kimia  
✅ Membantu analisis larutan lebih cepat  
✅ Interface modern dan interaktif  
✅ Cocok untuk pembelajaran dan presentasi  
✅ Database senyawa kimia lengkap  
""")

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

            massa=(info['Mr']*M*V)/1000

            with st.spinner("Menganalisis data..."):
                time.sleep(1)

            st.success(f"""
✅ Massa senyawa yang diperlukan:
{massa:.4f} gram
""")

            st.progress(100)

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

            V2=(M1*V1)/M2

            st.success(f"""
✅ Volume akhir larutan:
{V2:.2f} mL
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
🧪 Nama Senyawa : {info['nama']}

📌 Jenis : {info['jenis']}

⚖️ Mr : {info['Mr']} g/mol
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

        if ph < 3:
            st.error("🔴 Sangat Asam")

        elif ph < 7:
            st.warning("🟠 Asam")

        elif ph == 7:
            st.info("🟢 Netral")

        elif ph <= 11:
            st.success("🔵 Basa")

        else:
            st.success("🟣 Sangat Basa")

# ================= DATABASE =================

elif menu=="Database":

    st.title("📚 Chemical Database")

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
🧪 Nama Senyawa :
{data[0]}

📌 Rumus Kimia :
{pilih}

⚗️ Jenis :
{data[1]}

⚖️ Mr :
{data[2]}

⚠️ Bahaya :
{data[3]}
""")

# ================= MINI QUIZ =================

elif menu=="Mini Quiz":

    st.title("🧠 Mini Quiz Kimia")

    soal=random.choice([
    ("pH larutan netral adalah?", "7"),
    ("Rumus kimia asam sulfat?", "H2SO4"),
    ("NaOH termasuk asam atau basa?", "basa"),
    ("Satuan Mr adalah?", "g/mol")
    ])

    st.write("### ❓", soal[0])

    jawaban=st.text_input("Masukkan Jawaban")

    if st.button("Cek Jawaban"):

        if jawaban.lower()==soal[1].lower():

            st.success("✅ Jawaban Benar!")

        else:

            st.error(f"❌ Jawaban Salah. Jawaban benar: {soal[1]}")

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
<li>Chemical Database</li>
<li>Mini Quiz Interaktif</li>
<li>Interface Modern</li>
</ul>

<h4>👨‍💻 Teknologi</h4>

<ul>
<li>Python</li>
<li>Streamlit</li>
</ul>

</div>
""", unsafe_allow_html=True)
