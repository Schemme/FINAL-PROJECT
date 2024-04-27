import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

st.title('6th man of the year votes')
df=pd.read_csv('Schemme/FINAL-PROJECT/6MOY.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

player=st.radio('Select the player')