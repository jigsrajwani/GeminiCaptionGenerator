import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("API"))

def get_social_media_caption(image, input_text):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, image])
    return response.text

# UI Improvements
st.set_page_config(page_title='Social Media Image Enhancer', layout='wide')
st.title("Social Media Image Enhancer")
st.markdown("## Enhance your social media images with captivating captions!")

# Improved layout using columns
col1, col2 = st.columns(2)

# Additional input options
input_text = col1.text_input('Caption prompt:', key='input')

# Image upload and display on the left side
upload = col1.file_uploader("Upload image:")

if upload is not None:
    image = Image.open(upload)
    col1.image(image, caption='Uploaded image', use_column_width=True)

# Generated caption on the right side
col2.subheader("Generated Caption:")

# More interactive components
submit = col2.button("Generate Caption")

if submit and upload is not None:
    # No threshold parameter
    caption = get_social_media_caption(image, input_text)
    col2.write(caption)
