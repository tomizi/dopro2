# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:51:56 2022

@author: User
"""
import os
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from pathlib import Path

os_path = Path(__file__).patern[0]
st.set_page_config(page_title='Sales Dashboard', page_icon = ':bar_chart:',
                  layout='centered')
df = pd.read_excel(open(os_path,'rb'))


st.sidebar.header('Please Filter Here:')

miejsce = st.sidebar.multiselect(
    "Wybierz miejsce:",
    options=df['miejsce'].unique(),
    default=df['miejsce'].unique()
    )

df_selection= df.query(
    "miejsce == @miejsce")



st.title(':bar_chart: Wydatki')
#st.markdown('##')




l_c,r_c = st.columns(2)

suma = int(np.sum(df_selection.cena))
srednia = round(np.mean(df_selection['cena']),2)



with l_c:
    st.subheader('Suma:')
    st.subheader(f'{suma:,}zl')
with r_c:
    st.subheader('Średnia:')
    st.subheader(f"{srednia:,}zl")
st.markdown('---')



spsp = pd.DataFrame(df_selection.groupby(by=['miejsce'])['cena'].agg(np.sum)).sort_values(by='cena')

fig = px.bar(
    spsp,
    x = 'cena',
    y = spsp.index,
    orientation = 'h',
    title = '<b>Suma ceny produktów</b>')
st.plotly_chart(fig)
