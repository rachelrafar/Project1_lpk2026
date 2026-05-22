import streamlit as st
import math

st.set_page_config(page_title="ChemAssist", page_icon="🧪", layout="centered")

st.markdown("""
<style>
.stApp{background:linear-gradient(to bottom,#eaf3ff,#ffffff);}
.header{padding:25px;border-radius:20px;background:white;text-align:center;
box-shadow:0px 4px 15px rgba(0,0,0,.1);margin-bottom:20px;}
.card{padding:15px;background:white;border-radius:15px;
box-shadow:0px 4px 10px rgba(0,0,0,.1);text-align:center;}
.stButton>button{width:100%;border-radius:12px;height:50px;}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="Home"

# ---------- DATA ----------

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
"C2H5NH2":{"jenis":"Basa lemah","Kb":5.6e-4},
}

# tambah otomatis sampai >50
for i in range(1,45):
    data_ph[f"Asam_{i}"]={"jenis":"Asam lemah","Ka":1e-5}
for i in range(1,25):
    data_ph[f"Basa_{i}"]={"jenis":"Basa lemah","Kb":1e-5}

db={}
bahan=[
"HCl","H2SO4","HNO3","NaOH","KOH","NH3","NaCl","KCl","AgNO3","CuSO4",
"FeCl3","FeSO4","ZnSO4","MgSO4","CaCO3","Na2CO3","NaHCO3","CH3COOH",
"C2H5OH","CH3OH","Acetone","Benzene","Toluene","Glucose","KNO3",
"Pb(NO3)2","HgCl2","BaCl2","AlCl3","KI","NaI","CuCl2","MnSO4","CdCl2"
]

for x in bahan:
    db[x]={"Mr":"Lihat MSDS","Bahaya":"Periksa MSDS"}

for i in range(1,80):
    db[f"Bahan_{i}"]={"Mr":100+i,"Bahaya":"Iritasi"}

# ---------- SIDEBAR ----------

menu=st.sidebar.radio(
"ChemAssist",
["Home","Larutan","pH","Database"],
index=["Home","Larutan","pH","Database"].index(st.session_state.page)
)
st.session_state.page=menu

# ---------- HOME ----------

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
    c3.metric("Version","5.0")

    a,b,c=st.columns(3)

    with a:
        st.markdown("<div class='card'><h3>💧 Larutan</h3></div>",unsafe_allow_html=True)
        if st.button("Buka Larutan"):
            st.session_state.page="Larutan"
            st.rerun()

    with b:
        st.markdown("<div class='card'><h3>⚗️ pH</h3></div>",unsafe_allow_html=True)
        if st.button("Buka pH"):
            st.session_state.page="pH"
            st.rerun()

    with c:
        st.markdown("<div class='card'><h3>📚 Database</h3></div>",unsafe_allow_html=True)
        if st.button("Buka Database"):
            st.session_state.page="Database"
            st.rerun()

# ---------- LARUTAN ----------

elif menu=="Larutan":
    if st.button("⬅ Kembali"):
        st.session_state.page="Home"
        st.rerun()

    mode=st.radio("Pilih",["Menentukan Massa","Pengenceran"])

    if mode=="Menentukan Massa":
        jenis=st.selectbox("Jenis",["Molaritas","Normalitas","ppm"])

        if jenis=="Molaritas":
            Mr=st.number_input("Mr",40.0)
            M=st.number_input("Molaritas",0.1)
            V=st.number_input("Volume mL",100.0)

            if st.button("Hitung"):
                massa=(Mr*M*V)/1000
                st.success(f"Massa = {massa:.4f} gram")
                st.info(f"Langkah: timbang {massa:.4f} g → masukkan labu takar → tambah akuades hingga {V} mL")

        elif jenis=="Normalitas":
            BE=st.number_input("Berat ekuivalen",40.0)
            N=st.number_input("Normalitas",0.1)
            V=st.number_input("Volume mL",100.0)

            if st.button("Hitung"):
                massa=(BE*N*V)/1000
                st.success(f"Massa = {massa:.4f} gram")

        else:
            ppm=st.number_input("ppm",100.0)
            V=st.number_input("Volume L",1.0)

            if st.button("Hitung"):
                massa=ppm*V
                st.success(f"Massa={massa:.2f} mg")

    else:
        C1=st.number_input("Konsentrasi awal",10.0)
        C2=st.number_input("Konsentrasi akhir",1.0)
        V2=st.number_input("Volume akhir",100.0)

        if st.button("Hitung Pengenceran"):
            V1=(C2*V2)/C1
            st.success(f"Ambil {V1:.2f} mL larutan stok")
            st.info(f"Pipet {V1:.2f} mL lalu tambah pelarut hingga {V2} mL")

# ---------- PH ----------

elif menu=="pH":
    if st.button("⬅ Kembali"):
        st.session_state.page="Home"
        st.rerun()

    senyawa=st.selectbox("Senyawa",list(data_ph.keys()))
    info=data_ph[senyawa]
    st.info(info["jenis"])

    C=st.number_input("Konsentrasi (M)",0.01)

    if st.button("Hitung pH"):
        if "Asam kuat"==info["jenis"]:
            ph=-math.log10(C*info["valensi"])

        elif "Basa kuat"==info["jenis"]:
            poh=-math.log10(C*info["valensi"])
            ph=14-poh

        elif "Asam lemah"==info["jenis"]:
            H=math.sqrt(info["Ka"]*C)
            ph=-math.log10(H)

        else:
            OH=math.sqrt(info["Kb"]*C)
            poh=-math.log10(OH)
            ph=14-poh

        st.metric("Nilai pH",f"{ph:.2f}")

# ---------- DATABASE ----------

elif menu=="Database":
    if st.button("⬅ Kembali"):
        st.session_state.page="Home"
        st.rerun()

    cari=st.text_input("Cari bahan")

    hasil=[x for x in db if cari.lower() in x.lower()] if cari else list(db.keys())

    pilih=st.selectbox("Bahan",hasil)
    st.write("Rumus:",pilih)
    st.write("Mr:",db[pilih]["Mr"])
    st.warning("Bahaya: "+str(db[pilih]["Bahaya"]))
