import streamlit as st
import math

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="ChemAssist Pro",
    page_icon="🧪",
    layout="centered"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Background */
.stApp{
background:linear-gradient(to bottom,#dbeafe,#ffffff);
}

/* Header */
.judul{
padding:20px;
border-radius:20px;
text-align:center;
background:white;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
margin-bottom:20px;
}

/* Card */
.card{
padding:15px;
border-radius:20px;
background:white;
text-align:center;
box-shadow:0px 4px 10px rgba(0,0,0,0.1);
margin:5px;
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

/* Tab */
button[data-baseweb="tab"]{
font-size:15px;
border-radius:10px;
}

</style>
""",unsafe_allow_html=True)

# ==========================================
# TAB
# ==========================================

tab0,tab1,tab2,tab3=st.tabs([
"🏠 Home",
"💧 Pembuatan Larutan",
"🧬 Kalkulator pH",
"📦 Database Bahan"
])

# ==========================================
# HOME
# ==========================================

with tab0:

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
        st.metric("⚡ Fitur","6")

    with col3:
        st.metric("🧮 Version","2.0")

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
        <h3>🧬 pH</h3>
        Asam kuat/lemah dan basa kuat/lemah
        </div>
        """,unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class='card'>
        <h3>📦 Bahan Kimia</h3>
        Info Mr dan bahaya bahan
        </div>
        """,unsafe_allow_html=True)

    st.info(
    "ChemAssist membantu menghitung kebutuhan praktikum laboratorium secara cepat dan praktis."
    )

# ==========================================
# PEMBUATAN LARUTAN
# ==========================================

with tab1:

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

    # Molaritas
    if pilihan=="Molaritas":

        Mr=st.number_input(
        "Mr (g/mol)",
        value=40.0
        )

        M=st.number_input(
        "Molaritas (M)",
        value=0.1
        )

        V=st.number_input(
        "Volume (mL)",
        value=100.0
        )

        if st.button("Hitung Massa"):

            massa=(M*Mr*V)/1000

            st.success(
            f"Massa yang dibutuhkan = {massa:.4f} gram"
            )

    # Normalitas
    elif pilihan=="Normalitas":

        BE=st.number_input(
        "Berat Ekivalen",
        value=40.0
        )

        N=st.number_input(
        "Normalitas (N)",
        value=0.1
        )

        V=st.number_input(
        "Volume (mL)",
        value=100.0
        )

        if st.button("Hitung Normalitas"):

            massa=(N*BE*V)/1000

            st.success(
            f"Massa yang dibutuhkan = {massa:.4f} gram"
            )

    # ppm
    elif pilihan=="ppm":

        ppm=st.number_input(
        "Nilai ppm",
        value=100.0
        )

        V=st.number_input(
        "Volume (L)",
        value=1.0
        )

        if st.button("Hitung ppm"):

            massa=ppm*V

            st.success(
            f"Massa yang dibutuhkan = {massa:.2f} mg"
            )

    # Pengenceran
    else:

        M1=st.number_input(
        "Konsentrasi Awal",
        value=10.0
        )

        M2=st.number_input(
        "Konsentrasi Akhir",
        value=1.0
        )

        V2=st.number_input(
        "Volume Akhir (mL)",
        value=100.0
        )

        if st.button("Hitung Pengenceran"):

            V1=(M2*V2)/M1

            st.success(
            f"Volume stok yang diperlukan = {V1:.2f} mL"
            )

# ==========================================
# KALKULATOR PH
# ==========================================

with tab2:

    st.header("🧬 Kalkulator pH")

    jenis=st.selectbox(
    "Pilih Jenis Larutan",
    [
    "Asam kuat",
    "Basa kuat",
    "Asam lemah",
    "Basa lemah"
    ]
    )

    konsentrasi=st.number_input(
    "Konsentrasi (M)",
    value=0.01
    )

    ph=0

    if jenis=="Asam kuat":

        H=konsentrasi
        ph=-math.log10(H)

    elif jenis=="Basa kuat":

        poh=-math.log10(konsentrasi)
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

        if ph<7:
            st.error("Larutan bersifat ASAM")

        elif ph>7:
            st.success("Larutan bersifat BASA")

        else:
            st.info("Larutan NETRAL")

# ==========================================
# DATABASE BAHAN KIMIA
# ==========================================

with tab3:

    st.header("📦 Database Bahan Kimia")

    data={

    "HCl":{"Formula":"HCl","Mr":36.46,"Bahaya":"Korosif"},
    "NaOH":{"Formula":"NaOH","Mr":40,"Bahaya":"Korosif"},
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

    pilih=st.selectbox(
    "Pilih bahan",
    list(data.keys())
    )

    x=data[pilih]

    st.subheader(pilih)

    st.write(
    f"**Rumus :** {x['Formula']}"
    )

    st.write(
    f"**Mr :** {x['Mr']} g/mol"
    )

    st.warning(
    f"⚠️ Bahaya : {x['Bahaya']}"
    )
