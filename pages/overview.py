'''

Overview Page of teh App

'''

import streamlit as st

import pandas

pagekey = 'review_analytics'

def app():
    st.title('Overview')
    st.write('This is an app used to analyze useful reviews from the open database from Amazon.')