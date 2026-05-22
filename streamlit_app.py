import streamlit as st
import math

# ====================================
# KONFIGURASI
# ====================================

st.set_page_config(
    page_title="ChemAssist Pro",
    page_icon="🧪",
    layout="centered"
)

# ====================================
# CSS
# ====================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(to bottom,#dbeafe,#ffffff);
}

section[data-testid="stSidebar"]{
background:linear-gradient(to bottom,#93c5fd,#dbeafe);
}

.judul{
padding:20px;
border-radius:20px;
background:white;
text-align:center;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
margin-bottom:20px;
}

.card{
padding:20px;
border-radius:20px;
background:white;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
text-align:center;
margin-bottom:10px;
}

div[data-testid="stMetric"]{
background:white;
padding:10px;
border-radius:15px;
box-shadow:0px 4px 10px rgba(0,0,0,0.1);
}

.stButton>button{
width:100%;
height:50px;
border-radius:15px;
font-size:15px;
font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

# ====================================
# SESSION
# ====================================

if "page" not in st.session_state:
    st.session_state.page="🏠 Home"

# ====================================
# SIDEBAR
# ====================================

st.sidebar.title("🧪 ChemAssist Pro")

menu=st.sidebar.radio(
"Menu",
[
"🏠 Home",
"💧 Pembuatan Larutan",
"🧬 Kalkulator pH",
"📦 Database Bahan"
],
index=[
"🏠 Home",
"💧 Pembuatan Larutan",
"🧬 Kalkulator pH",
"📦 Database Bahan"
].index(st.session_state.page)
)

st.session_state.page=menu

# ====================================
# HOME
# ====================================

if menu=="🏠 Home":

    st.markdown("""
    <div class='judul'>
    <h1>🧪 ChemAssist Pro</h1>
    <h4>All in One Chemistry Laboratory Assistant</h4>
    </div>
    """,unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric("📚 Database","15+")

    with c2:
        st.metric("🧮 Kalkulator","8")

    with c3:
        st.metric("⚡ Version","2.1")

    st.write("")

    a,b,c=st.columns(3)

    with a:

        st.markdown("""
        <div class='card'>
        <h2>💧 Larutan</h2>
        Molaritas, Normalitas, ppm
        </div>
        """,unsafe_allow_html=True)

        if st.button("Larutan"):
            st.session_state.page="💧 Pembuatan Larutan"
            st.rerun()

    with b:

        st.markdown("""
        <div class='card'>
        <h2>🧬 pH</h2>
        Asam/Basa kuat dan lemah
        </div>
        """,unsafe_allow_html=True)

        if st.button("pH"):
            st.session_state.page="🧬 Kalkulator pH"
            st.rerun()

    with c:

        st.markdown("""
        <div class='card'>
        <h2>📦 Database</h2>
        Rumus, Mr, Bahaya
        </div>
        """,unsafe_allow_html=True)

        if st.button("Database"):
            st.session_state.page="📦 Database Bahan"
            st.rerun()

# ====================================
# LARUTAN
# ====================================

elif menu=="💧 Pembuatan Larutan":

    st.header("💧 Kalkulator Larutan")

    menu_larutan=st.radio(
    "Pilih",
    [
    "Menentukan Massa Yang Akan Ditimbang",
    "Pengenceran"
    ]
    )

# ====================
# MENENTUKAN MASSA
# ====================

    if menu_larutan=="Menentukan Massa":

        sub=st.selectbox(
        "Jenis Perhitungan",
        [
        "Molaritas",
        "Normalitas",
        "ppm"
        ]
        )

        if sub=="Molaritas":

            Mr=st.number_input(
            "Mr",
            value=40.0
            )

            M=st.number_input(
            "Molaritas",
            value=0.1
            )

            V=st.number_input(
            "Volume (mL)",
            value=100.0
            )

            if st.button("Hitung"):

                massa=(M*Mr*V)/1000

                st.success(
                f"Massa = {massa:.4f} gram"
                )

        elif sub=="Normalitas":

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

# ====================
# PENGENCERAN
# ====================

    elif menu_larutan=="Pengenceran":

        sub2=st.selectbox(
        "Jenis Pengenceran",
        [
        "Molaritas",
        "Normalitas"
        ]
        )

        if sub2=="Molaritas":

            M1=st.number_input(
            "M1",
            value=10.0
            )

            M2=st.number_input(
            "M2",
            value=1.0
            )

            V2=st.number_input(
            "V2 (mL)",
            value=100.0
            )

            if st.button("Hitung Pengenceran"):

                V1=(M2*V2)/M1

                st.success(
                f"V1 = {V1:.2f} mL"
                )

        elif sub2=="Normalitas":

            N1=st.number_input(
            "N1",
            value=10.0
            )

            N2=st.number_input(
            "N2",
            value=1.0
            )

            V2=st.number_input(
            "V2 (mL)",
            value=100.0
            )

            if st.button("Hitung"):

                V1=(N2*V2)/N1

                st.success(
                f"V1 = {V1:.2f} mL"
                )

# ====================================
# KALKULATOR PH
# ====================================

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

# ======================
# ASAM KUAT
# ======================

    if jenis=="Asam kuat":

        valensi=st.number_input(
        "Valensi H⁺",
        min_value=1,
        value=1
        )

        if st.button("Hitung pH"):

            H=konsentrasi*valensi

            ph=-math.log10(H)

            st.metric(
            "Nilai pH",
            f"{ph:.2f}"
            )

            st.error("Sifat : Asam kuat")


# ======================
# BASA KUAT
# ======================

    elif jenis=="Basa kuat":

        valensi=st.number_input(
        "Valensi OH⁻",
        min_value=1,
        value=1
        )

        if st.button("Hitung pH"):

            OH=konsentrasi*valensi

            poh=-math.log10(OH)

            ph=14-poh

            st.metric(
            "Nilai pH",
            f"{ph:.2f}"
            )

            st.success("Sifat : Basa kuat")

# ======================
# ASAM LEMAH
# ======================

    elif jenis=="Asam lemah":

        Ka=st.number_input(
        "Ka",
        min_value=0.0,
        value=1.8e-5,
        format="%e"
        )

        valensi=st.number_input(
        "Valensi H⁺",
        min_value=1,
        value=1
        )

        if st.button("Hitung pH"):

            H=math.sqrt(
            Ka*konsentrasi*valensi
            )

            ph=-math.log10(H)

            st.metric(
            "Nilai pH",
            f"{ph:.2f}"
            )

            st.warning(
            "Sifat : Asam lemah"
            )

# ======================
# BASA LEMAH
# ======================

    elif jenis=="Basa lemah":

        Kb=st.number_input(
        "Kb",
        min_value=0.0,
        value=1.8e-5,
        format="%e"
        )

        valensi=st.number_input(
        "Valensi OH⁻",
        min_value=1,
        value=1
        )

        if st.button("Hitung pH"):

            OH=math.sqrt(
            Kb*konsentrasi*valensi
            )

            poh=-math.log10(OH)

            ph=14-poh

            st.metric(
            "Nilai pH",
            f"{ph:.2f}"
            )

            st.info(
            "Sifat : Basa lemah"
            )
# ====================================
# DATABASE
# ====================================

elif menu=="📦 Database Bahan":

    st.header("📦 Database Bahan")

    data={

"HCl":{"Mr":36.46,"Bahaya":"Korosif"},
"H₂SO₄":{"Mr":98.07,"Bahaya":"Korosif"},
"NaOH":{"Mr":40,"Bahaya":"Korosif"},
"NH₃":{"Mr":17.03,"Bahaya":"Iritasi"},
"Etanol":{"Mr":46.07,"Bahaya":"Mudah terbakar"},
"Metanol":{"Mr":32.04,"Bahaya":"Toksik"},
"KMnO₄":{"Mr":158.03,"Bahaya":"Oksidator"},
"AgNO₃":{"Mr":169.87,"Bahaya":"Oksidator"},
"CuSO₄":{"Mr":159.61,"Bahaya":"Bahaya lingkungan"}

}

    pilih=st.selectbox(
    "Pilih Bahan",
    list(data.keys())
    )

    x=data[pilih]

    st.write(
    f"Mr : {x['Mr']} g/mol"
    )

    st.warning(
    f"Bahaya : {x['Bahaya']}"
    )
