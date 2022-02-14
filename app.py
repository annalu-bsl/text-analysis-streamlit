'''

Main function to run the app. This is a multipage app.

'''

import streamlit as st

#page general configurations
st.set_page_config(

    page_title = 'Analyzing Helpful Reviews from Amazon',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

#importing resources from multipages
from multipage import MultiPage
from pages import overview, review_analytics

app = MultiPage()

#setting the title in the main page of the app 
st.title("Analyzing Helpful Reviews")

#adding multiple pages of the app
app.add_page("Overview", overview.app)
app.add_page("Reviews Analytics", review_analytics.app)

#Run the main page of the app
app.run()