import streamlit as st
import View.read as Read
import View.create as Create

new_costumer_container = st.empty()
create_button = new_costumer_container.button("New Costumer")

if create_button:
    Create.create_form()

Read.read()
