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
            "Search Student",
            "Subject Analysis",
            "Pass / Fail",
            "Pivot Table"
        ],
        icons=[
            "table",
            "bar-chart",
            "trophy",
            "search",
            "book",
            "check-circle",
            "grid"
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
    
    n=st.number_input("How many topper you want to show",min_value=1,max_value=len(topper))
    st.dataframe(topper.head(n))
    
elif selected=="Search Student":
    st.subheader("Search Student")
    filter_txt=st.text_input("Enter student name to search")
    filtered_data=df[df["Name"].str.lower()==filter_txt.lower()]
    if not filtered_data.empty:
        st.dataframe(filtered_data)
        total=filtered_data["Marks"].sum()
        avg=filtered_data["Marks"].mean()
        st.write(f"Total marks of {filter_txt}={total}")
        st.write(f"Average marks of {filter_txt}={avg}")
elif selected=="Subject Analysis":
    avg=df.groupby("Subject")["Marks"].mean()
    st.dataframe(avg)
    
elif selected=="Pass / Fail":
    m=st.slider("Please select min marks",min_value=0,max_value=100,value=40)
    df["Result"]=df["Marks"].apply(
        lambda x: "Pass" if x>=m else "Fail"
    )
    st.dataframe(df)
    st.subheader("Summary of student")
    st.write(df["Result"].value_counts())
elif selected=="Pivot Table":
    pivot=df.pivot_table(values="Marks",index="Subject",columns="Name")
    st.dataframe(pivot)
        


    