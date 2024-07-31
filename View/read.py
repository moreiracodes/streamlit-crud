from Controllers.Costumer import Costumer
import streamlit as st
import time
import View.update as Update


def read():
    st.title("Costumers")

    cols = st.columns((1, 4, 1, 5, 2, 2), vertical_alignment="center")
    fields = ["Id", "Name", "Age", "E-mail", "", ""]
    for col, field in zip(cols, fields):
        if field:
            col.write(f"**{field}**")
        else:
            col.write(f"{field}")

    for costumer in Costumer().get_all():
        col1, col2, col3, col4, col5, col6 = st.columns(
            (1, 4, 1, 5, 2, 2), vertical_alignment="center"
        )
        col1.text(costumer.id)
        col2.text(costumer.name)
        col3.text(costumer.age)
        col4.text(costumer.email)

        delete_button_container = col5.empty()
        on_click_delete_button = delete_button_container.button(
            "Remove", "btn_remove" + str(costumer.id)
        )

        update_button_container = col6.empty()
        on_click_update_button = update_button_container.button(
            "Update", "btn_update" + str(costumer.id)
        )

        if on_click_delete_button:
            Costumer().delete(costumer)
            st.success(f"{costumer.name} was removed")
            time.sleep(2)
            st.rerun()

        if on_click_update_button:
            Update.update_form(costumer)
