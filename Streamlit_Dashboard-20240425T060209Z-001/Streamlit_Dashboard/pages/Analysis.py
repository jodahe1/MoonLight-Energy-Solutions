import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration
st.set_page_config(page_title="Basic EDA with Correlation Heatmaps & Regression", layout="wide")

# Add a sidebar for file upload
st.sidebar.title("Upload CSV Files")
file1 = st.sidebar.file_uploader("Upload File 1", type="csv")
file2 = st.sidebar.file_uploader("Upload File 2", type="csv")
file3 = st.sidebar.file_uploader("Upload File 3", type="csv")

# Check if files are uploaded
if file1 is not None and file2 is not None and file3 is not None:
    # Load the data
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)
    data3 = pd.read_csv(file3)

    # Show the first few rows of each dataset
    st.subheader("First Few Rows of Each Dataset")
    st.write("Dataset 1:")
    st.write(data1.head())
    st.write("Dataset 2:")
    st.write(data2.head())
    st.write("Dataset 3:")
    st.write(data3.head())

    # Show descriptive statistics
    st.subheader("Descriptive Statistics")
    st.write("Dataset 1:")
    st.write(data1.describe())
    st.write("Dataset 2:")
    st.write(data2.describe())
    st.write("Dataset 3:")
    st.write(data3.describe())

    # Show missing value information
    st.subheader("Missing Value Information")
    st.write("Dataset 1:")
    st.write(data1.isnull().sum())
    st.write("Dataset 2:")
    st.write(data2.isnull().sum())
    st.write("Dataset 3:")
    st.write(data3.isnull().sum())

    # # Correlation Heatmaps
    st.subheader("Correlation Heatmaps")
    columns_of_interest = ["GHI", "DHI", "ModA", "ModB", "Tamb", "RH", "WS", "WD"]
    for dataset, data in zip(["Dataset 1", "Dataset 2", "Dataset 3"], [data1, data2, data3]):
       selected_cols = [col for col in columns_of_interest if col in data.columns]
       if len(selected_cols) > 1:  # Check if there are enough numeric columns
            fig, ax = plt.subplots()
            sns.heatmap(data[selected_cols].corr(), annot=True, ax=ax)
            ax.set_title(f"{dataset} Correlation Heatmap")
            st.pyplot(fig)
    else:
            st.write(f"{dataset} has insufficient numeric columns for a heatmap.")

   

    # Show scatter plots 
    st.subheader("Scatter Plots")
    cols = st.multiselect("Select Columns for Scatter Plot", data1.columns)
    if len(cols) == 2:
        fig, ax = plt.subplots()
        ax.scatter(data1[cols[0]], data1[cols[1]])
        ax.set_xlabel(cols[0])
        ax.set_ylabel(cols[1])
        st.pyplot(fig)

    # Show histograms 
    st.subheader("Histograms")
    cols = st.multiselect("Select Columns for Histogram", data1.columns)
    if len(cols) > 0:
        fig, axs = plt.subplots(nrows=len(cols), ncols=1, figsize=(6, 4 * len(cols)))
        for i, col in enumerate(cols):
            axs[i].hist(data1[col], bins=20)
            axs[i].set_title(col)
        st.pyplot(fig)

else:
    st.warning("Please upload The CSV files to proceed.")
