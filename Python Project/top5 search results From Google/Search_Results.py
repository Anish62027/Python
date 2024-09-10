import streamlit as st
from googlesearch import search

st.header("Top5 Sarch Results From Google")

query = st.text_input("Enter You Search Query")
butoon = st.button("SUBMIT")

if butoon:
    search_results = search(query, num_results=5, lang="en")
    st.text(f"Your Sarch Query :- {query} ")

    for i, result in enumerate(search_results, start=1):
        
        st.info(f"Result {i}:")
        st.info(result)

    st.text("Thank You")   
    st.text("©2024 Life Tech ")
        
        

