import streamlit as st
import time
import sqlite3
import pandas as pd

@st.cache_data
def load_data():
    time.sleep(2)
    with sqlite3.connect('customers.db') as con:
        return pd.read_sql('SELECT * from customers_tbl',con)

def main():
    start = time.perf_counter()
    st.set_page_config(layout="wide")

    st.write("Hello, *World!* :sunglasses:")
    st.write("# Titre 1")
    title = st.text_input("Movie title", "Life of Brian")
    
    if st.button('Click !'):
        st.write(title)

    df = load_data()
    s = st.slider("Slider",0,100)
    st.write(df)
    end = time.perf_counter()
    st.write(f"slicer value: {s} - {end-start:0.2f} s")
if __name__=='__main__':
    main()
