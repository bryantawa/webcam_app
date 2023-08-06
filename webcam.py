import streamlit as st
from PIL import Image

st.subheader("Colour-to-Grayscale Image Converter")
st.write("<b>Upload Image</b>", unsafe_allow_html=True)

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # create a Pillow image instance
    img = Image.open(camera_image)

    # Convert Pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the browser
    st.image(gray_img)

if uploaded_image:
    # create a Pillow image instance
    img = Image.open(uploaded_image)

    # Convert Pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the browser
    st.image(gray_img)