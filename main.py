#import lib
import streamlit as st
import pandas as pd
#add header
st.title('Data Visualization')
#upload data
data_file = st.file_uploader('choose a csv file',type=(['.csv']))
if data_file is not None:
  df = pd.read_csv(data_file)
  st.dataframe(df)
