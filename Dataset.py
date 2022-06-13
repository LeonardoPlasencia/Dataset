import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
import gdown

#id = 1op-iq0XhBXBQOPlagCPE9TzFsFkkNVjQ

@st.experimental_memo

def download_data():
  #https://drive.google.com/uc?id=
  url = "https://drive.google.com/uc?id=1op-iq0XhBXBQOPlagCPE9TzFsFkkNVjQ"
  output= "data.csv"
  gdown.download(url,output,quiet = False)
  
download_data()
data = pd.read.csv("data.csv", sep = ";", nrows = 1000000, parse_dates = ["FECHA_CORTE","FECHA_RESULTADO"])
st.dataframe(data.head(20))

edades = data["EDAD"]
st.line_chart(edades)
