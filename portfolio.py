import streamlit as st

st.set_page_config(page_title="Benson Majawa Portfolio", layout="centered")

st.title("Benson Majawa")
st.subheader("BSc Applied Statistics - First Class")
st.write("Welcome to my professional portfolio. Use the buttons below to explore my background.")

page = st.radio("Navigate", ["Home", "Projects", "Skills", "Contact"])

if page == "Home":
    st.write("This is the home section with a short intro.")
elif page == "Projects":
    st.write("Here are some of my projects...")
elif page == "Skills":
    st.write("Here are my skills...")
elif page == "Contact":
    st.write("Contact me at: benson@example.com")
