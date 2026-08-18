# Imports
import os
from dotenv import load_dotenv
import streamlit as st
import anthropic
from datetime import date

# Claude Connection
load_dotenv()
client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))

# Visual Setup
st.set_page_config(page_title = "Task Prioritizer", page_icon = "📋", layout = "centered")
st.title("Task Prioritizer")
st.write("What are your current tasks? Add them below")

# Ensures list is not erased with each new input
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Page Layout and saving user inputs
with st.form("task_form", clear_on_submit = True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Task Name")
        due = st.date_input("Due Date", min_value = date.today())
    with col2:
        effort = st.select_slider("Effort Amount", options = ["Small", "Medium", "Large"])
        # Note, the default weight of importance is 20%
        weight = st.slider("Importance to Grade", 0, 100, 20)

    submitted = st.form_submit_button("Add Task")

# Add task to list
if submitted and name.strip() != "":
    st.session_state.tasks.append({
        "name": name,
        "due": due,
        "effort": effort,
        "weight": weight
    })

# Display list
if st.session_state.tasks:
    st.subheader("Your Tasks")
    st.table(st.session_state.tasks)

# Build readable text from data
if st.button("Prioritize"):
    with st.spinner("Thinking..."):
        today = date.today()
        task_lines = []
        for t in st.session_state.tasks:
            days_left = (t["due"] - today).days
            task_lines.append(
                # Create a string with the info on a task
                f"- {t['name']}: due in {days_left} days, effort = {t['effort']}, importance = {t['weight']}%"
            )
        task_summary = "\n".join(task_lines)

    # Prompt
    prompt = f"""You are helping a student prioritize their to-do list.
    Using the urgency (days left till due), effort, and importance, rank these tasks:

    Tasks:
    {task_summary}
    """

    response = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens = 800,
        messages = [{"role": "user", "content": prompt}]
    )

    st.markdown(response.content[0].text)
