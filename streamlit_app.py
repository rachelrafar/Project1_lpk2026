import streamlit as st
import math
import time

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
padding:20px;
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

"HCl":{
"nama":"Asam Klorida",
"jenis":"Asam kuat",
"valensi":1,
"Mr":36.46,
"kegunaan":"Pembersih logam dan analisis laboratorium"
},

"H2SO4":{
"nama":"Asam Sulfat",
"jenis":"Asam kuat",
"valensi":2,
"Mr":98.08,
"kegunaan":"Elektrolit aki dan industri pupuk"
},

"HNO3":{
"nama":"Asam Nitrat",
"jenis":"Asam kuat",
"valensi":1,
"Mr":63.01,
"kegunaan":"Pembuatan pupuk dan bahan peledak"
},

"HClO4":{
"nama":"Asam Perklorat",
"jenis":"Asam kuat",
"valensi":1,
"Mr":100.46,
"kegunaan":"Reagen analisis kimia"
},

"CH3COOH":{
"nama":"Asam Asetat",
"jenis":"Asam lemah",
"Ka":1.8e-5,
"Mr":60.05,
"kegunaan":"Bahan dasar cuka"
},

"HF":{
"nama":"Asam Fluorida",
"jenis":"Asam lemah",
"Ka":6.8e-4,
"Mr":20.01,
"kegunaan":"Etsa kaca"
},

"HCOOH":{
"nama":"Asam Format",
"jenis":"Asam lemah",
"Ka":1.8e-4,
"Mr":46.03,
"kegunaan":"Industri tekstil dan karet"
},

"H3PO4":{
"nama":"Asam Fosfat",
"jenis":"Asam lemah",
"Ka":7.5e-3,
"Mr":98.00,
"kegunaan":"Pembuatan pupuk"
},

"H2CO3":{
"nama":"Asam Karbonat",
"jenis":"Asam lemah",
"Ka":4.3e-7,
"Mr":62.03,
"kegunaan":"Minuman bersoda"
},

"NaOH":{
"nama":"Natrium Hidroksida",
"jenis":"Basa kuat",
"valensi":1,
"Mr":40.00,
"kegunaan":"Pembuatan sabun"
},

"KOH":{
"nama":"Kalium Hidroksida",
"jenis":"Basa kuat",
"valensi":1,
"Mr":56.11,
"kegunaan":"Elektrolit baterai"
},

"Ba(OH)2":{
"nama":"Barium Hidroksida",
"jenis":"Basa kuat",
"valensi":2,
"Mr":171.34,
"kegunaan":"Analisis kimia"
},

"Ca(OH)2":{
"nama":"Kalsium Hidroksida",
"jenis":"Basa kuat",
"valensi":2,
"Mr":74.09,
"kegunaan":"Penjernihan air"
},

"NH3":{
"nama":"Amonia",
"jenis":"Basa lemah",
"Kb":1.8e-5,
"Mr":17.03,
"kegunaan":"Pembuatan pupuk"
},

"NH4OH":{
"nama":"Amonium Hidroksida",
"jenis":"Basa lemah",
"Kb":1.8e-5,
"Mr":35.05,
"kegunaan":"Pembersih rumah tangga"
},

"CH3NH2":{
"nama":"Metilamina",
"jenis":"Basa lemah",
"Kb":4.4e-4,
"Mr":31.06,
"kegunaan":"Industri farmasi"
},

"C2H5NH2":{
"nama":"Etilamina",
"jenis":"Basa lemah",
"Kb":5.6e-4,
"Mr":45.08,
"kegunaan":"Pembuatan pestisida"
}

}

# ================= DATABASE =================

db={

"HCl":["Asam Klorida","Asam kuat","36.46 g/mol","Korosif dan menyebabkan iritasi","Pembersih logam"],

"H2SO4":["Asam Sulfat","Asam kuat","98.08 g/mol","Sangat korosif","Industri pupuk"],

"HNO3":["Asam Nitrat","Asam kuat","63.01 g/mol","Oksidator kuat","Pembuatan pupuk"],

"HClO4":["Asam Perklorat","Asam kuat","100.46 g/mol","Korosif","Reagen laboratorium"],

"CH3COOH":["Asam Asetat","Asam lemah","60.05 g/mol","Iritasi mata","Pembuatan cuka"],

"HF":["Asam Fluorida","Asam lemah","20.01 g/mol","Sangat beracun","Etsa kaca"],

"HCOOH":["Asam Format","Asam lemah","46.03 g/mol","Korosif","Industri tekstil"],

"H3PO4":["Asam Fosfat","Asam lemah","98.00 g/mol","Iritasi kulit","Pembuatan pupuk"],

"NaOH":["Natrium Hidroksida","Basa kuat","40.00 g/mol","Korosif","Pembuatan sabun"],

"KOH":["Kalium Hidroksida","Basa kuat","56.11 g/mol","Korosif","Elektrolit baterai"],

"Ba(OH)2":["Barium Hidroksida","Basa kuat","171.34 g/mol","Berbahaya","Analisis kimia"],

"Ca(OH)2":["Kalsium Hidroksida","Basa kuat","74.09 g/mol","Iritasi","Penjernihan air"],

"NH3":["Amonia","Basa lemah","17.03 g/mol","Gas beracun","Pembuatan pupuk"],

"NH4OH":["Amonium Hidroksida","Basa lemah","35.05 g/mol","Iritasi paru-paru","Pembersih"],

"NaCl":["Natrium Klorida","Garam","58.44 g/mol","Relatif aman","Garam dapur"],

"KCl":["Kalium Klorida","Garam","74.55 g/mol","Iritasi ringan","Pupuk"],

"AgNO3":["Perak Nitrat","Garam","169.87 g/mol","Oksidator","Analisis laboratorium"],

"CuSO4":["Tembaga Sulfat","Garam","159.61 g/mol","Beracun","Fungisida"],

"FeCl3":["Besi(III) Klorida","Garam","162.20 g/mol","Korosif","Pengolahan limbah"],

"MgSO4":["Magnesium Sulfat","Garam","120.37 g/mol","Iritasi ringan","Farmasi"],

"Na2CO3":["Natrium Karbonat","Garam basa","105.99 g/mol","Iritasi kulit","Industri kaca"],

"NaHCO3":["Natrium Bikarbonat","Garam basa","84.01 g/mol","Relatif aman","Baking soda"],

"C2H5OH":["Etanol","Alkohol","46.07 g/mol","Mudah terbakar","Desinfektan"],

"CH3OH":["Metanol","Alkohol","32.04 g/mol","Beracun","Pelarut"],

"Acetone":["Aseton","Keton","58.08 g/mol","Sangat mudah terbakar","Pembersih kuteks"],

"Benzene":["Benzena","Aromatik","78.11 g/mol","Karsinogen","Industri kimia"],

"Toluene":["Toluena","Aromatik","92.14 g/mol","Beracun","Pelarut cat"],

"Glucose":["Glukosa","Karbohidrat","180.16 g/mol","Relatif aman","Sumber energi"]

}

# ================= SIDEBAR =================

menu=st.sidebar.radio(
"🧪 ChemAssist Pro",
["Home","Larutan","pH","Database","Tentang"],
index=["Home","Larutan","pH","Database","Tentang"].index(
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
    c3.metric("🚀 Version","12.0")

    st.markdown("## 🔥 Fitur Utama")

    a,b,c=st.columns(3)

    with a:

        st.markdown("""
        <div class='card'>
        <h3>💧 Smart Solution Maker</h3>
        <p>Pembuatan larutan otomatis lengkap dengan langkah kerja laboratorium</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Menu Larutan"):
            st.session_state.page="Larutan"
            st.rerun()

    with b:

        st.markdown("""
        <div class='card'>
        <h3>⚗️ Smart pH Calculator</h3>
        <p>Perhitungan pH asam dan basa otomatis</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Kalkulator pH"):
            st.session_state.page="pH"
            st.rerun()

    with c:

        st.markdown("""
        <div class='card'>
        <h3>📚 Chemical Database</h3>
        <p>Informasi lengkap bahan kimia laboratorium</p>
        </div>
        """, unsafe_allow_html=True)

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

    st.info(f"""
🧪 Nama Senyawa : {info['nama']}

📌 Rumus Kimia : {senyawa}

⚖️ Mr : {info['Mr']} g/mol

🏭 Kegunaan :
{info['kegunaan']}
""")

    metode=st.selectbox(
    "Pilih Jenis Perhitungan",
    ["Molaritas","Pengenceran"]
    )

    if metode=="Molaritas":

        M=st.number_input("Konsentrasi Larutan (M)",0.1)
        V=st.number_input("Volume Larutan (mL)",100.0)

        if st.button("Hitung Massa"):

            with st.spinner("Menghitung massa senyawa..."):
                time.sleep(1)

            massa=(info['Mr']*M*V)/1000

            st.success(f"""
✅ Massa senyawa yang diperlukan:
{massa:.4f} gram
""")

            st.code(f"""
Langkah Pembuatan Larutan:

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

            st.code(f"""
Langkah Pengenceran:

1. Ambil {V1:.2f} mL larutan stok
2. Masukkan ke labu ukur
3. Tambahkan akuades hingga volume {V2:.2f} mL
4. Homogenkan larutan
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

🏭 Kegunaan :
{info['kegunaan']}
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

⚗️ Jenis Senyawa :
{data[1]}

⚖️ Mr :
{data[2]}

⚠️ Bahaya :
{data[3]}

🏭 Kegunaan :
{data[4]}
""")

    st.markdown("### 📋 Daftar Senyawa")

    for senyawa in db:

        st.markdown(f"""
<div class='info-box'>

<b>{senyawa}</b> — {db[senyawa][0]}

Jenis : {db[senyawa][1]}

Mr : {db[senyawa][2]}

</div>
""", unsafe_allow_html=True)

# ================= TENTANG =================

elif menu=="Tentang":

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("""
<div class='info-box'>

### 🧪 ChemAssist Pro

Aplikasi laboratorium kimia interaktif berbasis Python dan Streamlit.

### 🚀 Fitur Utama

- Smart Solution Maker
- Smart pH Calculator
- Chemical Database
- Perhitungan Pengenceran
- Database senyawa lengkap
- Progress indikator pH
- Interface modern dan interaktif

### 🎓 Tujuan

Membantu pembelajaran dan praktikum kimia secara digital dan efisien.

### 👨‍💻 Teknologi

- Python
- Streamlit

</div>
""", unsafe_allow_html=True)
