import streamlit as st
import pandas as pd
 
# 데이터 로드
data = pd.read_csv('kospi.csv')
 
# 제목 생성
st.title('나의 첫 번째 Streamlit 대시보드')
 
# 테이블에 데이터 표시
st.table(data)