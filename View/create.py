import streamlit as st
from Controllers.Costumer import Costumer
from Models.Costumer import Costumer as CostumerModel


def create_action():
    costumer = CostumerModel(
        name=st.session_state.name,
        age=st.session_state.age,
        email=st.session_state.email,
    )

    if costumer.name == "" or costumer.age == "" or costumer.email == "":
        st.warning("Please, fill up all fields.")

    else:
        Costumer().create(costumer)
        st.success(f"{st.session_state.name} was created")


def create_form():

    with st.form(key="update_client_form"):

        st.text_input(label="Name:", key="name")
        st.number_input(label="Age", format="%d", step=1, key="age")
        st.text_input(label="E-mail:", key="email")
        st.form_submit_button(label="Update", on_click=create_action)
