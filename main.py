import streamlit as st
st.title('나의 첫 웹 서비스 만들기') 
a=st.st.text_input('왓츄어네임')
if st.button('인사말 생성'):
   st.write(a+'님아 안녕하시긔')
