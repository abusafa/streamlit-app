import streamlit as st

st.title('Welcome to the Distance inspection tool!')
st.markdown("""
    The purpose of the provided Python script is to create an interactive data visualization application for exploring and analyzing student and school data. The script leverages various libraries such as pandas, streamlit, plotly, matplotlib, and pydeck to load data from a CSV file, perform data manipulations, and display visualizations and tables based on the selected data.

    The application serves the following purposes:

    1. Data Loading: The script loads data from a CSV file and stores it in a pandas DataFrame. This allows users to work with the dataset and perform various analyses.

    2. Data Visualization: The script generates visualizations to provide insights into the data. It creates a pie chart to show the distribution of students based on distance categories. Additionally, it generates a pivot table to display row counts based on administration and distance categories. These visualizations help users understand the data distribution and identify patterns or trends.

    3. Interactive Selection: The application allows users to interactively select specific administrations and schools. Users can choose an administration from a dropdown menu and then select a school associated with that administration. This feature enables users to focus on specific subsets of data and explore detailed information about selected schools.

    4. Geospatial Visualization: The script uses pydeck to create a map visualization that displays connections between schools and students. It visualizes arcs connecting the geographical coordinates of the selected school and the students associated with that school. This geospatial visualization provides a visual representation of the relationships between schools and students, allowing users to gain insights into the spatial distribution of students.

    5. Data Exploration: The application provides users with the ability to explore and analyze student and school data in an interactive and informative manner. Users can view tables with detailed information about the selected school and examine the associated student data. This functionality supports data exploration and facilitates deeper analysis of the dataset.

    Overall, the purpose of the script is to provide a user-friendly and interactive data visualization application that enables users to gain insights into student and school data, identify patterns, and explore the relationships between schools and students.
""")
