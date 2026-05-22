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
# SESSION
# ==================================================

if "page" not in st.session_state:
    st.session_state.page="Home"

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("ChemAssist")

menu=st.sidebar.radio(
"Menu",
[
"Home",
"Pembuatan Larutan",
"Kalkulator pH",
"Database Bahan"
],
index=[
"Home",
"Pembuatan Larutan",
"Kalkulator pH",
"Database Bahan"
].index(st.session_state.page)
)

st.session_state.page=menu

# ==================================================
# HOME
# ==================================================

if menu=="Home":

    st.markdown("""
    <div class='header'>
    <h1>ChemAssist</h1>
    <p>Laboratory Chemistry Assistant</p>
    </div>
    """,unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric("Database","40+")

    with c2:
        st.metric("Kalkulator","8")

    with c3:
        st.metric("Version","3.0")

    st.write("")

    a,b,c=st.columns(3)

    with a:
        st.markdown("""
        <div class='card'>
        <h3>Larutan</h3>
        Molaritas, Normalitas, ppm, Pengenceran
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Larutan"):
            st.session_state.page="Pembuatan Larutan"
            st.rerun()

    with b:
        st.markdown("""
        <div class='card'>
        <h3>pH</h3>
        Asam/Basa kuat dan lemah
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka pH"):
            st.session_state.page="Kalkulator pH"
            st.rerun()

    with c:
        st.markdown("""
        <div class='card'>
        <h3>Database</h3>
        Mr dan informasi bahan
        </div>
        """,unsafe_allow_html=True)

        if st.button("Buka Database"):
            st.session_state.page="Database Bahan"
            st.rerun()

# ==================================================
# PEMBUATAN LARUTAN
# ==================================================

elif menu=="Pembuatan Larutan":

    if st.button("←",key="back_larutan"):
        st.session_state.page="Home"
        st.rerun()

    st.header("Kalkulator Larutan")

    menu2=st.radio(
    "Pilih Menu",
    [
    "Menentukan Massa",
    "Pengenceran"
    ]
    )

    if menu2=="Menentukan Massa":

        sub=st.selectbox(
        "Jenis",
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

    if C1==0:

        st.error(
        "Konsentrasi awal tidak boleh 0"
        )

    else:

        V1=(C2*V2)/C1

        st.success(
        f"Volume stok = {V1:.2f} mL"
        )
# ==================================================
# KALKULATOR PH
# ==================================================

elif menu=="Kalkulator pH":

    if st.button("←",key="back_ph"):
        st.session_state.page="Home"
        st.rerun()

    st.header("Kalkulator pH")

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
    "Pilih senyawa",
    list(data_ph.keys())
    )

    info=data_ph[senyawa]

    st.info(
    f"Jenis: {info['jenis']}"
    )

    konsentrasi=st.number_input(
    "Konsentrasi (M)",
    value=0.01
    )

    if st.button("Hitung pH"):

    if konsentrasi<=0:
        st.error("Konsentrasi harus lebih besar dari 0")

    else:

        if info["jenis"]=="Asam kuat":

            H=konsentrasi*info["valensi"]
            ph=-math.log10(H)

        elif info["jenis"]=="Basa kuat":

            OH=konsentrasi*info["valensi"]

            pOH=-math.log10(OH)
            ph=14-pOH

        elif info["jenis"]=="Asam lemah":

            H=math.sqrt(
            info["Ka"]*
            konsentrasi*
            info["valensi"]
            )

            ph=-math.log10(H)

        else:

            OH=math.sqrt(
            info["Kb"]*
            konsentrasi*
            info["valensi"]
            )

            pOH=-math.log10(OH)
            ph=14-pOH

        st.metric(
        "Nilai pH",
        f"{ph:.2f}"
        )

        st.info(
        f"Sifat : {info['jenis']}"
        )

# ==================================================
# DATABASE
# ==================================================

elif menu=="Database Bahan":

    if st.button("←",key="back_db"):
        st.session_state.page="Home"
        st.rerun()

    st.header("Database Bahan")

    data={

"HCl":{"Mr":36.46,"Bahaya":"Korosif"},
"H₂SO₄":{"Mr":98.07,"Bahaya":"Korosif kuat"},
"HNO₃":{"Mr":63.01,"Bahaya":"Oksidator"},
"H₃PO₄":{"Mr":98.00,"Bahaya":"Iritasi"},
"NaOH":{"Mr":40.00,"Bahaya":"Korosif"},
"KOH":{"Mr":56.11,"Bahaya":"Korosif"},
"NH₃":{"Mr":17.03,"Bahaya":"Iritasi"},
"NH₄OH":{"Mr":35.04,"Bahaya":"Iritasi"},
"NaCl":{"Mr":58.44,"Bahaya":"Rendah"},
"KCl":{"Mr":74.55,"Bahaya":"Rendah"},
"KMnO₄":{"Mr":158.03,"Bahaya":"Oksidator"},
"K₂Cr₂O₇":{"Mr":294.18,"Bahaya":"Toksik"},
"AgNO₃":{"Mr":169.87,"Bahaya":"Oksidator"},
"CuSO₄":{"Mr":159.61,"Bahaya":"Bahaya lingkungan"},
"FeCl₃":{"Mr":162.20,"Bahaya":"Iritasi"},
"FeSO₄":{"Mr":151.91,"Bahaya":"Iritasi"},
"ZnSO₄":{"Mr":161.44,"Bahaya":"Bahaya lingkungan"},
"MgSO₄":{"Mr":120.36,"Bahaya":"Rendah"},
"CaCO₃":{"Mr":100.09,"Bahaya":"Rendah"},
"Na₂CO₃":{"Mr":105.99,"Bahaya":"Iritasi"},
"NaHCO₃":{"Mr":84.01,"Bahaya":"Rendah"},
"CH₃COOH":{"Mr":60.05,"Bahaya":"Korosif"},
"C₂H₅OH":{"Mr":46.07,"Bahaya":"Mudah terbakar"},
"CH₃OH":{"Mr":32.04,"Bahaya":"Toksik"},
"C₃H₆O":{"Mr":58.08,"Bahaya":"Mudah terbakar"},
"C₆H₆":{"Mr":78.11,"Bahaya":"Karsinogenik"},
"C₇H₈":{"Mr":92.14,"Bahaya":"Mudah terbakar"},
"C₆H₁₂O₆":{"Mr":180.16,"Bahaya":"Aman"},
"H₂O":{"Mr":18.02,"Bahaya":"Aman"},
"Na₂SO₄":{"Mr":142.04,"Bahaya":"Rendah"},
"KNO₃":{"Mr":101.10,"Bahaya":"Oksidator"},
"Pb(NO₃)₂":{"Mr":331.21,"Bahaya":"Toksik"},
"HgCl₂":{"Mr":271.50,"Bahaya":"Sangat toksik"},
"BaCl₂":{"Mr":208.23,"Bahaya":"Toksik"},
"AlCl₃":{"Mr":133.34,"Bahaya":"Korosif"},
"KI":{"Mr":166.00,"Bahaya":"Rendah"},
"NaI":{"Mr":149.89,"Bahaya":"Rendah"},
"CuCl₂":{"Mr":134.45,"Bahaya":"Bahaya lingkungan"},
"MnSO₄":{"Mr":151.00,"Bahaya":"Iritasi"},
"CdCl₂":{"Mr":183.32,"Bahaya":"Toksik"}

}

    cari=st.text_input(
    "Cari bahan"
    )

    if cari:
        hasil=[x for x in data if cari.lower() in x.lower()]
    else:
        hasil=list(data.keys())

    pilih=st.selectbox(
    "Pilih bahan",
    hasil
    )

    x=data[pilih]

    st.write(f"Rumus : {pilih}")
    st.write(f"Mr : {x['Mr']} g/mol")
    st.warning(f"Bahaya : {x['Bahaya']}")
