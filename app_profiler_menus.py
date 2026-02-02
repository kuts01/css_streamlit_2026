import streamlit as st
import pandas as pd
import numpy as np
import base64

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
        • *Mn:Ni:Ce Nanocomposite-Enhanced Bulk Heterojunction Inverted Organic Solar Cells*  
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
        **Tiny Metals: A Comprehensive Electron Microscopy Review into the Synthesis and
        Characterisation of Multi-element Metallic Nanoparticles**

        **Author:** Kutloano Sikosana  
        **Supervisors:** K.P.A. Sikosana, M.Y. Rasool  
        **Institution:** University of Pretoria  
        **Year:** 2025  
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

    st.markdown("---")

    st.subheader("Preview")

    # Embed PDF
    pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
    pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{pdf_base64}"
            width="100%"
            height="800"
            type="application/pdf">
        </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)

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








