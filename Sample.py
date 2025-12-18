import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="Goddard Riverside Dashboard", layout="wide")

# 2. Custom CSS with Droid Sans and Goddard Riverside Colors
st.markdown("""
    <style>
    /* Import Droid Serif from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Droid+Serif:ital,wght@0,400;0,700;1,400;1,700&display=swap');

    /* Force Droid Serif onto the main Streamlit variables */
    :root {
        --font: 'Droid Serif', serif !important;
    }

    /* Target every possible text element */
    html, body, [class*="st-"], .stApp, .stMarkdown, p, div, span, label, button {
        font-family: 'Droid Serif', serif !important;
    }

    /* Headings in Goddard Red */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Droid Serif', serif !important;
        color: #A50034 !important;
        font-weight: 700 !important;
    }

    /* App Background */
    .stApp {
        background-color: #FAF7EB;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #A50034;
        border-radius: 4px 4px 0px 0px;
        padding: 10px 20px;
    }
    /* Ensure tab text is Droid Serif and white */
    .stTabs [data-baseweb="tab"] div p {
        font-family: 'Droid Serif', serif !important;
        color: white !important;
        font-size: 16px;
    }
    /* 1. Style for the SELECTED tab */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #800028 !important; /* Darker Goddard Red */
        border-bottom: 5px solid #FAF7EB !important; /* Cream underline effect */
    }
    st.sidebar.markdown("<h2 style='font-size: 20px; color: #A50034; font-family: \"Droid Serif\", serif;'>By Michelle</h2>", unsafe_allow_html=True)

    </style>
    """, unsafe_allow_html=True)
# --- APP CONTENT ---

st.title("Goddard Riverside Community Portal")
st.subheader("Developed By Michelle Chiquitero")


tab1, tab2, tab3 = st.tabs(["Looker Dashboard", " Google Sheets", "Jotform"])

with tab1:
    st.header("Analytics Overview")
    looker_url = "https://lookerstudio.google.com/embed/reporting/44431229-56fb-47f8-9afe-3805bd3e2814/page/AnoiF"
    # Using the 'sandbox' fix to help with cookie access
    st.components.v1.html(
        f"""<iframe src="{looker_url}" width="100%" height="800" style="border:0" allowfullscreen 
        sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-forms"></iframe>""",
        height=820,
    )

with tab2:
    st.header("Live Spreadsheet Data")
    sheets_url = "https://docs.google.com/spreadsheets/d/1iW5_4_y3Lb_zK_plfgM3-wB1qCYtoADzxYYH8-EhR7k/edit?usp=sharing"
    components.iframe(sheets_url, height=600, scrolling=True)

with tab3:
    st.header("Submit Information")
    jotform_url = "https://form.jotform.com/253443777192061"
    components.iframe(jotform_url, height=900, scrolling=True)