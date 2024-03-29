import streamlit
import pandas as pd
import requests
import snowflake.connector
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
list_1 = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
list_1 = list_1.set_index('Calories')
calories_selected=streamlit.multiselect("Pick some calories:", list(list_1.index),[130,50,110])
calories_to_show = list_1.loc[calories_selected]
streamlit.dataframe(calories_to_show)
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute('select * from fruit_load_list')
my_data_row = my_cur.fetchone()
streamlit.text('The fruit load list contains:')
streamlit.text(my_data_row)


