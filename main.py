import streamlit as st
st.title('나의 첫 웹 서비스 만들기') 
a=st.text_input('왓츄어네임')
b=st.selectbox('좋아하는 음식이 뭐긔?',['국밥','새우','족발'])
if st.button('인사말 생성'):
   st.write(a+'님아 안녕하시긔')
st.write('b+'를 좋아하노? 난 싫어하긔;')
