import streamlit as st
import source_data
import pandas

pagekey = 'review_analytics'

def app():
    st.title('Reviews Analytics')
    d_json = source_data.get_data()
    df_train = d_json['train']
    df_test = d_json['test']

    st.dataframe(df_test)