import streamlit as st
import math

# ==========================================
# KONFIGURASI
# ==========================================
st.set_page_config(
    page_title="ChemAssist Pro",
    page_icon="🧪",
    layout="centered"
)

# ==========================================
# CSS TAMBAHAN
# ==========================================
st.markdown("""
<style>

/* Background utama */
.stApp{
    background: linear-gradient(to bottom,#e3f2fd,#ffffff);
}

/* Judul */
.judul{
    text-align:center;
    padding:20px;
    border-radius:20px;
    background:white;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom:25px;
}

/* Kartu fitur */
.card{
    padding:20px;
    border-radius:20px;
    background:white;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
    text-align:center;
    margin:10px;
}

/* Tombol */
.stButton>button{
    width:100%;
    border-radius:15px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

/* Metric */
div[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
}

/* Tab */
button[data-baseweb="tab"]{
    font-size:16px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# TAB
# ==========================================
tab0, tab1, tab2, tab3 = st.tabs([
with tab0:

    st.markdown("""
    <div class='judul'>
    <h1>🧪 ChemAssist Pro</h1>
    <h4>All in One Chemistry Laboratory Assistant</h4>
    </div>
    """,unsafe_allow_html=True)

    col1,col2,col3=st.columns(3)

    with col1:
        st.metric(
        "📚 Database",
        "15+"
        )

    with col2:
        st.metric(
        "🧮 Fitur",
        "6"
        )

    with col3:
        st.metric(
        "⚡ Version",
        "2.0"
        )

    st.write("")

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown("""
        <div class='card'>
        <h3>💧 Larutan</h3>
        Hitung Molaritas, Normalitas, ppm dan Pengenceran
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='card'>
        <h3>🧬 pH</h3>
        Asam kuat, basa kuat, asam lemah, basa lemah
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='card'>
        <h3>📦 MSDS Mini</h3>
        Informasi bahan dan tingkat bahaya
        </div>
        """,unsafe_allow_html=True)

    st.info("💡 ChemAssist membantu perhitungan praktikum kimia menjadi lebih cepat dan praktis")

with tab0:

    st.title("🧪 ChemAssist Pro")
    st.subheader("All in One Chemistry Laboratory Assistant")

    st.markdown("""
    ### Selamat Datang 👋

    ChemAssist membantu praktikum kimia dengan fitur:

    ✅ Pembuatan larutan (Molaritas, Normalitas, ppm)  
    ✅ Pengenceran larutan  
    ✅ Kalkulator pH (asam kuat/lemah & basa kuat/lemah)  
    ✅ Database bahan kimia lengkap  
    ✅ Informasi bahaya bahan (mini MSDS)  

    ---
    """)

    col1,col2,col3=st.columns(3)

    with col1:
        st.metric("Database Bahan","15+")

    with col2:
        st.metric("Mode Perhitungan","6")

    with col3:
        st.metric("Versi","2.0")

    st.image(
        "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69",
        width=700
        )

# ==========================================
# TAB PEMBUATAN LARUTAN
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

# ==================
# MOLARITAS
# ==================

    if pilihan=="Molaritas":

        mr=st.number_input(
            "Mr",
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

        if st.button("Hitung"):

            massa=(M*mr*V)/1000

            st.success(
                f"Massa zat = {massa:.4f} gram"
            )

# ==================
# NORMALITAS
# ==================

    elif pilihan=="Normalitas":

        BE=st.number_input(
            "Berat Ekivalen",
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

        if st.button("Hitung N"):

            massa=(N*BE*V)/1000

            st.success(
                f"Massa zat = {massa:.4f} gram"
            )

# ==================
# PPM
# ==================

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
                f"Massa zat = {massa:.2f} mg"
            )

# ==================
# PENGENCERAN
# ==================

    else:

        M1=st.number_input(
            "Konsentrasi awal",
            value=10.0
        )

        M2=st.number_input(
            "Konsentrasi akhir",
            value=1.0
        )

        V2=st.number_input(
            "Volume akhir",
            value=100.0
        )

        if st.button("Hitung Pengenceran"):

            V1=(M2*V2)/M1

            st.success(
                f"Volume stok = {V1:.2f} mL"
            )

# ==========================================
# KALKULATOR PH
# ==========================================

with tab2:

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
        value=0.01
    )

# ============
# ASAM KUAT
# ============

    if jenis=="Asam kuat":

        H=konsentrasi
        ph=-math.log10(H)

# ============
# BASA KUAT
# ============

    elif jenis=="Basa kuat":

        poh=-math.log10(konsentrasi)
        ph=14-poh

# ============
# ASAM LEMAH
# ============

    elif jenis=="Asam lemah":

        Ka=st.number_input(
            "Ka",
            value=1.8e-5,
            format="%e"
        )

        H=math.sqrt(Ka*konsentrasi)

        ph=-math.log10(H)

# ============
# BASA LEMAH
# ============

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

# ==========================================
# DATABASE BAHAN KIMIA
# ==========================================

with tab3:

    st.header("📦 Database Bahan Kimia")

    data={

    "HCl":{
    "Formula":"HCl",
    "Mr":36.46,
    "Bahaya":"Korosif"
    },

    "NaOH":{
    "Formula":"NaOH",
    "Mr":40,
    "Bahaya":"Korosif"
    },

    "H2SO4":{
    "Formula":"H₂SO₄",
    "Mr":98.07,
    "Bahaya":"Korosif kuat"
    },

    "HNO3":{
    "Formula":"HNO₃",
    "Mr":63,
    "Bahaya":"Oksidator"
    },

    "NH3":{
    "Formula":"NH₃",
    "Mr":17,
    "Bahaya":"Iritasi"
    },

    "NaCl":{
    "Formula":"NaCl",
    "Mr":58.44,
    "Bahaya":"Rendah"
    },

    "KMnO4":{
    "Formula":"KMnO₄",
    "Mr":158.03,
    "Bahaya":"Oksidator kuat"
    },

    "K2Cr2O7":{
    "Formula":"K₂Cr₂O₇",
    "Mr":294.18,
    "Bahaya":"Toksik"
    },

    "Etanol":{
    "Formula":"C₂H₅OH",
    "Mr":46.07,
    "Bahaya":"Mudah terbakar"
    },

    "Metanol":{
    "Formula":"CH₃OH",
    "Mr":32.04,
    "Bahaya":"Toksik"
    },

    "Aseton":{
    "Formula":"C₃H₆O",
    "Mr":58.08,
    "Bahaya":"Mudah terbakar"
    },

    "AgNO3":{
    "Formula":"AgNO₃",
    "Mr":169.87,
    "Bahaya":"Oksidator"
    },

    "CuSO4":{
    "Formula":"CuSO₄",
    "Mr":159.61,
    "Bahaya":"Berbahaya bagi lingkungan"
    },

    "Akuades":{
    "Formula":"H₂O",
    "Mr":18,
    "Bahaya":"Aman"
    }

    }

    pilih=st.selectbox(
        "Pilih bahan",
        list(data.keys())
    )

    x=data[pilih]

    st.write(
        f"**Rumus:** {x['Formula']}"
    )

    st.write(
        f"**Mr:** {x['Mr']} g/mol"
    )

    st.warning(
        f"Bahaya: {x['Bahaya']}"
    )
