import streamlit as st
import pandas as pd
import numpy as np
from waiste.layout_params import background_image, title, title1, title2, title3, subtitle1, subtitle2, subtitle3, paper_bin, cardboard_bin, metal_bin, plastic_bin, glass_bin, organic_bin, electronics_bin, bricks_bin, telgopor_bin, non_recyclable_bin, hazardous_bin, clothes_bin, paper_title, cardboard_title, metal_title, plastic_title, glass_title, organic_title, electronics_title, bricks_title, telgopor_title, non_recyclable_title, hazardous_title, clothes_title, available_categories, find_location

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
        "https://cdn.pixabay.com/photo/2016/01/03/00/43/upload-1118929_1280.png"
    )

with col2:
    st.markdown(title2, unsafe_allow_html=True)
    st.markdown(subtitle2, unsafe_allow_html=True)
    st.image(
        "https://cdn.pixabay.com/photo/2012/04/14/14/42/man-34164_1280.png")

with col3:
    st.markdown(title3, unsafe_allow_html=True)
    st.markdown(subtitle3, unsafe_allow_html=True)
    st.image(
        "https://cdn.pixabay.com/photo/2016/01/10/22/23/location-1132648_1280.png"
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
col4, col5 = st.columns(2)
with col4:
    name = st.text_input('Name', '')

with col5:
    address = st.text_input('Address', '')

# User uploads image
with st.expander("Upload your waste image..."):
    uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'])

# Acá va la predicción
category = 'Metal'

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(available_categories, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col6, col7, col8, col9, col10, col11 = st.columns(6)
with col6:
    st.markdown(paper_bin, unsafe_allow_html=True)
    st.markdown(paper_title, unsafe_allow_html=True)

with col7:
    st.markdown(cardboard_bin, unsafe_allow_html=True)
    st.markdown(cardboard_title, unsafe_allow_html=True)

with col8:
    st.markdown(metal_bin, unsafe_allow_html=True)
    st.markdown(metal_title, unsafe_allow_html=True)

with col9:
    st.markdown(plastic_bin, unsafe_allow_html=True)
    st.markdown(plastic_title, unsafe_allow_html=True)

with col10:
    st.markdown(glass_bin, unsafe_allow_html=True)
    st.markdown(glass_title, unsafe_allow_html=True)

with col11:
    st.markdown(organic_bin, unsafe_allow_html=True)
    st.markdown(organic_title, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
col12, col13, col14, col15, col16, col17 = st.columns(6)
with col12:
    st.markdown(electronics_bin, unsafe_allow_html=True)
    st.markdown(electronics_title, unsafe_allow_html=True)

with col13:
    st.markdown(bricks_bin, unsafe_allow_html=True)
    st.markdown(bricks_title, unsafe_allow_html=True)

with col14:
    st.markdown(telgopor_bin, unsafe_allow_html=True)
    st.markdown(telgopor_title, unsafe_allow_html=True)

with col15:
    st.markdown(hazardous_bin, unsafe_allow_html=True)
    st.markdown(hazardous_title, unsafe_allow_html=True)

with col16:
    st.markdown(clothes_bin, unsafe_allow_html=True)
    st.markdown(clothes_title, unsafe_allow_html=True)

with col17:
    st.markdown(non_recyclable_bin, unsafe_allow_html=True)
    st.markdown(non_recyclable_title, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Show map with locations
st.markdown(find_location, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


def get_map_data():
    data = pd.read_csv(
        "/Users/Nadia/code/nadiasalmen/waiste/raw_data/puntos-verdes_cleaned.csv",
        sep=",")
    data.rename(columns={'Lat': 'lon', 'Long': 'lat'}, inplace = True)
    df = pd.DataFrame(data[['lat', 'lon']])
    return df

df = get_map_data()
st.map(df)
