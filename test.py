# My first Streamlit App"

# Load Streamlit library
import streamlit as st

# Hello World
st.title('Hello World')
st.title('Paila Sunil Kumar - IMT Ghaziabad')
st.write("\nThis is my first Web App, built using Streamlit!")


from PIL import Image
image = Image.open('IMT.jpg')

st.image(image, caption='My Alma Matter')

image = Image.open('pic.jpg')

st.image(image, caption='Sunil@IMT')
