import streamlit as st
import math

# ================= CONFIG =================

st.set_page_config(
    page_title="ChemAssist",
    page_icon="🧪",
    layout="centered"
)

# ================= STYLE =================

st.markdown("""
<style>
.stApp{
background:linear-gradient(to bottom,#eaf3ff,#ffffff);
}

.header{
padding:25px;
border-radius:20px;
background:white;
text-align:center;
box-shadow:0px 4px 15px rgba(0,0,0,.1);
margin-bottom:20px;
}

.card{
padding:15px;
background:white;
border-radius:15px;
box-shadow:0px 4px 10px rgba(0,0,0,.1);
text-align:center;
}

.stButton>button{
width:100%;
border-radius:12px;
height:50px;
}
</style>
""", unsafe_allow_html=True)

# ================= SESSION =================

if "page" not in st.session_state:
    st.session_state.page="Home"

# ================= DATA pH =================

data_ph={

"HCl":{"jenis":"Asam kuat","valensi":1},
"HBr":{"jenis":"Asam kuat","valensi":1},
"HI":{"jenis":"Asam kuat","valensi":1},
"HNO3":{"jenis":"Asam kuat","valensi":1},
"H2SO4":{"jenis":"Asam kuat","valensi":2},

"NaOH":{"jenis":"Basa kuat","valensi":1},
"KOH":{"jenis":"Basa kuat","valensi":1},
"Ba(OH)2":{"jenis":"Basa kuat","valensi":2},
"Ca(OH)2":{"jenis":"Basa kuat","valensi":2},
"Sr(OH)2":{"jenis":"Basa kuat","valensi":2},
"LiOH":{"jenis":"Basa kuat","valensi":1},

"CH3COOH":{"jenis":"Asam lemah","Ka":1.8e-5},
"HF":{"jenis":"Asam lemah","Ka":6.8e-4},
"HCOOH":{"jenis":"Asam lemah","Ka":1.8e-4},
"HCN":{"jenis":"Asam lemah","Ka":4.9e-10},
"H2CO3":{"jenis":"Asam lemah","Ka":4.3e-7},
"H3PO4":{"jenis":"Asam lemah","Ka":7.5e-3},
"H2S":{"jenis":"Asam lemah","Ka":1e-7},
"HClO":{"jenis":"Asam lemah","Ka":3e-8},
"HClO4":{"jenis":"Asam kuat","valensi":1},
"H2C2O4":{"jenis":"Asam lemah","Ka":5.9e-2},
"H3BO3":{"jenis":"Asam lemah","Ka":5.8e-10},
"C6H8O7":{"jenis":"Asam lemah","Ka":7.4e-4},
"HNO2":{"jenis":"Asam lemah","Ka":4.5e-4},

"NH3":{"jenis":"Basa lemah","Kb":1.8e-5},
"NH4OH":{"jenis":"Basa lemah","Kb":1.8e-5},
"CH3NH2":{"jenis":"Basa lemah","Kb":4.4e-4},
"C2H5NH2":{"jenis":"Basa lemah","Kb":5.6e-4},
"(CH3)2NH":{"jenis":"Basa lemah","Kb":5.4e-4},
"C5H5N":{"jenis":"Basa lemah","Kb":1.7e-9},
"C6H5NH2":{"jenis":"Basa lemah","Kb":4e-10},

}

# ================= NAMA SENYAWA =================

nama_senyawa={

"HCl":"Asam Klorida (HCl)",
"HBr":"Asam Bromida (HBr)",
"HI":"Asam Iodida (HI)",
"HNO3":"Asam Nitrat (HNO3)",
"H2SO4":"Asam Sulfat (H2SO4)",
"CH3COOH":"Asam Asetat (CH3COOH)",
"HF":"Asam Fluorida (HF)",
"HCOOH":"Asam Format (HCOOH)",
"HCN":"Asam Sianida (HCN)",
"H2CO3":"Asam Karbonat (H2CO3)",
"H3PO4":"Asam Fosfat (H3PO4)",
"H2S":"Asam Sulfida (H2S)",
"HClO":"Asam Hipoklorit (HClO)",
"HClO4":"Asam Perklorat (HClO4)",
"H2C2O4":"Asam Oksalat (H2C2O4)",
"H3BO3":"Asam Borat (H3BO3)",
"C6H8O7":"Asam Sitrat (C6H8O7)",
"HNO2":"Asam Nitrit (HNO2)",

"NaOH":"Natrium Hidroksida (NaOH)",
"KOH":"Kalium Hidroksida (KOH)",
"Ba(OH)2":"Barium Hidroksida [Ba(OH)2]",
"Ca(OH)2":"Kalsium Hidroksida [Ca(OH)2]",
"Sr(OH)2":"Stronsium Hidroksida [Sr(OH)2]",
"LiOH":"Litium Hidroksida (LiOH)",

"NH3":"Amonia (NH3)",
"NH4OH":"Amonium Hidroksida (NH4OH)",
"CH3NH2":"Metilamina (CH3NH2)",
"C2H5NH2":"Etilamina (C2H5NH2)",
"(CH3)2NH":"Dimetilamina [(CH3)2NH]",
"C5H5N":"Piridina (C5H5N)",
"C6H5NH2":"Anilina (C6H5NH2)"

}

# ================= DATABASE =================

db={

"HCl":{
"nama":"Asam Klorida",
"jenis":"Asam kuat",
"Mr":36.46,
"Bahaya":"Korosif, menyebabkan iritasi kulit dan pernapasan"
},

"H2SO4":{
"nama":"Asam Sulfat",
"jenis":"Asam kuat",
"Mr":98.08,
"Bahaya":"Sangat korosif dan bereaksi hebat dengan air"
},

"HNO3":{
"nama":"Asam Nitrat",
"jenis":"Asam kuat",
"Mr":63.01,
"Bahaya":"Oksidator kuat dan korosif"
},

"CH3COOH":{
"nama":"Asam Asetat",
"jenis":"Asam lemah",
"Mr":60.05,
"Bahaya":"Iritasi mata dan kulit"
},

"HF":{
"nama":"Asam Fluorida",
"jenis":"Asam lemah",
"Mr":20.01,
"Bahaya":"Sangat beracun dan korosif"
},

"NaOH":{
"nama":"Natrium Hidroksida",
"jenis":"Basa kuat",
"Mr":40.00,
"Bahaya":"Korosif dan menyebabkan luka bakar"
},

"KOH":{
"nama":"Kalium Hidroksida",
"jenis":"Basa kuat",
"Mr":56.11,
"Bahaya":"Korosif terhadap kulit dan mata"
},

"Ca(OH)2":{
"nama":"Kalsium Hidroksida",
"jenis":"Basa kuat",
"Mr":74.09,
"Bahaya":"Iritasi saluran napas"
},

"NH3":{
"nama":"Amonia",
"jenis":"Basa lemah",
"Mr":17.03,
"Bahaya":"Gas beracun dan iritasi"
},

"NH4OH":{
"nama":"Amonium Hidroksida",
"jenis":"Basa lemah",
"Mr":35.05,
"Bahaya":"Iritasi kulit dan paru-paru"
},

"NaCl":{
"nama":"Natrium Klorida",
"jenis":"Garam",
"Mr":58.44,
"Bahaya":"Relatif aman"
},

"KCl":{
"nama":"Kalium Klorida",
"jenis":"Garam",
"Mr":74.55,
"Bahaya":"Iritasi ringan"
},

"AgNO3":{
"nama":"Perak Nitrat",
"jenis":"Garam",
"Mr":169.87,
"Bahaya":"Oksidator dan menyebabkan noda kulit"
},

"CuSO4":{
"nama":"Tembaga(II) Sulfat",
"jenis":"Garam",
"Mr":159.61,
"Bahaya":"Beracun bagi organisme air"
},

"FeCl3":{
"nama":"Besi(III) Klorida",
"jenis":"Garam",
"Mr":162.20,
"Bahaya":"Korosif dan iritasi"
},

"MgSO4":{
"nama":"Magnesium Sulfat",
"jenis":"Garam",
"Mr":120.37,
"Bahaya":"Iritasi ringan"
},

"CaCO3":{
"nama":"Kalsium Karbonat",
"jenis":"Garam",
"Mr":100.09,
"Bahaya":"Debu dapat mengiritasi saluran napas"
},

"Na2CO3":{
"nama":"Natrium Karbonat",
"jenis":"Garam basa",
"Mr":105.99,
"Bahaya":"Iritasi mata dan kulit"
},

"NaHCO3":{
"nama":"Natrium Bikarbonat",
"jenis":"Garam basa",
"Mr":84.01,
"Bahaya":"Relatif aman"
},

"C2H5OH":{
"nama":"Etanol",
"jenis":"Alkohol",
"Mr":46.07,
"Bahaya":"Mudah terbakar"
},

"CH3OH":{
"nama":"Metanol",
"jenis":"Alkohol",
"Mr":32.04,
"Bahaya":"Beracun dan mudah terbakar"
},

"Acetone":{
"nama":"Aseton",
"jenis":"Keton",
"Mr":58.08,
"Bahaya":"Sangat mudah terbakar"
},

"Benzene":{
"nama":"Benzena",
"jenis":"Hidrokarbon aromatik",
"Mr":78.11,
"Bahaya":"Karsinogen dan mudah terbakar"
},

"Toluene":{
"nama":"Toluena",
"jenis":"Hidrokarbon aromatik",
"Mr":92.14,
"Bahaya":"Beracun jika terhirup"
},

"Glucose":{
"nama":"Glukosa",
"jenis":"Karbohidrat",
"Mr":180.16,
"Bahaya":"Relatif aman"
}

}

# ================= SIDEBAR =================

menu=st.sidebar.radio(
"ChemAssist",
["Home","Larutan","pH","Database"],
index=["Home","Larutan","pH","Database"].index(st.session_state.page)
)

st.session_state.page=menu

# ================= HOME =================

if menu=="Home":

    st.markdown("""
    <div class='header'>
    <h1>🧪 ChemAssist</h1>
    <p>Laboratory Chemistry Assistant</p>
    </div>
    """,unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    c1.metric("📚 Database",f"{len(db)}+")
    c2.metric("⚗️ Senyawa",f"{len(data_ph)}+")
    c3.metric("Version","6.0")

    a,b,c=st.columns(3)

    with a:

        st.markdown(
        "<div class='card'><h3>💧 Larutan</h3></div>",
        unsafe_allow_html=True
        )

        if st.button("Buka Larutan"):
            st.session_state.page="Larutan"
            st.rerun()

    with b:

        st.markdown(
        "<div class='card'><h3>⚗️ pH</h3></div>",
        unsafe_allow_html=True
        )

        if st.button("Buka pH"):
            st.session_state.page="pH"
            st.rerun()

    with c:

        st.markdown(
        "<div class='card'><h3>📚 Database</h3></div>",
        unsafe_allow_html=True
        )

        if st.button("Buka Database"):
            st.session_state.page="Database"
            st.rerun()

# ================= LARUTAN =================

elif menu=="Larutan":

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    st.title("💧 Perhitungan Larutan")

    mode=st.radio(
    "Pilih Jenis Perhitungan",
    ["Menentukan Massa","Pengenceran"]
    )

    # ---------- MASSA ----------

    if mode=="Menentukan Massa":

        jenis=st.selectbox(
        "Jenis Konsentrasi",
        ["Molaritas","Normalitas","ppm"]
        )

        # MOLARITAS
        if jenis=="Molaritas":

            Mr=st.number_input("Mr",40.0)
            M=st.number_input("Molaritas (M)",0.1)
            V=st.number_input("Volume (mL)",100.0)

            if st.button("Hitung"):

                massa=(Mr*M*V)/1000

                st.success(f"""
Massa zat yang harus ditimbang = {massa:.4f} gram
""")

                st.info(f"""
Langkah pembuatan larutan:

1. Timbang {massa:.4f} gram zat menggunakan neraca analitik
2. Larutkan dengan sedikit akuades di gelas beker
3. Pindahkan ke labu ukur {V} mL
4. Tambahkan akuades hingga tanda batas
5. Homogenkan larutan
""")

        # NORMALITAS
        elif jenis=="Normalitas":

            BE=st.number_input("Berat ekuivalen",40.0)
            N=st.number_input("Normalitas",0.1)
            V=st.number_input("Volume (mL)",100.0)

            if st.button("Hitung"):

                massa=(BE*N*V)/1000

                st.success(f"""
Massa zat yang harus ditimbang = {massa:.4f} gram
""")

        # PPM
        else:

            ppm=st.number_input("ppm",100.0)
            V=st.number_input("Volume (L)",1.0)

            if st.button("Hitung"):

                massa=ppm*V

                st.success(f"""
Massa zat yang harus ditimbang = {massa:.2f} mg
""")

    # ---------- PENGENCERAN ----------

    else:

        C1=st.number_input("Konsentrasi awal",10.0)
        C2=st.number_input("Konsentrasi akhir",1.0)
        V2=st.number_input("Volume akhir (mL)",100.0)

        if st.button("Hitung Pengenceran"):

            V1=(C2*V2)/C1

            st.success(f"""
Ambil {V1:.2f} mL larutan stok
""")

            st.info(f"""
Langkah pengenceran:

1. Pipet {V1:.2f} mL larutan stok
2. Masukkan ke labu ukur
3. Tambahkan akuades hingga volume {V2} mL
4. Tutup dan homogenkan larutan
""")

# ================= pH =================

elif menu=="pH":

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    st.title("⚗️ Kalkulator pH")

    senyawa=st.selectbox(
    "Pilih Senyawa",
    list(data_ph.keys()),
    format_func=lambda x:nama_senyawa.get(x,x)
    )

    info=data_ph[senyawa]

    st.info(info["jenis"])

    C=st.number_input("Konsentrasi (M)",0.01)

    if st.button("Hitung pH"):

        # ASAM KUAT
        if "Asam kuat"==info["jenis"]:

            ph=-math.log10(C*info["valensi"])

        # BASA KUAT
        elif "Basa kuat"==info["jenis"]:

            poh=-math.log10(C*info["valensi"])
            ph=14-poh

        # ASAM LEMAH
        elif "Asam lemah"==info["jenis"]:

            H=math.sqrt(info["Ka"]*C)
            ph=-math.log10(H)

        # BASA LEMAH
        else:

            OH=math.sqrt(info["Kb"]*C)
            poh=-math.log10(OH)
            ph=14-poh

        st.metric("Nilai pH",f"{ph:.2f}")

# ================= DATABASE =================

elif menu=="Database":

    if st.button("⬅ Kembali ke Home"):
        st.session_state.page="Home"
        st.rerun()

    st.title("📚 Database Senyawa Kimia")

    cari=st.text_input("Cari bahan kimia")

    hasil=[
    x for x in db
    if cari.lower() in x.lower()
    ] if cari else list(db.keys())

    pilih=st.selectbox("Pilih Bahan",hasil)

    st.write("### Informasi Senyawa")

    st.write("Rumus Kimia :", pilih)
    st.write("Nama Senyawa :", db[pilih]["nama"])
    st.write("Jenis :", db[pilih]["jenis"])
    st.write("Mr :", db[pilih]["Mr"])

    st.warning("Bahaya : "+str(db[pilih]["Bahaya"]))
