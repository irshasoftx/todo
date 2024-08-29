import streamlit as st
from altair import Color

import functions

# Fetch the current list of todos
todos = functions.get_todos()

# Function to add a new todo
def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:  # Check if the todo is not empty
        todos.append(todo + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear the input box after adding

# Function to edit a todo in place
def edit_todo_in_place(index, new_value):
    todos[index] = new_value + "\n"
    functions.write_todos(todos)
    st.session_state["rerun"] = not st.session_state.get("rerun", False)  # Trigger a rerun

# UI setup
st.image("logo.png", width=150)  # Add your logo here
st.title("ToDo App")
#st.subheader("Welcome to Irshasoft ToDo App")
#st.write("This app is to increase your productivity")

# Display the list of todos with editable checkboxes
for index, todo in enumerate(todos):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        if f"edit_{index}" in st.session_state:
            # Editable text input when clicked on the checkbox
            new_value = st.text_input("", value=todos[index].strip(), key=f"edit_input_{index}")
            st.button("Save", key=f"save_{index}", on_click=edit_todo_in_place, args=(index, new_value))
        else:
            # Display the ToDo item normally with a checkbox
            if st.checkbox(todo.strip(), key=f"todo_{index}"):
                todos.pop(index)
                functions.write_todos(todos)
                st.session_state["rerun"] = not st.session_state.get("rerun", False)  # Trigger a rerun

# Input box for new todo
st.text_input(label="", placeholder="Add a new ToDo...", on_change=add_todo, key='new_todo')
