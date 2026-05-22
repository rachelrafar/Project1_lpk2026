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
border-radius:12px;
height:45px;
font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

# ==================================================
# DATA
# ==================================================

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

"CH3COOH":{"jenis":"Asam lemah","Ka":1.8e-5,"valensi":1},
"HF":{"jenis":"Asam lemah","Ka":6.8e-4,"valensi":1},
"HCOOH":{"jenis":"Asam lemah","Ka":1.8e-4,"valensi":1},
"H2CO3":{"jenis":"Asam lemah","Ka":4.3e-7,"valensi":2},

"NH4OH":{"jenis":"Basa lemah","Kb":1.8e-5,"valensi":1},
"NH3":{"jenis":"Basa lemah","Kb":1.8e-5,"valensi":1}
}

data_bahan={

"HCl":{"Mr":36.46,"Bahaya":"Korosif"},
"H2SO4":{"Mr":98.07,"Bahaya":"Korosif kuat"},
"NaOH":{"Mr":40.00,"Bahaya":"Korosif"},
"NH3":{"Mr":17.03,"Bahaya":"Iritasi"},
"CuSO4":{"Mr":159.61,"Bahaya":"Bahaya lingkungan"},
"Etanol":{"Mr":46.07,"Bahaya":"Mudah terbakar"},
"Metanol":{"Mr":32.04,"Bahaya":"Toksik"},
"H2O":{"Mr":18.02,"Bahaya":"Aman"},
"NaCl":{"Mr":58.44,"Bahaya":"Risiko rendah"}

}

# ==================================================
# MENU
# ==================================================

menu=st.sidebar.radio(
"Menu",
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
    <h1>ChemAssist</h1>
    <p>Laboratory Chemistry Assistant</p>
    </div>
    """,unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric("Database",len(data_bahan))

    with c2:
        st.metric("Senyawa pH",len(data_ph))

    with c3:
        st.metric("Versi","3.0")

# ==================================================
# PEMBUATAN LARUTAN
# ==================================================

elif menu=="Pembuatan Larutan":

    st.header("Kalkulator Larutan")

    menu2=st.radio(
    "Pilih",
    ["Menentukan Massa","Pengenceran"]
    )

    if menu2=="Menentukan Massa":

        jenis=st.selectbox(
        "Jenis",
        ["Molaritas","Normalitas","ppm"]
        )

        if jenis=="Molaritas":

            Mr=st.number_input(
            "Mr",
            min_value=0.01,
            value=40.0
            )

            M=st.number_input(
            "Molaritas",
            min_value=0.0,
            value=0.1
            )

            V=st.number_input(
            "Volume (mL)",
            min_value=1.0,
            value=100.0
            )

            if st.button("Hitung Massa"):

                massa=(M*Mr*V)/1000

                st.success(
                f"Massa = {massa:.4f} gram"
                )

        elif jenis=="Normalitas":

            BE=st.number_input(
            "Berat ekivalen",
            min_value=0.01,
            value=40.0
            )

            N=st.number_input(
            "Normalitas",
            min_value=0.0,
            value=0.1
            )

            V=st.number_input(
            "Volume (mL)",
            min_value=1.0,
            value=100.0,
            key="Vnormal"
            )

            if st.button("Hitung Normalitas"):

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

            if st.button("Hitung ppm"):

                massa=ppm*V

                st.success(
                f"Massa = {massa:.2f} mg"
                )

    else:

        C1=st.number_input(
        "Konsentrasi awal",
        min_value=0.01,
        value=10.0
        )

        C2=st.number_input(
        "Konsentrasi akhir",
        min_value=0.01,
        value=1.0
        )

        V2=st.number_input(
        "Volume akhir",
        min_value=1.0,
        value=100.0
        )

        if st.button("Hitung Pengenceran"):

            V1=(C2*V2)/C1

            st.success(
            f"Volume stok = {V1:.2f} mL"
            )

# ==================================================
# KALKULATOR PH
# ==================================================

elif menu=="Kalkulator pH":

    st.header("Kalkulator pH")

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
    min_value=0.000001,
    value=0.01
    )

    if st.button("Hitung pH"):

        jenis=info["jenis"]

        if jenis=="Asam kuat":

            H=konsentrasi*info["valensi"]
            ph=-math.log10(H)

        elif jenis=="Basa kuat":

            OH=konsentrasi*info["valensi"]
            pOH=-math.log10(OH)
            ph=14-pOH

        elif jenis=="Asam lemah":

            H=math.sqrt(
            info["Ka"]*konsentrasi
            )

            ph=-math.log10(H)

        else:

            OH=math.sqrt(
            info["Kb"]*konsentrasi
            )

            pOH=-math.log10(OH)

            ph=14-pOH

        st.metric(
        "Nilai pH",
        f"{ph:.2f}"
        )

# ==================================================
# DATABASE
# ==================================================

elif menu=="Database Bahan":

    st.header("Database Bahan")

    cari=st.text_input(
    "Cari bahan"
    )

    if cari:
        hasil=[
        x for x in data_bahan
        if cari.lower() in x.lower()
        ]
    else:
        hasil=list(data_bahan.keys())

    pilih=st.selectbox(
    "Pilih bahan",
    hasil
    )

    x=data_bahan[pilih]

    st.write(f"Rumus : {pilih}")
    st.write(f"Mr : {x['Mr']} g/mol")
    st.warning(f"Bahaya : {x['Bahaya']}")
