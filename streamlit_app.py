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
# CSS
# ==========================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(to bottom,#dbeafe,#ffffff);
}

section[data-testid="stSidebar"]{
background:linear-gradient(to bottom,#bfdbfe,#dbeafe);
}

.judul{
padding:25px;
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
box-shadow:0px 4px 10px rgba(0,0,0,.1);
text-align:center;
margin-bottom:10px;
}

div[data-testid="stMetric"]{
background:white;
padding:15px;
border-radius:15px;
box-shadow:0px 4px 10px rgba(0,0,0,.1);
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

# ==========================================
# SESSION
# ==========================================

if "page" not in st.session_state:
    st.session_state.page="🏠 Home"

# ==========================================
# SIDEBAR
# ==========================================

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

# ==========================================
# HOME
# ==========================================

if menu=="🏠 Home":

    st.markdown("""
    <div class='judul'>
    <h1>🧪 ChemAssist Pro</h1>
    <h4>All in One Chemistry Laboratory Assistant</h4>
    </div>
    """,unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric("📚 Database","20+")

    with c2:
        st.metric("🧮 Kalkulator","8")

    with c3:
        st.metric("⚡ Version","3.0")

    st.write("")

    a,b,c=st.columns(3)

    with a:

        st.markdown("""
        <div class='card'>
        <h2>💧 Larutan</h2>
        Molaritas, Normalitas, ppm
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Larutan"):
            st.session_state.page="💧 Pembuatan Larutan"
            st.rerun()

    with b:

        st.markdown("""
        <div class='card'>
        <h2>🧬 pH</h2>
        Asam/Basa kuat dan lemah
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka pH"):
            st.session_state.page="🧬 Kalkulator pH"
            st.rerun()

    with c:

        st.markdown("""
        <div class='card'>
        <h2>📦 Database</h2>
        Rumus, Mr, Bahaya
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Database"):
            st.session_state.page="📦 Database Bahan"
            st.rerun()

# ==========================================
# PEMBUATAN LARUTAN
# ==========================================

elif menu=="💧 Pembuatan Larutan":

    if st.button("⬅ Back ke Home"):
        st.session_state.page="🏠 Home"
        st.rerun()

    st.header("💧 Kalkulator Larutan")

    menu_larutan=st.radio(
    "Pilih",
    ["Menentukan Massa","Pengenceran"]
    )

    if menu_larutan=="Menentukan Massa":

        sub=st.selectbox(
        "Metode",
        ["Molaritas","Normalitas","ppm"]
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

            if st.button("Hitung Massa"):

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

        else:

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

        metode=st.selectbox(
        "Metode Pengenceran",
        ["Molaritas","Normalitas"]
        )

        if metode=="Molaritas":

            M1=st.number_input("M1",value=10.0)
            M2=st.number_input("M2",value=1.0)
            V2=st.number_input("V2",value=100.0)

            if st.button("Hitung"):

                V1=(M2*V2)/M1

                st.success(
                f"Volume stok={V1:.2f} mL"
                )

# ==========================================
# KALKULATOR PH
# ==========================================

elif menu=="🧬 Kalkulator pH":

    if st.button("⬅ Back ke Home"):
        st.session_state.page="🏠 Home"
        st.rerun()

    st.header("🧬 Kalkulator pH")

data_ph={

# ASAM KUAT
"HCl":{"jenis":"Asam kuat","valensi":1},
"HBr":{"jenis":"Asam kuat","valensi":1},
"HI":{"jenis":"Asam kuat","valensi":1},
"HNO₃":{"jenis":"Asam kuat","valensi":1},
"HClO₄":{"jenis":"Asam kuat","valensi":1},
"H₂SO₄":{"jenis":"Asam kuat","valensi":2},

# BASA KUAT
"NaOH":{"jenis":"Basa kuat","valensi":1},
"KOH":{"jenis":"Basa kuat","valensi":1},
"LiOH":{"jenis":"Basa kuat","valensi":1},
"RbOH":{"jenis":"Basa kuat","valensi":1},
"CsOH":{"jenis":"Basa kuat","valensi":1},
"Ba(OH)₂":{"jenis":"Basa kuat","valensi":2},
"Ca(OH)₂":{"jenis":"Basa kuat","valensi":2},
"Sr(OH)₂":{"jenis":"Basa kuat","valensi":2},

# ASAM LEMAH
"CH₃COOH":{"jenis":"Asam lemah","Ka":1.8e-5,"valensi":1},
"HF":{"jenis":"Asam lemah","Ka":6.8e-4,"valensi":1},
"HCOOH":{"jenis":"Asam lemah","Ka":1.8e-4,"valensi":1},
"HCN":{"jenis":"Asam lemah","Ka":4.9e-10,"valensi":1},
"H₂CO₃":{"jenis":"Asam lemah","Ka":4.3e-7,"valensi":2},
"H₃PO₄":{"jenis":"Asam lemah","Ka":7.5e-3,"valensi":3},
"C₆H₈O₇":{"jenis":"Asam lemah","Ka":7.4e-4,"valensi":3},
"C₄H₆O₆":{"jenis":"Asam lemah","Ka":9.2e-4,"valensi":2},
"H₂S":{"jenis":"Asam lemah","Ka":1e-7,"valensi":2},
"HClO":{"jenis":"Asam lemah","Ka":3e-8,"valensi":1},

# BASA LEMAH
"NH₄OH":{"jenis":"Basa lemah","Kb":1.8e-5,"valensi":1},
"NH₃":{"jenis":"Basa lemah","Kb":1.8e-5,"valensi":1},
"CH₃NH₂":{"jenis":"Basa lemah","Kb":4.4e-4,"valensi":1},
"C₂H₅NH₂":{"jenis":"Basa lemah","Kb":5.6e-4,"valensi":1},
"C₆H₅NH₂":{"jenis":"Basa lemah","Kb":4.3e-10,"valensi":1},
"(CH₃)₂NH":{"jenis":"Basa lemah","Kb":5.4e-4,"valensi":1},
"(CH₃)₃N":{"jenis":"Basa lemah","Kb":6.3e-5,"valensi":1}

}

    senyawa=st.selectbox(
    "Pilih Senyawa",
    list(data_ph.keys())
    )

    info=data_ph[senyawa]

    st.write(
    f"Jenis : {info['jenis']}"
    )

    konsentrasi=st.number_input(
    "Konsentrasi",
    value=0.01
    )

    if st.button("Hitung pH"):

        jenis=info["jenis"]
        valensi=info["valensi"]

        if jenis=="Asam kuat":

            H=konsentrasi*valensi
            ph=-math.log10(H)

        elif jenis=="Basa kuat":

            OH=konsentrasi*valensi
            ph=14+math.log10(OH)

        elif jenis=="Asam lemah":

            H=math.sqrt(
            info["Ka"]*
            konsentrasi*
            valensi
            )

            ph=-math.log10(H)

        elif jenis=="Basa lemah":

            OH=math.sqrt(
            info["Kb"]*
            konsentrasi*
            valensi
            )

            ph=14+math.log10(OH)

        st.metric(
        "Nilai pH",
        f"{ph:.2f}"
        )

        st.info(
        f"Sifat : {jenis}"
        )

# ==========================================
# DATABASE
# ==========================================

elif menu=="📦 Database Bahan":

    if st.button("⬅ Back ke Home"):
        st.session_state.page="🏠 Home"
        st.rerun()

    st.header("📦 Database Bahan")

    data={

"HCl":{"Mr":36.46,"Bahaya":"Korosif"},
"H₂SO₄":{"Mr":98.07,"Bahaya":"Korosif"},
"NaOH":{"Mr":40,"Bahaya":"Korosif"},
"NH₃":{"Mr":17.03,"Bahaya":"Iritasi"},
"Etanol":{"Mr":46.07,"Bahaya":"Mudah terbakar"},
"Metanol":{"Mr":32.04,"Bahaya":"Toksik"},
"CuSO₄":{"Mr":159.61,"Bahaya":"Bahaya lingkungan"}

}

    pilih=st.selectbox(
    "Pilih bahan",
    list(data.keys())
    )

    x=data[pilih]

    st.write(f"Mr : {x['Mr']} g/mol")
    st.warning(f"Bahaya : {x['Bahaya']}")
