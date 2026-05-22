import streamlit as st
import math

# ==================================================
# KONFIGURASI
# ==================================================

st.set_page_config(
    page_title="ChemAssist",
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
# SIDEBAR
# ==================================================

menu=st.sidebar.radio(
"🧪 ChemAssist",
[
"Home",
"Pembuatan Larutan",
"Kalkulator pH",
"Database Bahan"
]
)

# ==================================================
# HOME
# ==================================================

if menu=="Home":

    st.markdown("""
    <div class='header'>
    <h1>🧪 ChemAssist</h1>
    <p>Laboratory Chemistry Assistant</p>
    </div>
    """,unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric("📚 Database","70+")

    with c2:
        st.metric("⚗️ Senyawa pH","50+")

    with c3:
        st.metric("Version","4.0")

    st.write("")

    a,b,c=st.columns(3)

    with a:
        st.markdown("""
        <div class='card'>
        <h3>💧 Larutan</h3>
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
        Mr dan informasi bahan
        </div>
        """,unsafe_allow_html=True)

# ==================================================
# LARUTAN
# ==================================================

elif menu=="Pembuatan Larutan":

    st.header("💧 Kalkulator Larutan")

    menu2=st.radio(
    "Pilih Menu",
    ["Menentukan Massa","Pengenceran"]
    )

    if menu2=="Menentukan Massa":

        sub=st.selectbox(
        "Jenis",
        ["Molaritas","Normalitas","ppm"]
        )

        if sub=="Molaritas":

            Mr=st.number_input("Mr",value=40.0)
            M=st.number_input("Molaritas",value=0.1)
            V=st.number_input("Volume (mL)",value=100.0)

            if st.button("Hitung"):

                massa=(M*Mr*V)/1000
                st.success(
                f"Massa = {massa:.4f} gram"
                )

        elif sub=="Normalitas":

            BE=st.number_input(
            "Berat ekivalen",
            value=40.0
            )

            N=st.number_input(
            "Normalitas",
            value=0.1
            )

            V=st.number_input(
            "Volume (mL)",
            value=100.0
            )

            if st.button("Hitung"):

                massa=(N*BE*V)/1000

                st.success(
                f"Massa = {massa:.4f} gram"
                )

        elif sub=="ppm":

            ppm=st.number_input(
            "ppm",
            value=100.0
            )

            V=st.number_input(
            "Volume (L)",
            value=1.0
            )

            if st.button("Hitung"):

                massa=ppm*V

                st.success(
                f"Massa = {massa:.2f} mg"
                )

    else:

        C1=st.number_input(
        "Konsentrasi awal",
        value=10.0
        )

        C2=st.number_input(
        "Konsentrasi akhir",
        value=1.0
        )

        V2=st.number_input(
        "Volume akhir",
        value=100.0
        )

        if st.button("Hitung Pengenceran"):

            if C1<=0:
                st.error("Konsentrasi awal tidak boleh nol")

            else:

                V1=(C2*V2)/C1

                st.success(
                f"Volume stok = {V1:.2f} mL"
                )

# ==================================================
# PH
# ==================================================

elif menu=="Kalkulator pH":

    st.header("⚗️ Kalkulator pH")

    data_ph={

    "HCl":{"jenis":"Asam kuat","valensi":1},
    "HNO3":{"jenis":"Asam kuat","valensi":1},
    "HBr":{"jenis":"Asam kuat","valensi":1},
    "HI":{"jenis":"Asam kuat","valensi":1},
    "H2SO4":{"jenis":"Asam kuat","valensi":2},

    "NaOH":{"jenis":"Basa kuat","valensi":1},
    "KOH":{"jenis":"Basa kuat","valensi":1},
    "Ba(OH)2":{"jenis":"Basa kuat","valensi":2},

    "CH3COOH":{"jenis":"Asam lemah","Ka":1.8e-5},
    "HF":{"jenis":"Asam lemah","Ka":6.8e-4},
    "HCOOH":{"jenis":"Asam lemah","Ka":1.8e-4},
    "HCN":{"jenis":"Asam lemah","Ka":4.9e-10},
    "H2CO3":{"jenis":"Asam lemah","Ka":4.3e-7},
    "H3PO4":{"jenis":"Asam lemah","Ka":7.5e-3},
    "H2S":{"jenis":"Asam lemah","Ka":1e-7},
    "HClO":{"jenis":"Asam lemah","Ka":3e-8},

    "NH3":{"jenis":"Basa lemah","Kb":1.8e-5},
    "NH4OH":{"jenis":"Basa lemah","Kb":1.8e-5},
    "CH3NH2":{"jenis":"Basa lemah","Kb":4.4e-4},
    "C2H5NH2":{"jenis":"Basa lemah","Kb":5.6e-4}
    }

    senyawa=st.selectbox(
    "Pilih senyawa",
    list(data_ph.keys())
    )

    info=data_ph[senyawa]

    st.info(
    f"Jenis : {info['jenis']}"
    )

    konsentrasi=st.number_input(
    "Konsentrasi (M)",
    min_value=0.0001,
    value=0.01
    )

    if st.button("Hitung pH"):

        if info["jenis"]=="Asam kuat":

            H=konsentrasi*info["valensi"]
            ph=-math.log10(H)

        elif info["jenis"]=="Basa kuat":

            OH=konsentrasi*info["valensi"]
            poh=-math.log10(OH)
            ph=14-poh

        elif info["jenis"]=="Asam lemah":

            H=math.sqrt(
            info["Ka"]*konsentrasi
            )
            ph=-math.log10(H)

        else:

            OH=math.sqrt(
            info["Kb"]*konsentrasi
            )
            poh=-math.log10(OH)
            ph=14-poh

        st.metric(
        "Nilai pH",
        f"{ph:.2f}"
        )

# ==================================================
# DATABASE
# ==================================================

elif menu=="Database Bahan":

    st.header("📚 Database Bahan")

    data={}

    bahan=[
"HCl","H2SO4","NaOH","KOH","NH3","NaCl","KCl","AgNO3",
"CuSO4","FeCl3","FeSO4","ZnSO4","MgSO4","CaCO3",
"Na2CO3","NaHCO3","CH3COOH","C2H5OH","CH3OH",
"Acetone","Benzene","Toluene","Glucose","KNO3",
"Pb(NO3)2","HgCl2","BaCl2","AlCl3","KI","NaI",
"CuCl2","MnSO4","CdCl2","Na2SO4","K2SO4",
"CaCl2","MgCl2","NaBr","KBr","NaF","KF",
"LiCl","NaNO3","KNO2","NaNO2","H2O2",
"KMnO4","K2Cr2O7","Na2S2O3","EDTA",
"Phenol","Urea","Sucrose","Formaldehyde",
"Citric acid","Oxalic acid","Benzoic acid",
"Boric acid","Aniline","Glycerol","Hexane",
"Heptane","Octane","Propanol","Butanol",
"Acetonitrile","Chloroform","Diethyl ether"
]

    for x in bahan:
        data[x]={
        "Mr":"Lihat MSDS",
        "Bahaya":"Periksa MSDS"
        }

    pilih=st.selectbox(
    "Pilih bahan",
    list(data.keys())
    )

    st.write(f"Rumus : {pilih}")
    st.write(f"Mr : {data[pilih]['Mr']}")
    st.warning(
    f"Bahaya : {data[pilih]['Bahaya']}"
    )
