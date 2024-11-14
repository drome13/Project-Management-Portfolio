import streamlit as st
from streamlit_option_menu import option_menu
from templates import ganttchart, sow  # Import display functions for specific pages

# Initialize session state for page selection if it doesn't exist
if "selected_page" not in st.session_state:
    st.session_state["selected_page"] = "Home"

# Apply CSS styling to the sidebar and the main header
st.markdown(
    """
    <style>
    /* Sidebar customization */
    .css-1d391kg { /* Sidebar container class, this might change across versions */
        background-color: #333;  /* Dark background color */
        padding: 20px;
    }
    .css-1d391kg .css-1v0mbdj { /* The menu title in sidebar */
        color: #FFF;  /* White font color */
    }
    .css-1d391kg .css-17eq0hr {  /* Sidebar menu items */
        color: #80DDFF;  /* Light blue font color */
        font-size: 1.2em;
    }
    .css-1d391kg .css-17eq0hr:hover {
        color: #FFF;  /* White font color on hover */
    }

    /* Title styling */
    .title-header {
        background-color: #80DDFF;
        color: black;
        text-align: center;
        border: solid 3px black;
        padding: 20px;
        font-size: 2em;
        margin-bottom: 20px;
    }
    
    /* Styling the page content */
    .stMarkdown {
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Gantt Chart", "Work Breakdown Structure", "Mindmap", "SOW"],
        icons=["house", "bar-chart-steps", "list-ul", "diagram-3", "person-workspace"],
        default_index=["Home", "Gantt Chart", "Work Breakdown Structure", "Mindmap", "SOW"].index(st.session_state["selected_page"]),
    )
    # Update session state with selected page
    st.session_state["selected_page"] = selected

# Display header
st.markdown('<h1 class="title-header">Group 5 Project Management Portfolio</h1>', unsafe_allow_html=True)

# Content display based on selected page
if st.session_state["selected_page"] == "Home":
    st.write("Welcome to the Home Page!")
elif st.session_state["selected_page"] == "Gantt Chart":
    ganttchart.display_gantt_chart()
elif st.session_state["selected_page"] == "Work Breakdown Structure":
    st.title("Work Breakdown Structure")
elif st.session_state["selected_page"] == "Mindmap":
    st.title("Mindmap")
elif st.session_state["selected_page"] == "SOW":
    sow.display_statement_of_work()
