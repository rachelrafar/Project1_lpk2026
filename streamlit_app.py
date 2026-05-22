import streamlit as st
import math

# ================= CONFIG =================

st.set_page_config(
    page_title="ChemAssist",
    page_icon="🧪",
    layout="centered"
)

# ================= CSS =================

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
}

.stButton>button{
    width:100%;
    border-radius:12px;
    height:50px;
}

.info-box{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,.1);
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

# ================= SESSION =================

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ================= DATA pH =================

data_ph = {

    "HCl":{
        "nama":"Asam Klorida",
        "jenis":"Asam kuat",
        "valensi":1
    },

    "H2SO4":{
        "nama":"Asam Sulfat",
        "jenis":"Asam kuat",
        "valensi":2
    },

    "HNO3":{
        "nama":"Asam Nitrat",
        "jenis":"Asam kuat",
        "valensi":1
    },

    "NaOH":{
        "nama":"Natrium Hidroksida",
        "jenis":"Basa kuat",
        "valensi":1
    },

    "KOH":{
        "nama":"Kalium Hidroksida",
        "jenis":"Basa kuat",
        "valensi":1
    },

    "Ba(OH)2":{
        "nama":"Barium Hidroksida",
        "jenis":"Basa kuat",
        "valensi":2
    },

    "CH3COOH":{
        "nama":"Asam Asetat",
        "jenis":"Asam lemah",
        "Ka":1.8e-5
    },

    "HF":{
        "nama":"Asam Fluorida",
        "jenis":"Asam lemah",
        "Ka":6.8e-4
    },

    "NH3":{
        "nama":"Amonia",
        "jenis":"Basa lemah",
        "Kb":1.8e-5
    },

    "NH4OH":{
        "nama":"Amonium Hidroksida",
        "jenis":"Basa lemah",
        "Kb":1.8e-5
    }
}

# ================= DATABASE =================

db = {

    "HCl":{
        "nama":"Asam Klorida",
        "jenis":"Asam kuat",
        "Mr":36.46,
        "bahaya":"Korosif, menyebabkan luka bakar kulit dan iritasi pernapasan"
    },

    "H2SO4":{
        "nama":"Asam Sulfat",
        "jenis":"Asam kuat",
        "Mr":98.08,
        "bahaya":"Sangat korosif dan bereaksi hebat dengan air"
    },

    "HNO3":{
        "nama":"Asam Nitrat",
        "jenis":"Asam kuat",
        "Mr":63.01,
        "bahaya":"Oksidator kuat dan korosif"
    },

    "CH3COOH":{
        "nama":"Asam Asetat",
        "jenis":"Asam lemah",
        "Mr":60.05,
        "bahaya":"Iritasi kulit dan mata"
    },

    "HF":{
        "nama":"Asam Fluorida",
        "jenis":"Asam lemah",
        "Mr":20.01,
        "bahaya":"Sangat beracun dan korosif"
    },

    "NaOH":{
        "nama":"Natrium Hidroksida",
        "jenis":"Basa kuat",
        "Mr":40.00,
        "bahaya":"Korosif dan menyebabkan luka bakar"
    },

    "KOH":{
        "nama":"Kalium Hidroksida",
        "jenis":"Basa kuat",
        "Mr":56.11,
        "bahaya":"Korosif terhadap kulit dan mata"
    },

    "Ca(OH)2":{
        "nama":"Kalsium Hidroksida",
        "jenis":"Basa kuat",
        "Mr":74.09,
        "bahaya":"Iritasi saluran napas"
    },

    "NH3":{
        "nama":"Amonia",
        "jenis":"Basa lemah",
        "Mr":17.03,
        "bahaya":"Gas beracun dan iritasi"
    },

    "NH4OH":{
        "nama":"Amonium Hidroksida",
        "jenis":"Basa lemah",
        "Mr":35.05,
        "bahaya":"Iritasi kulit dan paru-paru"
    },

    "NaCl":{
        "nama":"Natrium Klorida",
        "jenis":"Garam",
        "Mr":58.44,
        "bahaya":"Relatif aman"
    },

    "KCl":{
        "nama":"Kalium Klorida",
        "jenis":"Garam",
        "Mr":74.55,
        "bahaya":"Iritasi ringan"
    },

    "AgNO3":{
        "nama":"Perak Nitrat",
        "jenis":"Garam",
        "Mr":169.87,
        "bahaya":"Oksidator dan menyebabkan noda kulit"
    },

    "CuSO4":{
        "nama":"Tembaga(II) Sulfat",
        "jenis":"Garam",
        "Mr":159.61,
        "bahaya":"Beracun bagi organisme air"
    },

    "FeCl3":{
        "nama":"Besi(III) Klorida",
        "jenis":"Garam",
        "Mr":162.20,
        "bahaya":"Korosif dan iritasi"
    },

    "MgSO4":{
        "nama":"Magnesium Sulfat",
        "jenis":"Garam",
        "Mr":120.37,
        "bahaya":"Iritasi ringan"
    },

    "CaCO3":{
        "nama":"Kalsium Karbonat",
        "jenis":"Garam",
        "Mr":100.09,
        "bahaya":"Debu mengiritasi saluran napas"
    },

    "Na2CO3":{
        "nama":"Natrium Karbonat",
        "jenis":"Garam basa",
        "Mr":105.99,
        "bahaya":"Iritasi mata dan kulit"
    },

    "NaHCO3":{
        "nama":"Natrium Bikarbonat",
        "jenis":"Garam basa",
        "Mr":84.01,
        "bahaya":"Relatif aman"
    },

    "C2H5OH":{
        "nama":"Etanol",
        "jenis":"Alkohol",
        "Mr":46.07,
        "bahaya":"Mudah terbakar"
    },

    "CH3OH":{
        "nama":"Metanol",
        "jenis":"Alkohol",
        "Mr":32.04,
        "bahaya":"Beracun dan mudah terbakar"
    },

    "Acetone":{
        "nama":"Aseton",
        "jenis":"Keton",
        "Mr":58.08,
        "bahaya":"Sangat mudah terbakar"
    },

    "Benzene":{
        "nama":"Benzena",
        "jenis":"Hidrokarbon aromatik",
        "Mr":78.11,
        "bahaya":"Karsinogen dan mudah terbakar"
    },

    "Toluene":{
        "nama":"Toluena",
        "jenis":"Hidrokarbon aromatik",
        "Mr":92.14,
        "bahaya":"Beracun jika terhirup"
    },

    "Glucose":{
        "nama":"Glukosa",
        "jenis":"Karbohidrat",
        "Mr":180.16,
        "bahaya":"Relatif aman"
    }
}

# ================= SIDEBAR =================

menu = st.sidebar.radio(
    "ChemAssist",
    ["Home", "Larutan", "pH", "Database"]
)

# ================= HOME =================

if menu == "Home":

    st.markdown("""
    <div class='header'>
    <h1>🧪 ChemAssist</h1>
    <p>Laboratory Chemistry Assistant</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    c1.metric("📚 Database", f"{len(db)}")
    c2.metric("⚗️ Senyawa", f"{len(data_ph)}")
    c3.metric("Version", "6.0")

# ================= LARUTAN =================

elif menu == "Larutan":

    st.title("💧 Perhitungan Larutan")

    mode = st.radio(
        "Pilih Perhitungan",
        ["Menentukan Massa", "Pengenceran"]
    )

    # ---------- MASSA ----------

    if mode == "Menentukan Massa":

        jenis = st.selectbox(
            "Jenis Perhitungan",
            ["Molaritas", "Normalitas", "ppm"]
        )

        # MOLARITAS
        if jenis == "Molaritas":

            Mr = st.number_input("Mr", 40.0)
            M = st.number_input("Molaritas (M)", 0.1)
            V = st.number_input("Volume (mL)", 100.0)

            if st.button("Hitung Massa"):

                massa = (Mr * M * V) / 1000

                st.success(f"Massa yang dibutuhkan = {massa:.4f} gram")

        # NORMALITAS
        elif jenis == "Normalitas":

            BE = st.number_input("Berat ekuivalen", 40.0)
            N = st.number_input("Normalitas", 0.1)
            V = st.number_input("Volume (mL)", 100.0)

            if st.button("Hitung Massa"):

                massa = (BE * N * V) / 1000

                st.success(f"Massa yang dibutuhkan = {massa:.4f} gram")

        # PPM
        else:

            ppm = st.number_input("ppm", 100.0)
            V = st.number_input("Volume (L)", 1.0)

            if st.button("Hitung Massa"):

                massa = ppm * V

                st.success(f"Massa = {massa:.2f} mg")

    # ---------- PENGENCERAN ----------

    else:

        C1 = st.number_input("Konsentrasi awal", 10.0)
        C2 = st.number_input("Konsentrasi akhir", 1.0)
        V2 = st.number_input("Volume akhir (mL)", 100.0)

        if st.button("Hitung Pengenceran"):

            V1 = (C2 * V2) / C1

            st.success(f"Ambil {V1:.2f} mL larutan stok")

            st.info(
                f"Pipet {V1:.2f} mL lalu tambahkan pelarut hingga {V2} mL"
            )

# ================= pH =================

elif menu == "pH":

    st.title("⚗️ Kalkulator pH")

    senyawa = st.selectbox(
        "Pilih Senyawa",
        list(data_ph.keys())
    )

    info = data_ph[senyawa]

    st.info(f"{info['nama']} ({info['jenis']})")

    C = st.number_input("Konsentrasi (M)", 0.01)

    if st.button("Hitung pH"):

        # ASAM KUAT
        if info["jenis"] == "Asam kuat":

            ph = -math.log10(C * info["valensi"])

        # BASA KUAT
        elif info["jenis"] == "Basa kuat":

            poh = -math.log10(C * info["valensi"])
            ph = 14 - poh

        # ASAM LEMAH
        elif info["jenis"] == "Asam lemah":

            H = math.sqrt(info["Ka"] * C)
            ph = -math.log10(H)

        # BASA LEMAH
        else:

            OH = math.sqrt(info["Kb"] * C)
            poh = -math.log10(OH)
            ph = 14 - poh

        st.metric("Nilai pH", f"{ph:.2f}")

# ================= DATABASE =================

elif menu == "Database":

    st.title("📚 Database Senyawa Kimia")

    cari = st.text_input("Cari bahan kimia")

    hasil = [
        x for x in db
        if cari.lower() in x.lower()
    ] if cari else list(db.keys())

    pilih = st.selectbox("Pilih Bahan", hasil)

    st.markdown("<div class='info-box'>", unsafe_allow_html=True)

    st.write("### Informasi Senyawa")

    st.write("Rumus Kimia :", pilih)

    st.write("Nama Senyawa :", db[pilih]["nama"])

    st.write("Jenis :", db[pilih]["jenis"])

    st.write("Mr :", db[pilih]["Mr"])

    st.error("Bahaya : " + db[pilih]["bahaya"])

    st.markdown("</div>", unsafe_allow_html=True)
