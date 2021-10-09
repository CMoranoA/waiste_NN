import streamlit as st
import pandas as pd
import numpy as np
from waiste.layout_params import background_image, title, title1, title2, title3, subtitle1, subtitle2, subtitle3

# Site configuration
st.set_page_config(page_title="wAIste",
                   page_icon="♻️",
                   layout="centered",
                   initial_sidebar_state="collapsed")

# Main section
st.markdown(title, unsafe_allow_html=True)
st.markdown(f'<style>{background_image}</style>', unsafe_allow_html=True)

# How it works section
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(title1, unsafe_allow_html=True)
    st.markdown(subtitle1, unsafe_allow_html=True)
    st.image(
      "https://cdn.pixabay.com/photo/2017/07/11/10/43/upload-2493114_1280.png"
    )

with col2:
    st.markdown(title2, unsafe_allow_html=True)
    st.markdown(subtitle2, unsafe_allow_html=True)
    st.image(
        "https://cdn.pixabay.com/photo/2016/10/10/01/49/delete-1727486_1280.png"
    )

with col3:
    st.markdown(title3, unsafe_allow_html=True)
    st.markdown(subtitle3, unsafe_allow_html=True)
    st.image(
        "https://cdn.pixabay.com/photo/2016/10/08/18/35/the-location-of-the-1724293_1280.png"
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# User inputs
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
name = st.text_input('Name', '')
address = st.text_input('Address', '')
st.subheader('Upload a photo')

# User uploads image
with st.expander("Upload your waste image..."):
    uploaded_file = st.file_uploader("Choose an image...",
                                     type=['png', 'jpg', 'jpeg'])

# Acá va la predicción


# Show map with locations
def get_map_data():

    data = pd.read_csv(
        "/Users/Nadia/code/nadiasalmen/waiste/raw_data/puntos-verdes_cleaned.csv",
        sep=",")
    data.rename(columns={'Lat': 'lon', 'Long': 'lat'}, inplace = True)
    df = pd.DataFrame(data[['lat', 'lon']])
    return df

df = get_map_data()
st.map(df)
