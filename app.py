import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

from api.fast import predict
from waiste.distance import calculate_minimun_distance, locate_lat_long
from waiste.layout_params import background_image, title, title1, title2, title3, subtitle1, subtitle2, subtitle3, paper_title, cardboard_title, metal_title, plastic_title, glass_title, organic_title, electronics_title, bricks_title, telgopor_title, hazardous_title, clothes_title, bin_locations, find_location, enter_data, paper_bin, cardboard_bin, metal_bin, plastic_bin, glass_bin, organic_bin, electronics_bin, bricks_bin, telgopor_bin, hazardous_bin, clothes_bin, paper_small_bin, cardboard_small_bin, metal_small_bin, plastic_small_bin, glass_small_bin, organic_small_bin, electronics_small_bin, bricks_small_bin, telgopor_small_bin, hazardous_small_bin, clothes_small_bin, paper_subtitle, cardboard_subtitle, metal_subtitle, plastic_subtitle, glass_subtitle, organic_subtitle, electronics_subtitle, bricks_subtitle, telgopor_subtitle, hazardous_subtitle, clothes_subtitle, category, closest_location
from waiste.params import PATH_TO_PUNTOS_VERDES, PATH_TO_MAP_DOTS
from waiste.predict import predict_gcp
from PIL import Image

def get_map_data():
    data = pd.read_csv(PATH_TO_PUNTOS_VERDES, sep=",")
    data.rename(columns={'Lat': 'lat', 'Long': 'lon'}, inplace = True)
    df = pd.DataFrame(data[['lat', 'lon']])
    return df

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
st.markdown(enter_data, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col4, col5 = st.columns(2)
with col4:
    name = st.text_input('Name', '')

with col5:
    address = st.text_input('Address', '')

# User uploads image
with st.expander("Upload your waste image..."):
    uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'])

# Prediction
if uploaded_file:
    image = Image.open(uploaded_file)
    material = predict_gcp(image)
    # material = predict(uploaded_file)
    if material == "Telgopor":
        material = "telgopor"
    elif material == "Tetra-brik":
        material = "tetrabrik"
    elif material == "hazardous (bateries, cds)":
        material = "hazardous"
else:
    material = ""


COLORS_R = {"brown": 182, "violet": 146, "green": 40, "gray": 126, "gold": 206, "orange": 254, "darkgreen": 38, "lightblue": 82, "yellow": 254, "blue": 51, "red": 254}
COLORS_G = {"brown": 96, "violet": 45, "green": 219, "gray": 123, "gold": 173, "orange": 156, "darkgreen": 126, "lightblue": 177, "yellow": 212, "blue": 142, "red": 3}
COLORS_B = {"brown": 1, "violet": 205, "green": 3, "gray": 123, "gold": 73, "orange": 0, "darkgreen": 41, "lightblue": 190, "yellow": 0, "blue": 211, "red": 0}

# data = pd.read_csv(PATH_TO_MAP_DOTS)
# st.write(data)

LAT_COLUMN = "Lat"
LONG_COLUMN = "Long"

LOCS = {
    "Plaza Armenia": {
        "latitude": -34.6185,
        "longitude": -58.4476
    },
}

PLAZA_ARMENIA = LOCS["Plaza Armenia"]

MATERIAL_COLORS = {
    "clothes": "brown",
    "electronics": "violet",
    "organics": "green",
    "telgopor": "gray",
    "tetrabrik": "gold",
    "plastic": "orange",
    "metal": "darkgreen",
    "glass": "lightblue",
    "cardboard": "yellow",
    "paper": "blue",
    "hazardous": "red",
}

class ViewInitialLocation:
    def __init__(self):
        self.latitude = PLAZA_ARMENIA["latitude"]
        self.longitude = PLAZA_ARMENIA["longitude"]
        self.zoom = 10.85
        self.pitch = 40.0

    def edit_view(self):
        location = st.sidebar.selectbox("Location",
                                        options=list(LOCS.keys()),
                                        index=0)
        self.latitude = LOCS[location]["latitude"]
        self.longitude = LOCS[location]["longitude"]

    @property
    def view_location(self) -> pdk.ViewState:
        return pdk.ViewState(
            longitude=self.longitude,
            latitude=self.latitude,
            zoom=self.zoom
        )


class WasteBinsMap:
    def __init__(self):
        self.view_initial_location = ViewInitialLocation()
        self.data = self.get_data()
        self.show_data = False

    @staticmethod
    @st.cache
    def get_data() -> pd.DataFrame:
        data = pd.read_csv(PATH_TO_MAP_DOTS, sep=";", decimal=',')

        data["material_color"] = data.material.map(MATERIAL_COLORS)
        data["material_color"] = data["material_color"].fillna("gray")
        data["color_r"] = data["material_color"].map(COLORS_R)
        data["color_g"] = data["material_color"].map(COLORS_G)
        data["color_b"] = data["material_color"].map(COLORS_B)
        data["color_a"] = 140

        return data[[
            LAT_COLUMN,
            LONG_COLUMN,
            "material",
            "Lugar",
            "material_color",
            "color_r",
            "color_g",
            "color_b",
            "color_a",
        ]]

    def _scatter_plotter_layer(self):
        return pdk.Layer(
            "ScatterplotLayer",
            data=self.data,
            get_position=[LONG_COLUMN, LAT_COLUMN],
            get_fill_color="[color_r, color_g, color_b]",
            get_radius="color_a",
            pickable=True,
            stroked=False,
            filled=True,
            wireframe=True,
        )

    def _deck(self):
        return pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v10",
            initial_view_state=self.view_initial_location.view_location,
            layers=[self._scatter_plotter_layer()])

    def view(self):
        st.pydeck_chart(self._deck())


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if material == "":
    st.markdown(find_location, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col21, col22, col23, col24, col25, col26, col27, col28, col29, col30, col31 = st.columns(11)

    with col21:
        st.markdown(paper_small_bin, unsafe_allow_html=True)
        st.markdown(paper_subtitle, unsafe_allow_html=True)

    with col22:
        st.markdown(cardboard_small_bin, unsafe_allow_html=True)
        st.markdown(cardboard_subtitle, unsafe_allow_html=True)

    with col23:
        st.markdown(metal_small_bin, unsafe_allow_html=True)
        st.markdown(metal_subtitle, unsafe_allow_html=True)

    with col24:
        st.markdown(plastic_small_bin, unsafe_allow_html=True)
        st.markdown(plastic_subtitle, unsafe_allow_html=True)

    with col25:
        st.markdown(glass_small_bin, unsafe_allow_html=True)
        st.markdown(glass_subtitle, unsafe_allow_html=True)

    with col26:
        st.markdown(organic_small_bin, unsafe_allow_html=True)
        st.markdown(organic_subtitle, unsafe_allow_html=True)

    with col27:
        st.markdown(electronics_small_bin, unsafe_allow_html=True)
        st.markdown(electronics_subtitle, unsafe_allow_html=True)

    with col28:
        st.markdown(bricks_small_bin, unsafe_allow_html=True)
        st.markdown(bricks_subtitle, unsafe_allow_html=True)

    with col29:
        st.markdown(telgopor_small_bin, unsafe_allow_html=True)
        st.markdown(telgopor_subtitle, unsafe_allow_html=True)

    with col30:
        st.markdown(hazardous_small_bin, unsafe_allow_html=True)
        st.markdown(hazardous_subtitle, unsafe_allow_html=True)

    with col31:
        st.markdown(clothes_small_bin, unsafe_allow_html=True)
        st.markdown(clothes_subtitle, unsafe_allow_html=True)


    waste_bins = WasteBinsMap()
    waste_bins.view()

else:
    col1, col2 = st.columns([1,3])
    if material == 'metal':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(metal_bin, unsafe_allow_html=True)
            st.markdown(metal_title, unsafe_allow_html=True)

    if material == 'cardboard':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(cardboard_bin, unsafe_allow_html=True)
            st.markdown(cardboard_title, unsafe_allow_html=True)

    if material == 'paper':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(paper_bin, unsafe_allow_html=True)
            st.markdown(paper_title, unsafe_allow_html=True)

    if material == 'plastic':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(plastic_bin, unsafe_allow_html=True)
            st.markdown(plastic_title, unsafe_allow_html=True)

    if material == 'glass':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(glass_bin, unsafe_allow_html=True)
            st.markdown(glass_title, unsafe_allow_html=True)

    if material == 'organic':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(organic_bin, unsafe_allow_html=True)
            st.markdown(organic_title, unsafe_allow_html=True)

    if material == 'electronics':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(electronics_bin, unsafe_allow_html=True)
            st.markdown(electronics_title, unsafe_allow_html=True)

    if material == 'tetrabrik':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(bricks_bin, unsafe_allow_html=True)
            st.markdown(bricks_title, unsafe_allow_html=True)

    if material == 'telgopor':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(telgopor_bin, unsafe_allow_html=True)
            st.markdown(telgopor_title, unsafe_allow_html=True)

    if material == 'hazardous':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(hazardous_bin, unsafe_allow_html=True)
            st.markdown(hazardous_title, unsafe_allow_html=True)

    if material == 'clothes':
        with col1:
            st.markdown(category, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(clothes_bin, unsafe_allow_html=True)
            st.markdown(clothes_title, unsafe_allow_html=True)

    with col2:
        if material == "telgopor":
            material = "Telgopor"
        elif material == "tetrabrik":
            material = "Tetra-brik"
        elif material == "hazardous":
            material = "hazardous (bateries, cds)"
        closest_location_info = calculate_minimun_distance(address, material)
        st.markdown(closest_location, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f'<h2 style="font-family: sans-serif; color: rgba(17, 63, 8, 0.959); text-align: center; text-shadow: 0 0 black; padding-bottom: 8px; padding-left: 24px; padding-right: 24px; font-size: 16px;">{closest_location_info["Lugar"]}</h2>',
            unsafe_allow_html=True)
        st.markdown(
            f'<h2 style="font-family: sans-serif; color: rgba(17, 63, 8, 0.959); text-align: center; text-shadow: 0 0 black; padding-bottom: 8px; padding-left: 24px; padding-right: 24px; font-size: 16px;">{closest_location_info["Dirección"]} - {closest_location_info["Barrio"]}</h2>',
            unsafe_allow_html=True)
        st.markdown(
            f'<h2 style="font-family: sans-serif; color: rgba(17, 63, 8, 0.959); text-align: center; text-shadow: 0 0 black; padding-bottom: 8px; padding-left: 24px; padding-right: 24px; font-size: 16px;">{closest_location_info["Cooperativa"]}<br>Abierto: {closest_location_info["Día y Horario"]}</h2>',
            unsafe_allow_html=True)


    st.markdown("<br>", unsafe_allow_html=True)

    # Show map with closest location
    lat, long = locate_lat_long(address)
    d = {
        "Lat": [lat],
        "Long": [long],
        "material": [material],
        "material_color": [""],
        "color_r": [""],
        "color_g": [""],
        "color_b": [""],
        "color_a": [""],
    }
    data = pd.DataFrame(d)
    data["material_color"] = data.material.map(MATERIAL_COLORS)
    data["color_r"] = data["material_color"].map(COLORS_R)
    data["color_g"] = data["material_color"].map(COLORS_G)
    data["color_b"] = data["material_color"].map(COLORS_B)
    data["color_a"] = 140
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=data,
        get_position=[long, lat],
        get_fill_color="[color_r, color_g, color_b]",
        get_radius="color_a",
        pickable=True,
        stroked=False,
        filled=True,
        wireframe=True,
        get_polygon='-',
    )
    view_state = pdk.ViewState(longitude=long,
                               latitude=lat,
                               zoom=12.5)
    deck = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v10",
        initial_view_state=view_state,
        layers=[layer],
        tooltip={
            "html":
            f'{material.upper()} CONTAINER - {closest_location_info["Lugar"]}',
            "style": {
                "color": "white"
            }
        })
    st.pydeck_chart(deck)
