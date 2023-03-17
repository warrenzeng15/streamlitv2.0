import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(
     page_title="Streamlit Introduction",
     page_icon="💯",
     initial_sidebar_state="expanded",
)

banner = Image.open('banner.png')
st.image(banner)

st.title('Welcome to my presentation on Streamlit!')

st.header('Now, what is Streamlit exactly?')
st.write("Started in 2019, with version 1.0 being released in 2021, Streamlit is an open-source framework that turns datascripts (Python) into working web applications.")  
st.write("Basically, it’s a platform that allows you to build a data website very quickly")
st.write("It's not “educational” in the literal sense, but can be used to facilitate data related projects, or for students to build websites for projects")

         
st.write("")
st.write("Check out the Streamlit Gallery for many interesting examples!: [link](https://streamlit.io/gallery)")

st.write("")
st.header(":red[At this point I realized that re-doing my powerpoint slides here would be time consuming and redundant, so instead i'm just going to throw some examples down here.]") 
st.header(":red[I pulled most of these from the documentation by copy/pasting:]")

st.write(":blue[Here's a slider widget that lets you choose a value by sliding:]")
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

sliders = '''age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')'''
st.code(sliders, language='python')

st.write("")
st.write(':blue[This widget finds the square value of the number you choose on the slider:]')
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

squares = '''x = st.slider("Select a value")
st.write(x, "squared is", x * x)'''
st.code(squares, language='python')

st.write("")

st.write(":blue[This one is a color picker:]")
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

colorpicker = '''color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)'''
st.code(colorpicker, language='python')


st.write(':blue[Line chart:]')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

linechart= '''chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)'''
st.code(linechart, language='python')

st.write(':blue[Bar chart:]')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

barchart='''chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)'''
st.code(barchart, language='python')

st.write(':blue[Dot map:]')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.7678, -73.9645],
    columns=['lat', 'lon'])

st.map(df)

dotmap ='''df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.7678, -73.9645],
    columns=['lat', 'lon'])
    
st.map(df)'''

st.code(dotmap, language='python')


st.write("")
st.header("There are many other useful widgets that you can find in the documentation. There are also community made 'components' which you can use in your own projects: [link](https://streamlit.io/components?category=featured)")


