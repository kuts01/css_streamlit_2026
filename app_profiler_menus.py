import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="Kutloano Sikosana | MSc Physics Profile",
    layout="wide"
)

# ---------------- Sidebar Navigation ----------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    [
        "Academic Profile",
        "Research & Interests",
        "Publications",
        "Computational & STEM Portfolio",
        "Contact"
    ],
)

# ---------------- Cached Data ----------------
@st.cache_data
def load_physics_data():
    return pd.DataFrame({
        "Experiment": [
            "Alpha Decay",
            "Beta Decay",
            "Gamma Spectroscopy",
            "Ion Cluster Simulation",
            "Energy Minimisation (GA)"
        ],
        "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
        "Date": pd.date_range(start="2024-01-01", periods=5),
    })

physics_data = load_physics_data()

# ---------------- Academic Profile ----------------
if menu == "Academic Profile":
    st.title("Academic Profile")

    st.subheader("Personal Information")
    st.write("**Name:** Kutloano Sikosana")
    st.write("**Field:** Physics and Mathematics")
    st.write("**Degree:** BSc Physics and Mathematics")
    st.write("**Institution:** University of Pretoria")
    st.write("**Current Goal:** MSc in Physics")

    st.markdown("---")

    st.subheader("Academic Summary")
    st.write(
        """
        Physics Master’s student at the University of Pretoria | NRF-funded researcher in renewable energy.

        I hold a BSc in Physics and Mathematics and an Honours degree in Physics from UP. My research experience 
        focuses on polymer (organic) solar cells, combining experimental work and simulation-based modelling to improve 
        device efficiency and stability.

        Driven by curiosity and problem-solving, I am passionate about advancing clean energy 
        technologies and contributing to impactful scientific innovation.
        """
    )

    st.markdown("---")

    st.subheader("Teaching & Academic Support")
    st.write(
        """
        • Tutor for Computational Physics  
        • Mentor  
        • Experience explaining complex physical concepts clearly and rigorously  
        """
    )

# ---------------- Research & Interests ----------------
elif menu == "Research & Interests":
    st.title("Research & Academic Interests")

    st.subheader("Primary Interests")
    st.write(
        """
        • Renewable Energy (Organic Solar Cells) 
        • Theoretical Physics
        • Computational Physics    
        • Numerical Methods and Simulations  
        """
    )

    st.subheader("Research Experience")
    st.write(
        """
        • K.P.A. Sikosana, M.Y. Rasool. 2024. “Tiny Metals: A Comprehensive Electron Microscopy Review
        into the Synthesis and Characterisation of Multi-element Metallic Nanoparticles.” Department
        of Physics, University of Pretoria.
        ● K.P.A. Sikosana, M.M. Diale, T.E. Seimela, M.S.G. Hamed. 2024. “Investigating a Mn:Ni:Ce Metallic 
        Nanocomposite-Enhanced Bulk Heterojunction Inverted Organic Solar Cell Device.” Department of 
        Physics, University of Pretoria.
        """
    )

    st.subheader("Future MSc Focus")
    st.write(
        """
        For my MSc, I aim to deepen my theoretical foundation while developing robust
        computational tools for solving complex physical systems, particularly in
        statistical and condensed matter physics.
        """
    )

# ---------------- Publications ----------------
elif menu == "Publications":
    st.title("Publications & Academic Output")

    st.write(
        """
        Upload a CSV file containing publications, conference abstracts,
        posters, or preprints. This section is structured to mirror
        academic application requirements.

        • K.P.A. Sikosana, M.Y. Rasool. 2024. “Tiny Metals: A Comprehensive Electron Microscopy Review
        into the Synthesis and Characterisation of Multi-element Metallic Nanoparticles.” Department
        of Physics, University of Pretoria.
        ● K.P.A. Sikosana, M.M. Diale, T.E. Seimela, M.S.G. Hamed. 2024. “Investigating a Mn:Ni:Ce Metallic 
        Nanocomposite-Enhanced Bulk Heterojunction Inverted Organic Solar Cell Device.” Department of 
        Physics, University of Pretoria.
        """
    )

    uploaded_file = st.file_uploader(
        "Upload Publications (CSV)",
        type="csv"
    )

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        st.markdown("---")

        keyword = st.text_input("Filter by keyword (title, journal, year, authors)")

        if keyword:
            mask = publications.astype(str).apply(
                lambda col: col.str.lower().str.contains(keyword.lower())
            )
            filtered = publications[mask.any(axis=1)]
            st.subheader(f"Filtered Results for '{keyword}'")
            st.dataframe(filtered)

        if "Year" in publications.columns:
            st.subheader("Publication Timeline")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)

# ---------------- Computational & STEM Portfolio ----------------
elif menu == "Computational & STEM Portfolio":
    st.title("Computational & STEM Portfolio")

    st.write(
        """
        This section highlights my ability to work with scientific data,
        simulations, and computational analysis.
        """
    )

    st.subheader("Physics Simulation Data")
    st.dataframe(physics_data)

    energy_range = st.slider(
        "Filter by Energy (MeV)",
        0.0, 10.0,
        (0.0, 10.0)
    )

    filtered_physics = physics_data[
        physics_data["Energy (MeV)"].between(*energy_range)
    ]

    st.subheader("Filtered Results")
    st.dataframe(filtered_physics)

    st.subheader("Energy vs Time")
    st.line_chart(
        filtered_physics.set_index("Date")["Energy (MeV)"]
    )

    st.markdown("---")

    st.subheader("Technical Skills")
    st.write(
        """
        • Python (NumPy, Pandas, Matplotlib, Streamlit)  
        • Scientific Computing and Numerical Analysis  
        • Genetic Algorithms and Optimisation  
        • Data Analysis and Visualisation  
        • Linux-based computational environments  
        """
    )

# ---------------- Contact ----------------
elif menu == "Contact":
    st.title("Contact Information")

    st.write("**Email:** kutloanosikosana@gmail.com")
    st.write("LinkedIn: www.linkedin.com/in/kutloano-sikosana-5025a2283")
    st.write("**Field:** Physics (MSc Applicant)")
    st.write(
        """
        I am open to research opportunities, academic collaborations,
        and postgraduate study discussions.
        """
    )



