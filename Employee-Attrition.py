import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import pickle
from pathlib import Path
from PIL import Image
import Dashboard,Prediction,Contact

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
logo = current_dir / "Photos" / "logo.png"
logo = Image.open(logo)

# set page configrations
st.set_page_config(
    page_title="RetainRadar",
    page_icon="♾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# importing data
df = pd.read_csv('Employees.csv')
# set style for menu options in sidebar
style = {
        "nav-link": {"font-family": "Monospace, Arial" ,"--hover-color": "SkyBlue"},
        "nav-link-selected": {"background-color": "rgb(10, 0, 124)","font-family": "Monospace , Arial" },
    }

# the main class of the application
class MaltiPage:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function":function
        })

    def run():
        with st.sidebar:
            st.title('RetainRadar')
            st.image(logo, width=175)
        with st.sidebar:
            app = option_menu(None,
                options =['Dashboard', 'Check the Risk', 'Contact'],
                icons=["pie-chart-fill", "person-check-fill", "file-person-fill"],
                styles=style,
                default_index=0,
            )

        if app =='Dashboard':
            Dashboard.app(df, st)
        if app =='Check the Risk':
            Prediction.app(df, st, option_menu, pd, pickle)
        if app =='Contact':
            Contact.app(st, current_dir, Image)

## run the program     
    run()

