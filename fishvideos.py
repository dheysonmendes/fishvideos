import streamlit as st
from pytube import YouTube



st.title('Pescar Videos Youtube')
with st.form(key='dowload'):
    link = st.text_input(label='Insira o link do video:')
    botão_enviar = st.form_submit_button('Pescar')


if link:
    video = YouTube(link)
    video.streams.first().download()
    st.write('Pescando.')


