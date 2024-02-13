import streamlit
streamlit.title('Welcome to streamlit world')
streamlit.header('First lesson')
streamlit.text('Today logged in')
streamlit.text('Eager to create app')
streamlit.text('It is soo interesting....')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas as pd
list_1 = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
list_1 = list_1.set_index('Calories')
streamlit.multiselect("Pick some calories:", list(list_1.index),[130,50,110])
streamlit.dataframe(list_1)



