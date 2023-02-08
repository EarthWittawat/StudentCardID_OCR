from PIL import Image
import streamlit as st
import easyocr
from pathlib import Path
import pathlib

st.set_page_config(
    page_title="School election",
    layout="wide",
)

model = easyocr.Reader(['th'])


def ocr(image):
    getText = model.readtext(image)
    result = []
    name = getText[6][1].replace(' ', '')
    id = getText[8][1].replace('เลขประจำตัว', '')
    information = {
        "fullname": f'{name} {getText[7][1]}',
        "id": id.replace(' ', ''),
        "citizen_id": f'{getText[10][1]} {getText[11][1]}'
    }
    return information


with st.container():
    file_up = st.file_uploader("Upload an image", type="jpg")
    if file_up is not None:
        image = Image.open(file_up)
        st.image(image, caption='อัปโหลดบัตรนักเรียน',
                 width=300)
        st.write("")
        labels = ocr(image)
        st.write(labels)
