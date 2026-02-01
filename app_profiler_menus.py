
import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Kutloano Sikosana | MSc Physics Profile",
    layout="wide"
)

# -------------------------------------------------
# Academic styling (CV-like)
# -------------------------------------------------
st.markdown(
    """
    <style>
    h1, h2, h3 {
        color: #1E3A8A;
    }

    section[data-testid="stSidebar"] {
        background-color: #F7F9FB;
        border-right: 1px solid #D1D5DB;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    [
        "Academic Profile",
        "Research & Experience",
        "Publications",
        "Computational & STEM Portfolio",
        "Contact"
    ],
)

# -------------------------------------------------
# Cached STEM data
# -------------------------------------------------
@st.cache_data
def load_physics_data():
    return pd.DataFrame({
        "Study": [
            "Alpha Decay",
            "Gamma Spectroscopy",
            "Nanoparticle Microscopy",
            "Organic Solar Cell Modelling",
            "Genetic Algorithm Optimisation"
        ],
        "Energy / Metric": [4.2, 2.9, 3.4, 6.1, 7.1],
        "Date": pd.date_range(start="2024-01-01", periods=5),
    })

physics_data = load_physics_data()

# -------------------------------------------------
# Academic Profile
# -------------------------------------------------
if menu == "Academic Profile":
    st.title("Academic Profile")

    st.subheader("Personal Information")
    st.write("**Name:** Kutloano Sikosana")
    st.write("**Degree:** BSc Physics, BSc Physics Honours")
    st.write("**Institution:** University of Pretoria")
    st.write("**Current Status:** MSc Physics Candidate")
    st.write("**Email:** kutloanosikosana@gmail.com")

    st.markdown("---")

    st.subheader("Professional Profile")
    st.write(
        """
        Physics graduate with a strong background in experimental and computational physics,
        with research experience in organic photovoltaics and nanomaterials.
        Current work focuses on incorporating metallic nanoparticles into nanoscale
        bulk heterojunctions to improve polymer solar cell efficiency, combining laboratory
        experimentation with simulation-based modelling.

        Demonstrated strengths in scientific writing, microscopy and microanalysis,
        numerical methods, and technical communication, supported by tutoring,
        mentoring, and leadership experience.
        """
    )

# -------------------------------------------------
# Research & Experience
# -------------------------------------------------
elif menu == "Research & Experience":
    st.title("Research & Experience")

    st.subheader("Research Areas")
    st.write(
        """
        • Organic Photovoltaics  
        • Metallic Nanoparticles and Nanocomposites  
        • Computational Physics and Modelling  
        • Statistical Mechanics and Optimisation  
        """
    )

    st.subheader("Research Output")
    st.write(
        """
        • *Tiny Metals:* Electron microscopy review into the synthesis and characterisation
          of multi-element metallic nanoparticles  
        • *Mn:Ni:Ce Nanocomposite-Enhanced Bulk Heterojunction Inverted Organic Solar Cells*  
        """
    )

    st.subheader("Teaching & Academic Support")
    st.write(
        """
        • Computational Physics Tutor (PHY 255), University of Pretoria  
        • Physics Demonstrator (PHY 114M)  
        • Assisted students with debugging, numerical methods, and scientific reasoning  
        """
    )

# -------------------------------------------------
# Publications
# -------------------------------------------------
elif menu == "Publications":
    st.title("Publications")

    st.write(
        """
        Upload a CSV containing publications, manuscripts, posters,
        or conference contributions.
        """
    )

    uploaded_file = st.file_uploader(
        "Upload Publications (CSV)",
        type="csv"
    )

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        keyword = st.text_input("Filter by keyword")

        if keyword:
            mask = publications.astype(str).apply(
                lambda col: col.str.lower().str.contains(keyword.lower())
            )
            filtered = publications[mask.any(axis=1)]
            st.subheader(f"Results for '{keyword}'")
            st.dataframe(filtered)

        if "Year" in publications.columns:
            st.subheader("Publication Timeline")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)

# -------------------------------------------------
# Computational & STEM Portfolio
# -------------------------------------------------
elif menu == "Computational & STEM Portfolio":
    st.title("Computational & STEM Portfolio")

    st.write(
        """
        This section demonstrates my ability to analyse,
        model, and visualise scientific data.
        """
    )

    st.subheader("Physics and Modelling Data")
    st.dataframe(physics_data)

    energy_filter = st.slider(
        "Filter by Energy / Metric",
        0.0, 10.0,
        (0.0, 10.0)
    )

    filtered_data = physics_data[
        physics_data["Energy / Metric"].between(*energy_filter)
    ]

    st.subheader("Filtered Results")
    st.dataframe(filtered_data)

    st.subheader("Metric vs Time")
    st.line_chart(
        filtered_data.set_index("Date")["Energy / Metric"]
    )

    st.markdown("---")

    st.subheader("Technical Skills")
    st.write(
        """
        • Python (NumPy, Pandas, Matplotlib, Streamlit)  
        • Genetic Algorithms and Optimisation  
        • SEM and EDS Microscopy  
        • Thin-Film and Bulk Heterojunction Fabrication  
        • Numerical Analysis and Scientific Computing  
        """
    )

# -------------------------------------------------
# Contact
# -------------------------------------------------
elif menu == "Contact":
    st.title("Contact")

    st.write("**Email:** kutloanosikosana@gmail.com")
    st.write("**LinkedIn:** www.linkedin.com/in/kutloano-sikosana-5025a2283")

    st.write(
        """
        Open to postgraduate research opportunities,
        academic collaboration, and funded MSc projects.
        """
    )
