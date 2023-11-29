#import lib
import streamlit as st
import pandas as pd
import io
#add header
st.title('Data Visualization')
#upload data
data_file = st.file_uploader('choose a csv file',type=(['.csv']))
#show data
if data_file is not None:
  df = pd.read_csv(data_file)
  st.header('Show data')
  st.dataframe(df)
  #add describe
  st.header('Descriptive statistics')
  st.table(df.describe())
  #add info
  st.header('Show data info')
  buffer = io.StringIO()
  df.info(buf=buffer)
  st.text(buffer.getvalue())
