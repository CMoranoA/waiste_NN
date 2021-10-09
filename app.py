import streamlit as st
import pandas as pd
import numpy as np
from waiste.layout_params import background_image, title

# Site configuration
st.set_page_config(page_title="wAIste",
                   page_icon="♻️",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.markdown(f'<style>{background_image}</style>', unsafe_allow_html=True)

# # Sidebar with project info
# about = st.sidebar.header('About')

# Main section
st.markdown(title, unsafe_allow_html=True)

'How it works section!'

# User inputs
name = st.text_input('Nombre:', '')
address = st.text_input('Address:', '')
st.subheader('Upload a photo')

# User uploads image
with st.expander("Upload your waste image..."):
    uploaded_file = st.file_uploader("Choose an image...",
                                     type=['png', 'jpg', 'jpeg'])

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
