import streamlit as st
from Controllers.Costumer import Costumer
from Models.Costumer import Costumer as CostumerModel


def update_action():
    costumer = CostumerModel(
        name=st.session_state.name,
        age=st.session_state.age,
        email=st.session_state.email,
        id=st.session_state.costumer_id,
    )

    Costumer().update(costumer)
    st.success(f"{st.session_state.name} was updated successfully")


def update_form(costumer):

    with st.form(key="update_client_form_" + str(costumer.id)):

        st.session_state.costumer_id = costumer.id
        st.text_input(label="Name:", value=costumer.name, key="name")
        st.number_input(
            label="Age", format="%d", step=1, value=costumer.age, key="age"
        )
        st.text_input(label="E-mail:", value=costumer.email, key="email")
        st.form_submit_button(label="Update", on_click=update_action)
