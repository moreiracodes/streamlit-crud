# streamlit-crud

This CRUD uses Python, [Streamlit](https://streamlit.io/) and SQL SERVER. 

The main goal of this project was got my hands on streamlit lib and feel what I could do with that.


## To run the project

1. Create a .env file in the project directory to set up the environment variables: DB_SERVER, DB_NAME, DB_USERNAME and DB_PASSWORD.

2. If you don't use SQL SERVER, be careful! There is one T-SQL query in create table method in [line 13](https://github.com/moreiracodes/streamlit-crud/blob/main/Controllers/Costumer.py) that might not work properly in others SQL databases.

3. Install the dependencies ` run pip install -r requeriments.txt ` 

4. Run the server with the command ` streamlit run main.py `
