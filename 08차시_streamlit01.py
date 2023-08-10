import streamlit as st
import pandas as pd
 
#코스피 주가 데이터를 로딩 
data = pd.read_csv('kospi.csv')
 
#타이틀을 출력 
st.title('나의 첫 번째 Streamlit 대시보드')
 
#데이터 출력 
st.table(data)

