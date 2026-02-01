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
    st.title("Publications & Academic Output")

    st.write(
        """
        Upload a CSV file containing publications, conference abstracts,
        posters, or preprints.
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






