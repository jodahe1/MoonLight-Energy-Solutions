import streamlit as st
import pandas as pd
import plotly.express as px


# Function to calculate the statistical measures
def calculate_statistics(data):
    statistics = data.describe()
    return statistics

# Main function
def main():
    st.title("")
    
# Display a subheader and some text
st.subheader("Statistical Measures for MoonLight Energy Solutions")
st.write("The motive behind developin this Dashboard is to help  MoonLight Energy Solutions on there solar investments to make Starategic Decisos you can go an click the analysis button and upload the 3 .csv file you have it will do basic EDA activites which will help you out it might take sometime when it load its speed will depend on youre pc performance so be patient and wait Thank You  .")
st.write(" DashBoard created by-Yodahe Teshome")

# Run the app
if __name__ == "__main__":
    main()
