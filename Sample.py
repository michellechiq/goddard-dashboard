import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="Goddard Riverside Dashboard", layout="wide")

# 2. Corrected CSS: Forced Black Text for Readme and No Sidebar
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Droid+Serif:ital,wght@0,400;0,700;1,400;1,700&display=swap');

    :root {
        --font: 'Droid Serif', serif !important;
    }

    /* 1. FORCE ALL TEXT TO BE VISIBLE (Dark Grey/Black) */
    html, body, .stApp, .stMarkdown, p, li, span {
        font-family: 'Droid Serif', serif !important;
        color: #333333 !important; /* This makes your README text dark/visible */
    }

    /* 2. HEADER COLORS */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Droid Serif', serif !important;
        color: #A50034 !important;
        font-weight: 700 !important;
    }

    .stApp {
        background-color: #FAF7EB;
    }

    /* 3. TAB STYLING */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #E0DBC3; 
        border-radius: 4px 4px 0px 0px;
        padding: 10px 20px;
    }
    /* Inactive Tab Text */
    .stTabs [data-baseweb="tab"] div p {
        color: #333333 !important; 
    }
    /* Active Tab (Goddard Red) */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #A50034 !important;
    }
    /* White text ONLY on the active red tab */
    .stTabs [data-baseweb="tab"][aria-selected="true"] div p {
        color: white !important;
    }

    /* 4. REMOVE SIDEBAR COMPLETELY */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
        display: none !important;
        width: 0px !important;
    }
    
    /* Ensure the main content uses the full width now that sidebar is gone */
    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP CONTENT ---
st.title("Goddard Riverside Community Portal")
st.subheader("Developed By Michelle Chiquitero")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Looker Dashboard", "Google Sheets", "Jotform", "Project Info"])

with tab1:
    st.header("Analytics Overview")
    looker_url = "https://lookerstudio.google.com/embed/reporting/44431229-56fb-47f8-9afe-3805bd3e2814/page/AnoiF"
    components.html(
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

with tab4:
    # Everything inside this tab is now forced to be dark/visible by the CSS above
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_text = f.read()
        st.markdown(readme_text)
    except FileNotFoundError:
        st.warning("README.md file not found.")