import streamlit as st
import random
import time
 
st.title('실시간 IoT 센서 데이터')
 
data = []
 
for _ in range(100):
    data.append(random.randint(0, 100))
    st.line_chart(data)
    time.sleep(0.1)

    