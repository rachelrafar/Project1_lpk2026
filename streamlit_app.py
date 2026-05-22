import streamlit as st
import math

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
"Mr":36.46
},

"H2SO4":{
"nama":"Asam Sulfat",
"jenis":"Asam kuat",
"valensi":2,
"Mr":98.08
},

"HNO3":{
"nama":"Asam Nitrat",
"jenis":"Asam kuat",
"valensi":1,
"Mr":63.01
},

"CH3COOH":{
"nama":"Asam Asetat",
"jenis":"Asam lemah",
"Ka":1.8e-5,
"Mr":60.05
},

"HF":{
"nama":"Asam Fluorida",
"jenis":"Asam lemah",
"Ka":6.8e-4,
"Mr":20.01
},

"NaOH":{
"nama":"Natrium Hidroksida",
"jenis":"Basa kuat",
"valensi":1,
"Mr":40.00
},

"KOH":{
"nama":"Kalium Hidroksida",
"jenis":"Basa kuat",
"valensi":1,
"Mr":56.11
},

"Ba(OH)2":{
"nama":"Barium Hidroksida",
"jenis":"Basa kuat",
"valensi":2,
"Mr":171.34
},

"Ca(OH)2":{
"nama":"Kalsium Hidroksida",
"jenis":"Basa kuat",
"valensi":2,
"Mr":74.09
},

"NH3":{
"nama":"Amonia",
"jenis":"Basa lemah",
"Kb":1.8e-5,
"Mr":17.03
},

"NH4OH":{
"nama":"Amonium Hidroksida",
"jenis":"Basa lemah",
"Kb":1.8e-5,
"Mr":35.05
},

"CH3NH2":{
"nama":"Metilamina",
"jenis":"Basa lemah",
"Kb":4.4e-4,
"Mr":31.06
},

"C2H5NH2":{
"nama":"Etilamina",
"jenis":"Basa lemah",
"Kb":5.6e-4,
"Mr":45.08
},

}

# ================= DATABASE =================

db={

"HCl":{
"nama":"Asam Klorida",
"jenis":"Asam kuat",
"Mr":"36.46 g/mol",
"Bahaya":"Korosif, menyebabkan iritasi kulit dan pernapasan"
},

"H2SO4":{
"nama":"Asam Sulfat",
"jenis":"Asam kuat",
"Mr":"98.08 g/mol",
"Bahaya":"Sangat korosif dan bereaksi hebat dengan air"
},

"HNO3":{
"nama":"Asam Nitrat",
"jenis":"Asam kuat",
"Mr":"63.01 g/mol",
"Bahaya":"Oksidator kuat dan korosif"
},

"CH3COOH":{
"nama":"Asam Asetat",
"jenis":"Asam lemah",
"Mr":"60.05 g/mol",
"Bahaya":"Iritasi mata dan kulit"
},

"HF":{
"nama":"Asam Fluorida",
"jenis":"Asam lemah",
"Mr":"20.01 g/mol",
"Bahaya":"Sangat beracun dan korosif"
},

"NaOH":{
"nama":"Natrium Hidroksida",
"jenis":"Basa kuat",
"Mr":"40.00 g/mol",
"Bahaya":"Korosif dan menyebabkan luka bakar"
},

"KOH":{
"nama":"Kalium Hidroksida",
"jenis":"Basa kuat",
"Mr":"56.11 g/mol",
"Bahaya":"Korosif terhadap kulit dan mata"
},

"Ca(OH)2":{
"nama":"Kalsium Hidroksida",
"jenis":"Basa kuat",
"Mr":"74.09 g/mol",
"Bahaya":"Iritasi saluran napas"
},

"NH3":{
"nama":"Amonia",
"jenis":"Basa lemah",
"Mr":"17.03 g/mol",
"Bahaya":"Gas beracun dan iritasi"
},

"NH4OH":{
"nama":"Amonium Hidroksida",
"jenis":"Basa lemah",
"Mr":"35.05 g/mol",
"Bahaya":"Iritasi kulit dan paru-paru"
},

"NaCl":{
"nama":"Natrium Klorida",
"jenis":"Garam",
"Mr":"58.44 g/mol",
"Bahaya":"Relatif aman"
},

"KCl":{
"nama":"Kalium Klorida",
"jenis":"Garam",
"Mr":"74.55 g/mol",
"Bahaya":"Iritasi ringan"
},

"AgNO3":{
"nama":"Perak Nitrat",
"jenis":"Garam",
"Mr":"169.87 g/mol",
"Bahaya":"Oksidator dan menyebabkan noda kulit"
},

"CuSO4":{
"nama":"Tembaga(II) Sulfat",
"jenis":"Garam",
"Mr":"159.61 g/mol",
"Bahaya":"Beracun bagi organisme air"
},

"FeCl3":{
"nama":"Besi(III) Klorida",
"jenis":"Garam",
"Mr":"162.20 g/mol",
"Bahaya":"Korosif dan iritasi"
},

"MgSO4":{
"nama":"Magnesium Sulfat",
"jenis":"Garam",
"Mr":"120.37 g/mol",
"Bahaya":"Iritasi ringan"
},

"CaCO3":{
"nama":"Kalsium Karbonat",
"jenis":"Garam",
"Mr":"100.09 g/mol",
"Bahaya":"Debu dapat mengiritasi saluran napas"
},

"Na2CO3":{
"nama":"Natrium Karbonat",
"jenis":"Garam basa",
"Mr":"105.99 g/mol",
"Bahaya":"Iritasi mata dan kulit"
},

"NaHCO3":{
"nama":"Natrium Bikarbonat",
"jenis":"Garam basa",
"Mr":"84.01 g/mol",
"Bahaya":"Relatif aman"
},

"C2H5OH":{
"nama":"Etanol",
"jenis":"Alkohol",
"Mr":"46.07 g/mol",
"Bahaya":"Mudah terbakar"
},

"CH3OH":{
"nama":"Metanol",
"jenis":"Alkohol",
"Mr":"32.04 g/mol",
"Bahaya":"Beracun dan mudah terbakar"
},

"Acetone":{
"nama":"Aseton",
"jenis":"Keton",
"Mr":"58.08 g/mol",
"Bahaya":"Sangat mudah terbakar"
},

"Benzene":{
"nama":"Benzena",
"jenis":"Hidrokarbon aromatik",
"Mr":"78.11 g/mol",
"Bahaya":"Karsinogen dan mudah terbakar"
},

"Toluene":{
"nama":"Toluena",
"jenis":"Hidrokarbon aromatik",
"Mr":"92.14 g/mol",
"Bahaya":"Beracun jika terhirup"
},

"Glucose":{
"nama":"Glukosa",
"jenis":"Karbohidrat",
"Mr":"180.16 g/mol",
"Bahaya":"Relatif aman"
}

}

# ================= SIDEBAR =================

menu=st.sidebar.radio(
"🧪 ChemAssist Pro",
["Home","Larutan","pH","Database"]
)

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
    c3.metric("🚀 Version","7.0")

    a,b,c=st.columns(3)

    with a:

        st.markdown("""
        <div class='card'>
        <h3>💧 Smart Solution Maker</h3>
        <p>Perhitungan larutan otomatis</p>
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Menu Larutan"):
            st.session_state.page="Larutan"
            st.rerun()

    with b:

        st.markdown("""
        <div class='card'>
        <h3>⚗️ Smart pH Calculator</h3>
        <p>Hitung pH asam dan basa</p>
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Kalkulator pH"):
            st.session_state.page="pH"
            st.rerun()

    with c:

        st.markdown("""
        <div class='card'>
        <h3>📚 Chemical Database</h3>
        <p>Informasi senyawa kimia</p>
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

    mode=st.radio(
    "Pilih Jenis Perhitungan",
    ["Pembuatan Larutan","Pengenceran Larutan"]
    )

    if mode=="Pembuatan Larutan":

        Mr=st.number_input("Mr Senyawa (g/mol)",40.0)
        M=st.number_input("Konsentrasi Molaritas (M)",0.1)
        V=st.number_input("Volume Larutan (mL)",100.0)

        if st.button("Hitung Massa Senyawa"):

            massa=(Mr*M*V)/1000

            st.success(f"""
✅ Massa senyawa yang harus ditimbang:
{massa:.4f} gram
""")

            st.info(f"""
📋 Prosedur Pembuatan Larutan:

1. Timbang {massa:.4f} gram senyawa
2. Larutkan dengan sedikit akuades
3. Pindahkan ke labu ukur {V} mL
4. Tambahkan akuades hingga tanda batas
5. Homogenkan larutan sebelum digunakan
""")

    else:

        C1=st.number_input("Konsentrasi Awal",10.0)
        C2=st.number_input("Konsentrasi Akhir",1.0)
        V2=st.number_input("Volume Akhir (mL)",100.0)

        if st.button("Hitung Pengenceran"):

            V1=(C2*V2)/C1

            st.success(f"""
✅ Volume larutan stok yang diperlukan:
{V1:.2f} mL
""")

            st.info(f"""
📋 Langkah Pengenceran:

1. Pipet {V1:.2f} mL larutan stok
2. Masukkan ke labu ukur
3. Tambahkan akuades hingga volume {V2} mL
4. Tutup dan homogenkan larutan
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

### 📌 Informasi Senyawa

- Nama Senyawa : {info['nama']}
- Rumus Kimia : {senyawa}
- Jenis : {info['jenis']}
- Mr : {info['Mr']} g/mol

</div>
""", unsafe_allow_html=True)

    C=st.number_input("Masukkan Konsentrasi (M)",0.01)

    if st.button("Hitung Nilai pH"):

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

        st.metric("📊 Nilai pH Larutan",f"{ph:.2f}")

        if ph < 7:
            st.error("Larutan bersifat ASAM")

        elif ph > 7:
            st.success("Larutan bersifat BASA")

        else:
            st.info("Larutan bersifat NETRAL")

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
    or cari.lower() in db[x]["nama"].lower()
    ] if cari else list(db.keys())

    pilih=st.selectbox("Pilih Senyawa",hasil)

    st.markdown(f"""
<div class='info-box'>

### 🧪 Informasi Senyawa

- Nama Senyawa : {db[pilih]['nama']}
- Rumus Kimia : {pilih}
- Jenis Senyawa : {db[pilih]['jenis']}
- Massa Molekul Relatif (Mr) : {db[pilih]['Mr']}

### ⚠️ Informasi Bahaya

{db[pilih]['Bahaya']}

</div>
""", unsafe_allow_html=True)
