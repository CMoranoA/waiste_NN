import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from waiste.params import PATH_TO_PUNTOS_VERDES

data = pd.read_csv(PATH_TO_PUNTOS_VERDES)


def minkowski_distance(lat_casa="latitud_casa",
                       long_casa="longitud_casa",
                       lat_punto="dropoff_latitude",
                       long_punto="dropoff_longitude"):
    x1 = long_casa
    x2 = long_punto
    y1 = lat_casa
    y2 = lat_punto
    return ((abs(x2 - x1) ** 2) + (abs(y2 - y1)) ** 2) ** (1 / 2)

def locate_lat_long(direction):
    geolocator = Nominatim(user_agent="example app")
    location = geolocator.geocode(f"{direction}, Capital Federal, Argentina").point
    lat, long = location[0], location[1]
    return (lat, long)

def calculate_minimun_distance(direction, material):
    if material == "No reciclable":
        return ("Material no reciclable.")
    else:
        # dirección casa
        lat_d = locate_lat_long(direction)[0]
        long_d = locate_lat_long(direction)[1]

        #subset dataframe para dejar los que puntos que tienen la categoría de la foto y buscar lat y long
        data_set = data[data[material] == 1]
        lat_p = data_set["Lat"]
        long_p = data_set["Long"]

        #calcular distancias
        distancias = []
        for i in range(data_set.shape[0]):
            distancias.append(minkowski_distance(lat_casa = lat_d, long_casa = long_d,
                                                    lat_punto = lat_p[i], long_punto = long_p[i]))

        return (data.iloc[distancias.index(min(distancias)), 2:7])
