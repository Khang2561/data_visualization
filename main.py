#import lib
import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns
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
  #Visualize each attribute
  st.header('Visualize each attribute')
  for col in list(df.columns):
    fig, ax = plt.subplots()
    ax.hist(df[col],bins = 20)
    plt.xlabel(col)
    plt.ylabel('Quality')
    st.pyplot(fig)

    st.header('Show correlation between varibles')
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(method = 'pearson'),ax =ax,vmax =1,square = True,annot=True,cmap='Blues')
    st.write(fig)
