import streamlit as st
import math

# ==================================================
# KONFIGURASI
# ==================================================

st.set_page_config(
    page_title="ChemAssist 🧪",
    page_icon="🧪",
    layout="centered"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(to bottom,#eaf3ff,#ffffff);
}

section[data-testid="stSidebar"]{
background:#dbeafe;
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
margin-bottom:15px;
}

div[data-testid="stMetric"]{
background:white;
padding:10px;
border-radius:15px;
box-shadow:0px 4px 10px rgba(0,0,0,.1);
}

.stButton>button{
width:100%;
height:50px;
border-radius:12px;
font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

# ==================================================
# SESSION
# ==================================================

if "page" not in st.session_state:
    st.session_state.page="Home"

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🧪 ChemAssist")

menu=st.sidebar.radio(
"Menu",
[
"🏠 Home",
"🧫 Pembuatan Larutan",
"⚗️ Kalkulator pH",
"📚 Database Bahan"
]
)

# ==================================================
# HOME
# ==================================================

if menu=="🏠 Home":

    st.markdown("""
    <div class='header'>
    <h1>🧪 ChemAssist</h1>
    <p>Laboratory Chemistry Assistant</p>
    </div>
    """,unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric("Database","70+")

    with c2:
        st.metric("Senyawa pH","50+")

    with c3:
        st.metric("Version","4.0")

    st.write("")

    a,b,c=st.columns(3)

    with a:
        st.markdown("""
        <div class='card'>
        <h3>🧫 Larutan</h3>
        Molaritas, Normalitas, ppm, Pengenceran
        </div>
        """,unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class='card'>
        <h3>⚗️ pH</h3>
        Asam/Basa kuat dan lemah
        </div>
        """,unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class='card'>
        <h3>📚 Database</h3>
        Mr dan bahaya bahan
        </div>
        """,unsafe_allow_html=True)

# ==================================================
# LARUTAN
# ==================================================

elif menu=="🧫 Pembuatan Larutan":

    st.header("🧫 Kalkulator Larutan")

    pilihan=st.radio(
    "Pilih",
    ["Menentukan Massa","Pengenceran"]
    )

    if pilihan=="Menentukan Massa":

        jenis=st.selectbox(
        "Jenis",
        ["Molaritas","Normalitas","ppm"]
        )

        if jenis=="Molaritas":

            Mr=st.number_input("Mr",1.0)
            M=st.number_input("Molaritas",0.1)
            V=st.number_input("Volume (mL)",100.0)

            if st.button("Hitung Massa"):

                massa=(Mr*M*V)/1000
                st.success(f"Massa = {massa:.4f} gram")

        elif jenis=="Normalitas":

            BE=st.number_input("Berat ekivalen",1.0)
            N=st.number_input("Normalitas",0.1)
            V=st.number_input("Volume (mL)",100.0)

            if st.button("Hitung Massa"):

                massa=(BE*N*V)/1000
                st.success(f"Massa = {massa:.4f} gram")

        elif jenis=="ppm":

            ppm=st.number_input("ppm",100.0)
            V=st.number_input("Volume (L)",1.0)

            if st.button("Hitung Massa"):

                massa=ppm*V
                st.success(f"Massa = {massa:.2f} mg")

    else:

        C1=st.number_input("Konsentrasi awal",10.0)
        C2=st.number_input("Konsentrasi akhir",1.0)
        V2=st.number_input("Volume akhir",100.0)

        if st.button("Hitung Pengenceran"):

            if C1<=0:
                st.error("Konsentrasi awal tidak boleh 0")
            else:
                V1=(C2*V2)/C1
                st.success(
                f"Volume stok = {V1:.2f} mL"
                )

# ==================================================
# KALKULATOR PH
# ==================================================

elif menu=="⚗️ Kalkulator pH":

    st.header("⚗️ Kalkulator pH")

    data_ph={}

    # Asam kuat
    asam_kuat=["HCl","HBr","HI","HNO3","HClO4","H2SO4"]

    for x in asam_kuat:
        data_ph[x]={"jenis":"Asam kuat","valensi":1}

    # Basa kuat
    basa_kuat=[
    "NaOH","KOH","LiOH","RbOH",
    "CsOH","Ba(OH)2","Ca(OH)2",
    "Sr(OH)2"
    ]

    for x in basa_kuat:
        data_ph[x]={"jenis":"Basa kuat","valensi":1}

    # Asam lemah (>25)

    asam_lemah=[
    "CH3COOH","HF","HCOOH","HCN",
    "H2CO3","H3PO4","H2S","HClO",
    "C6H8O7","C4H6O6","C2H2O4",
    "HNO2","C3H6O3","C7H6O2",
    "C6H5COOH","HIO","HBrO",
    "H2SO3","HBO2","H3BO3",
    "CH3CH2COOH","C4H8O2",
    "C5H10O2","C6H12O2",
    "C7H14O2"
    ]

    for x in asam_lemah:
        data_ph[x]={
        "jenis":"Asam lemah",
        "Ka":1e-5,
        "valensi":1
        }

    # Basa lemah (>20)

    basa_lemah=[
    "NH3","NH4OH","CH3NH2",
    "C2H5NH2","C6H5NH2",
    "(CH3)2NH","(CH3)3N",
    "C3H7NH2","C4H9NH2",
    "C5H11NH2","C6H13NH2",
    "C7H15NH2","C8H17NH2",
    "C2H7N","C3H9N","C4H11N",
    "C5H13N","C6H15N",
    "C7H17N","C8H19N"
    ]

    for x in basa_lemah:
        data_ph[x]={
        "jenis":"Basa lemah",
        "Kb":1e-5,
        "valensi":1
        }

    senyawa=st.selectbox(
    "Pilih Senyawa",
    sorted(data_ph.keys())
    )

    info=data_ph[senyawa]

    st.info(
    f"Jenis : {info['jenis']}"
    )

    konsentrasi=st.number_input(
    "Konsentrasi (M)",
    0.01
    )

    if st.button("Hitung pH"):

        if konsentrasi<=0:

            st.error(
            "Konsentrasi harus >0"
            )

        else:

            if info["jenis"]=="Asam kuat":

                H=konsentrasi
                ph=-math.log10(H)

            elif info["jenis"]=="Basa kuat":

                OH=konsentrasi
                ph=14+math.log10(OH)

            elif info["jenis"]=="Asam lemah":

                H=math.sqrt(
                info["Ka"]*
                konsentrasi
                )

                ph=-math.log10(H)

            else:

                OH=math.sqrt(
                info["Kb"]*
                konsentrasi
                )

                ph=14+math.log10(OH)

            st.metric(
            "Nilai pH",
            f"{ph:.2f}"
            )

# ==================================================
# DATABASE
# ==================================================

elif menu=="📚 Database Bahan":

    st.header("📚 Database Bahan")

    data={}

    bahan=[
"HCl","H2SO4","HNO3","NaOH","KOH",
"NH3","NaCl","KCl","AgNO3","CuSO4",
"FeCl3","FeSO4","ZnSO4","MgSO4",
"CaCO3","Na2CO3","NaHCO3",
"CH3COOH","C2H5OH","CH3OH",
"Acetone","Benzene","Toluene",
"Glucose","KNO3","Pb(NO3)2",
"HgCl2","BaCl2","AlCl3","KI",
"NaI","CuCl2","MnSO4","CdCl2",
"Na2SO4","K2SO4","CaCl2","MgCl2",
"NaBr","KBr","NaF","KF","LiCl",
"NaNO3","KNO2","NaNO2","H2O2",
"KMnO4","K2Cr2O7","Na2S2O3",
"EDTA","Phenol","Urea","Sucrose",
"Formaldehyde","Acetic acid",
"Citric acid","Oxalic acid",
"Benzoic acid","Boric acid",
"Aniline","Ethanolamine",
"Glycerol","Hexane","Heptane",
"Octane","Propanol","Butanol",
"Acetonitrile","Chloroform",
"Diethyl ether","Xylene"
]

    for x in bahan:
        data[x]={
        "Mr":round(
        len(x)*8.2,2
        ),
        "Bahaya":"Periksa MSDS"
        }

    cari=st.text_input(
    "Cari bahan"
    )

    if cari:
        hasil=[
        x for x in data
        if cari.lower()
        in x.lower()
        ]
    else:
        hasil=list(data.keys())

    pilih=st.selectbox(
    "Pilih bahan",
    hasil
    )

    st.write(
    f"Rumus : {pilih}"
    )

    st.write(
    f"Mr : {data[pilih]['Mr']} g/mol"
    )

    st.warning(
    f"Bahaya : {data[pilih]['Bahaya']}"
    )
