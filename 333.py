from vega_datasets import data
import streamlit as st
import altair as alt
import numpy as np
import time
#from PIL import Image

    


def main():
    page1 = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration", "Page_3", "Page_columns", "Page_tables", "Page_expander", "Page_container", "Page_empty", "Page_image", "Page_status_elements", "Page_form"])

    page = st.sidebar.radio("Choose a page", ["Homepage", "Exploration", "Page_3", "Page_columns", "Page_tables", "Page_expander", "Page_container", "Page_empty", "Page_image", "Page_status_elements", "Page_form"])

    
    #└─── pages/
    #    └─── About.py # This is a page
    #    └─── 2_Page_two.py # This is another page
    #    └─── 3_😎_three.py # So is this
    if page == "Homepage":
        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
        #st.write(df)
    elif page == "Exploration":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")         
        st_color_picker = st.color_picker('Pick a color')
        if st_color_picker:
            st.write(st_color_picker)
            st.write(type(st_color_picker))  
        tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
        with tab1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        with tab2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        with tab3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
 
    if page1 == "Homepage":
        #container = st.container()            
        #container.write("This is inside the container")
        #st.write("This is outside the container")
        # Now insert some more in the container
        #container.write("This is inside too")  
        with st.container():
            st.write("This is inside the container")
            # You can call any Streamlit command, including custom components:
            st.bar_chart(np.random.randn(50, 3))
        st.write("This is outside the container 2")   
        #st.write(df)
        expander = st.expander("See explanation")
        expander.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
        """)
        expander.image("https://static.streamlit.io/examples/dice.jpg")           
        
        
    elif page1 == "Exploration":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")         
        st_color_picker = st.color_picker('Pick a color')
        if st_color_picker:
            st.write(st_color_picker)
            st.write(type(st_color_picker))  
        tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
        with tab1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        with tab2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        with tab3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


if __name__ == "__main__":
    st.set_page_config(page_title='Omdena Envisionit', page_icon="🧊", layout='centered', initial_sidebar_state='auto')
    main()