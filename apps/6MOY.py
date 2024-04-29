import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
 
st.title('6th man of the year votes')
df=pd.read_csv('https://github.com/Schemme/FINAL-PROJECT/blob/main/6MOY.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.sidebar.title("Choose votes to Display")
    first_place = st.sidebar.checkbox("1st Place Votes", value=True)
    second_place = st.sidebar.checkbox("2nd Place Votes", value=True)
    third_place = st.sidebar.checkbox("3rd Place Votes", value=True)


    fig, ax = plt.subplots()
    data_to_plot = df[columns_to_display].sum()
    data_to_plot.plot(kind='bar', ax=ax)
    ax.set_ylabel('Votes')
    ax.set_title('Votes Distribution')
    st.pyplot(fig)
