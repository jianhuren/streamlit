import pandas as pd
from datetime import time
import streamlit as st

# st.title('Hello World')
data = pd.read_excel('/Users/mac/Desktop/Workbook.xlsx',sheet_name='Sheet1')
a = int(max(data['红包剩余金额']))
print(a)
st.slider('金额大小',0,a,(0,int(a/2)),key='start')
st.session_state.start[0]
print(type(st.session_state.start[0]))
st.slider('时间选择',value=(time(11,30),time(9,30)))
# df = pd.DataFrame(data[(data['红包剩余金额']>=st.session_state.start[0]) & (data['红包剩余金额']<=st.session_state.start[1])])
# st.text(len(df))
# st.write(df)
st.selectbox('选择',[1,2,3])


st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
    'Red')

st.write('You selected:', options)
st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")