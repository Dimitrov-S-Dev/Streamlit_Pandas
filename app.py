#
import pandas as pd
import seaborn as sns
import streamlit as st

# 1 Title and Subheader
st.title("Dimitrov-S-Dev")
st.subheader("Data Analysis with Python and Streamlit")

# 2 Upload Dataset
upload = st.file_uploader("Upload your Dataset(=>>>CSV format ONLY!<<<=)")

# 3 Show Dataset
if upload is not None:
    df = pd.read_csv(upload)
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(df.head())
        if st.button("Tail"):
            st.write(df.tail())

# 4 Check DataType of each column
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(df.dtypes)

# 5 Find Shape of our Dataset
if upload is not None:
    data_shape = st.radio("What Dimensions Would you like to check?", ('Rows', 'Columns'))
    if data_shape == "Rows":
        st.text("Number of Rows")
        st.write(df.shape[0])
    if data_shape == "Columns":
        st.text("Number of Columns")
        st.write(df.shape[1])

# 6 Find Null Values in the Dataset
if upload is not None:
    test = df.isnull().values.any()
    if test:
        if st.checkbox("Null Values in the Dataset"):
            sns.heatmap(df.isnull())
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    else:
        st.success("Great!!!,No missing Values")

# 7 Find Duplicated Values in the Dataset
if upload is not None:
    test = df.duplicated().any()
    if test:
        st.warning("Dataset Contains Some Duplicated Values")
        dup = st.selectbox("Would you like to remove Duplicated Values?", ('Select', 'Yes', 'No'))
        if dup == "Yes":
            df = df.drop_duplicates()
            st.text("Duplicated Values are Removed")
        if dup == "No":
            st.text("As you wish")

# 8 Get Overall Statistic
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(df.describe())

# 9 About Section
if st.button("About App"):
    st.text("Built with Streamlit")


# 10 By
if st.checkbox("Created By"):
    st.success("Dimitrov-S-Dev")

# Download uploaded file
if st.button("Save DataFrame"):
    open("data_streamlit.csv", "w").write(df.to_csv())
    st.text("Saved to local Drive")
