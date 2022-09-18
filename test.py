import streamlit as st 
from PIL import Image as PILImage
import rembg as rm


uploaded_files=st.file_uploader("Upload a file", type=["png", "jpg", "jpeg"], accept_multiple_files=True) 
for file in uploaded_files:
    img1 = PILImage.open(file)
    st.image(file)
    img_rem=rm.remove(img1)
    st.image(img_rem,width=1000)