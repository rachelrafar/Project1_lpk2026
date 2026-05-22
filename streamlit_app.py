import streamlit as st
import math

# ======================================
# KONFIGURASI
# ======================================

st.set_page_config(
    page_title="ChemAssist Pro",
    page_icon="🧪",
    layout="centered"
)

# ======================================
# CSS
# ======================================

st.markdown("""
<style>

/* Background */
.stApp{
background:linear-gradient(to bottom,#dbeafe,#ffffff);
}

/* Sidebar */
section[data-testid="stSidebar"]{
background:linear-gradient(to bottom,#93c5fd,#dbeafe);
}

/* Header */
.judul{
padding:20px;
border-radius:20px;
background:white;
text-align:center;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
margin-bottom:20px;
}

/* Card */
.card{
padding:15px;
border-radius:20px;
background:white;
box-shadow:0px 4px 10px rgba(0,0,0,0.1);
text-align:center;
}

/* Metric */
div[data-testid="stMetric"]{
background:white;
padding:10px;
border-radius:15px;
box-shadow:0px 4px 10px rgba(0,0,0,0.1);
}

/* Button */
.stButton>button{
width:100%;
height:50px;
border-radius:15px;
font-size:16px;
font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

# ======================================
# SIDEBAR MENU
# ======================================

menu=st.sidebar.radio(
"Menu",
[
"🏠 Home",
"💧 Pembuatan Larutan dan Pengenceran",
"🧬 Kalkulator pH",
"📦 Info Bahan Kimia"
],
index=[
"🏠 Home",
"💧 Pembuatan Larutan dan Pengenceran",
"🧬 Kalkulator pH",
"📦 Info Bahan Kimia"
].index(st.session_state.page)
)

# ======================================
# HOME
# ======================================

if "page" not in st.session_state:
    st.session_state.page="🏠 Home"

if menu=="🏠 Home":

    st.markdown("""
    <div class='judul'>
    <h1>🧪 ChemAssist Pro</h1>
    <h4>All in One Chemistry Laboratory Assistant</h4>
    </div>
    """,unsafe_allow_html=True)

    col1,col2,col3=st.columns(3)

    with col1:
        st.metric("📚 Database","15+")

    with col2:
        st.metric("🧮 Kalkulator","6")

    with col3:
        st.metric("⚡ Version","2.0")

    st.write("")

    c1,c2,c3=st.columns(3)

    with c1:

        st.markdown("""
        <div class='card'>
        <h2>💧 Larutan</h2>
        Molaritas, Normalitas, ppm, Pengenceran
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Menu Larutan"):
            st.session_state.page="💧 Pembuatan Larutan"
            st.rerun()

    with c2:

        st.markdown("""
        <div class='card'>
        <h2>🧬 pH</h2>
        Asam/Basa kuat dan lemah
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Menu pH"):
            st.session_state.page="🧬 Kalkulator pH"
            st.rerun()

    with c3:

        st.markdown("""
        <div class='card'>
        <h2>📦 Database</h2>
        Mr, rumus dan bahaya bahan
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Database"):
            st.session_state.page="📦 Database Bahan"
            st.rerun()

    st.info(
    "ChemAssist membantu perhitungan laboratorium menjadi lebih cepat dan praktis."
    )

# ======================================
# PEMBUATAN LARUTAN
# ======================================

elif menu=="💧 Pembuatan Larutan":

    st.header("💧 Kalkulator Larutan")

    pilihan=st.selectbox(
    "Pilih Perhitungan",
    [
    "Molaritas",
    "Normalitas",
    "ppm",
    "Pengenceran"
    ]
    )

    if pilihan=="Molaritas":

        Mr=st.number_input(
        "Mr (g/mol)",
        min_value=0.0,
        value=40.0
        )

        M=st.number_input(
        "Molaritas (M)",
        min_value=0.0,
        value=0.1
        )

        V=st.number_input(
        "Volume (mL)",
        min_value=0.0,
        value=100.0
        )

        if st.button("Hitung Massa"):

            massa=(M*Mr*V)/1000

            st.success(
            f"Massa yang dibutuhkan = {massa:.4f} gram"
            )

    elif pilihan=="Normalitas":

        BE=st.number_input(
        "Berat Ekivalen",
        min_value=0.0,
        value=40.0
        )

        N=st.number_input(
        "Normalitas",
        min_value=0.0,
        value=0.1
        )

        V=st.number_input(
        "Volume (mL)",
        min_value=0.0,
        value=100.0
        )

        if st.button("Hitung Normalitas"):

            massa=(N*BE*V)/1000

            st.success(
            f"Massa yang dibutuhkan = {massa:.4f} gram"
            )

    elif pilihan=="ppm":

        ppm=st.number_input(
        "Nilai ppm",
        min_value=0.0,
        value=100.0
        )

        V=st.number_input(
        "Volume (L)",
        min_value=0.0,
        value=1.0
        )

        if st.button("Hitung ppm"):

            massa=ppm*V

            st.success(
            f"Massa yang dibutuhkan = {massa:.2f} mg"
            )

    else:

        M1=st.number_input(
        "Konsentrasi Awal",
        min_value=0.0,
        value=10.0
        )

        M2=st.number_input(
        "Konsentrasi Akhir",
        min_value=0.0,
        value=1.0
        )

        V2=st.number_input(
        "Volume Akhir (mL)",
        min_value=0.0,
        value=100.0
        )

        if st.button("Hitung Pengenceran"):

            V1=(M2*V2)/M1

            st.success(
            f"Volume stok yang diperlukan = {V1:.2f} mL"
            )

# ======================================
# KALKULATOR PH
# ======================================

elif menu=="🧬 Kalkulator pH":

    st.header("🧬 Kalkulator pH")

    jenis=st.selectbox(
    "Jenis Larutan",
    [
    "Asam kuat",
    "Basa kuat",
    "Asam lemah",
    "Basa lemah"
    ]
    )

    konsentrasi=st.number_input(
    "Konsentrasi (M)",
    min_value=0.000001,
    value=0.01,
    format="%.6f"
    )

    ph=0

    if jenis=="Asam kuat":

        valensi=st.number_input(
        "Valensi H+",
        min_value=1,
        max_value=5,
        value=1
        )

        H=konsentrasi*valensi
        ph=-math.log10(H)

    elif jenis=="Basa kuat":

        valensi=st.number_input(
        "Valensi OH-",
        min_value=1,
        max_value=5,
        value=1
        )

        OH=konsentrasi*valensi
        poh=-math.log10(OH)
        ph=14-poh

    elif jenis=="Asam lemah":

        Ka=st.number_input(
        "Ka",
        value=1.8e-5,
        format="%e"
        )

        H=math.sqrt(Ka*konsentrasi)
        ph=-math.log10(H)

    elif jenis=="Basa lemah":

        Kb=st.number_input(
        "Kb",
        value=1.8e-5,
        format="%e"
        )

        OH=math.sqrt(Kb*konsentrasi)

        poh=-math.log10(OH)
        ph=14-poh

    if st.button("Hitung pH"):

        st.metric(
        "Nilai pH",
        f"{ph:.2f}"
        )

        st.write(f"**Jenis Larutan : {jenis}**")

        if ph<7:
            st.error("Sifat : Asam")

        elif ph>7:
            st.success("Sifat : Basa")

        else:
            st.info("Sifat : Netral")

# ======================================
# DATABASE BAHAN
# ======================================

elif menu=="📦 Database Bahan":

    st.header("📦 Database Bahan Kimia")

    data={

    "HCl":{"Formula":"HCl","Mr":36.46,"Bahaya":"Korosif"},
    "NaOH":{"Formula":"NaOH","Mr":40.00,"Bahaya":"Korosif"},
    "H₂SO₄":{"Formula":"H₂SO₄","Mr":98.07,"Bahaya":"Korosif kuat"},
    "HNO₃":{"Formula":"HNO₃","Mr":63.01,"Bahaya":"Oksidator"},
    "NH₃":{"Formula":"NH₃","Mr":17.03,"Bahaya":"Iritasi"},
    "NaCl":{"Formula":"NaCl","Mr":58.44,"Bahaya":"Rendah"},
    "KMnO₄":{"Formula":"KMnO₄","Mr":158.03,"Bahaya":"Oksidator"},
    "K₂Cr₂O₇":{"Formula":"K₂Cr₂O₇","Mr":294.18,"Bahaya":"Toksik"},
    "Etanol":{"Formula":"C₂H₅OH","Mr":46.07,"Bahaya":"Mudah terbakar"},
    "Metanol":{"Formula":"CH₃OH","Mr":32.04,"Bahaya":"Toksik"},
    "Aseton":{"Formula":"C₃H₆O","Mr":58.08,"Bahaya":"Mudah terbakar"},
    "AgNO₃":{"Formula":"AgNO₃","Mr":169.87,"Bahaya":"Oksidator"},
    "CuSO₄":{"Formula":"CuSO₄","Mr":159.61,"Bahaya":"Berbahaya bagi lingkungan"},
    "FeCl₃":{"Formula":"FeCl₃","Mr":162.2,"Bahaya":"Iritasi"},
    "Akuades":{"Formula":"H₂O","Mr":18.02,"Bahaya":"Aman"}
    }

    bahan=st.selectbox(
    "Pilih Bahan",
    list(data.keys())
    )

    x=data[bahan]

    st.subheader(bahan)

    st.write(f"**Rumus :** {x['Formula']}")
    st.write(f"**Mr :** {x['Mr']} g/mol")
    st.warning(f"⚠️ Bahaya : {x['Bahaya']}")
