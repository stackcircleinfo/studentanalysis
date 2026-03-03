import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Welcome to Student Data Analysis Project", page_icon=":material/thumb_up:", 
                   layout="wide", initial_sidebar_state="expanded",   menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })

st.title("🎓 Welcome to Student Result Analysis System")
st.sidebar.title("StackCircle")
with st.sidebar:
    uploaded_file=st.file_uploader("Please Upload CSV File for Analysis",type=["csv"])
    
    st.markdown("---")

    selected = option_menu(
        menu_title="📌 Menu",
        options=[
            "Raw Data",
            "Student Result",
            "Topper",
            # "Search Student",
            # "Subject Analysis",
            # "Pass / Fail",
            # "Pivot Table"
        ],
        icons=[
            "table",
            "bar-chart",
            "trophy",
            # "search",
            # "book",
            # "check-circle",
            # "grid"
        ],
        menu_icon="menu-button-wide",
        default_index=0
    )
if uploaded_file is None:
    st.warning("Please select CSV file to start analysis")
    st.stop()

df=pd.read_csv(uploaded_file)
if selected=="Raw Data":
    st.subheader("🚀 Raw Data")
    st.dataframe(df)
elif selected=="Student Result":
    st.subheader("Student Result")
    total=df.groupby("Name")["Marks"].sum()
    avg=df.groupby("Name")["Marks"].mean()
    st.dataframe({"Total":total,"Average":avg})
    
elif selected=="Topper":
    st.subheader("Topper in Class")
    topper=df.groupby("Name")["Marks"].sum().sort_values(ascending=False)
    st.dataframe(topper.head(1))


    