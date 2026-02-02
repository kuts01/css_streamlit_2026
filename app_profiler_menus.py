import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="Kutloano Sikosana | MSc Physics",
    layout="wide"
)

# ---------------- Sidebar Navigation ----------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    [
        "Academic Profile",
        "Research & Experience",
        "Publications",
        "Contact"
    ],
)

# ---------------- Academic Profile ----------------
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

        I have demonstrated strengths in scientific writing, microscopy and microanalysis,
        numerical methods, and technical communication, supported by tutoring,
        mentoring, and leadership experience.
        """
    )

# ---------------- Research & Interests ----------------
elif menu == "Research & Experience":
    st.title("Research & Experience")

    st.subheader("Research Areas")
    st.write(
        """
        • Organic Photovoltaics  
        • Metallic Nanoparticles and Nanocomposites  
        • Computational Physics and Modelling    
        """
    )

    st.subheader("Research Output")
    st.write(
        """
        • *Tiny Metals:* Electron microscopy review into the synthesis and characterisation
          of multi-element metallic nanoparticles  
        • *Investigating a Mn:Ni:Ce Metallic Nanocomposite-Enhanced Bulk Heterojunction Inverted Organic Solar Cell Device*  
        """
    )

    st.subheader("Teaching & Academic Support")
    st.write(
        """
        • Computational Physics Tutor (PHY 255), University of Pretoria  
        • Mentor (STARS Mentorship Programme), University of Pretoria  
        • Assisted students with debugging, numerical methods, and scientific reasoning  
        """
    )


# ---------------- Publications ----------------
elif menu == "Publications":
    st.title("Publications")

    st.subheader("Honours Research Papers")

    st.markdown(
        """
        **Investigating a Mn:Ni:Ce Metallic
        Nanocomposite-Enhanced Bulk Heterojunction
        Inverted Organic Solar Cell Device**

        **Author:** Kutloano Sikosana  
        **Supervisors:** M. Diale, T.E. Seimela, M.S.G. Hamed  
        **Institution:** University of Pretoria  
        **Year:** 2025 
        
        **Abstract:** This study investigates the incorporation of Mn:Ni:Ce trimetallic nanoparticles into the bulk
        heterojunction active layer of inverted organic solar cells based on a PCBM:PCDTBT blend.
        The nanoparticles were synthesised via a wet chemical process and characterised using SEM
        and EDS, revealing predominantly spherical particles with a strong cerium dominance,
        indicating incomplete trimetallic alloy formation. Devices fabricated with varying nanoparticle
        concentrations were evaluated using J-V measurements, quantum efficiency, UV-Vis
        absorption, and impedance spectroscopy. The optimal nanoparticle loading of 1 mg led to a
        power conversion efficiency of 6.63%, nearly tripling that of the pristine device, through
        enhanced fill factor, short-circuit current, and open-circuit voltage. Optical measurements
        showed broader spectral absorption and increased photon harvesting attributed to localised
        surface plasmon resonance effects. Impedance analysis confirmed improved and more
        uniform charge transport at optimal loading, while higher concentrations caused aggregation
        and recombination losses. These findings demonstrate that controlled nanoparticle integration
        enhances organic solar cell performance, with further research needed to optimise
        nnanoparticle composition and stability.
        """
    )

    st.markdown("---")

    # Load PDF
    pdf_path = "HonoursResearchProjectKutloanoSikosana20420961.pdf"

    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.download_button(
        label="Download Honours Paper (PDF)",
        data=pdf_bytes,
        file_name="Kutloano_Sikosana_Honours_Paper.pdf",
        mime="application/pdf",
    )

# ---------------- Contact ----------------

elif menu == "Contact":
    st.title("Contact Information")

    st.write("**Email:** kutloanosikosana@gmail.com")
    st.write("**LinkedIn:** www.linkedin.com/in/kutloano-sikosana-5025a2283")

    st.write(
        """
        Open to postgraduate research opportunities,
        academic collaboration, and funded MSc projects.
        """
    )













