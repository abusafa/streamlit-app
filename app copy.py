# import pandas as pd
import streamlit as st
# import plotly.express as px
# import matplotlib.pyplot as plt
# import pydeck as pdk
# st.set_page_config(layout="wide")

# df_students = pd.DataFrame()
# df_schools = pd.DataFrame()
# df_students_schools = pd.DataFrame()
# df_students_schools_routes = pd.DataFrame()

# @st.cache_data
# def load_data(uploaded_file):
#     return pd.read_csv(uploaded_file)

# uploaded_file_students, uploaded_file_schools, uploaded_file_students_schools, uploaded_file_students_schools_routes = st.columns(4)

# with uploaded_file_students:
#     uploaded_file_students = st.file_uploader("Choose a students CSV file", type="csv")

# with uploaded_file_schools:
#     uploaded_file_schools = st.file_uploader("Choose a schools CSV file", type="csv")

# with uploaded_file_students_schools:
#     uploaded_file_students_schools = st.file_uploader("Choose a students_schools CSV file", type="csv")

# with uploaded_file_students_schools_routes:
#     uploaded_file_students_schools_routes = st.file_uploader("Choose a students_schools_routes CSV file", type="csv")

# if uploaded_file_students is not None:
#     df_students = load_data(uploaded_file_students)
#     st.write("Students Data")

# if uploaded_file_schools is not None:
#     df_schools = load_data(uploaded_file_schools)

# if uploaded_file_students_schools is not None:
#     df_students_schools = load_data(uploaded_file_students_schools)

# if uploaded_file_students_schools_routes is not None:
#     df_students_schools_routes = load_data(uploaded_file_students_schools_routes)



# if uploaded_file_schools is not None and st.checkbox('Show schools data'):
#     st.subheader('Raw data')
#     st.write(df_schools.head(100))

# if uploaded_file_students is not None and st.checkbox('Show students data'):
#     st.subheader('Raw data')
#     st.write(df_students.head(100))

# if uploaded_file_students_schools is not None and st.checkbox('Show students_schools data'):
#     st.subheader('Raw data')
#     st.write(df_students_schools.head(100))
#     st.subheader('Pie Chart: Count by Distance Category')
#     distance_counts = df_students_schools['distanceCategoryLabel'].value_counts().reset_index()
#     distance_counts.columns = ['distanceCategoryLabel', 'count']
#     fig = px.pie(distance_counts, names='distanceCategoryLabel', values='count', title='Count by Distance Category')
#     st.plotly_chart(fig)

#     st.subheader('Pivot Table: Administration Row Counts for Each Distance Category')
#     pivot_table = df_students_schools.pivot_table(index='administration', columns='distanceCategoryLabel', aggfunc='size', fill_value=0)
#     st.write(pivot_table)

#     selected_administration = st.selectbox(
#         'Select Administration',
#         df_students_schools['administration'].unique()
#     )

#     selected_school = st.selectbox(
#         'Select School',
#         df_students_schools[df_students_schools['administration'] == selected_administration]['school'].unique()
#     )

#     school_data = df_students_schools[(df_students_schools['administration'] == selected_administration) & (df_students_schools['school'] == selected_school)]

#     # Create the arc layer
#     arc_layer = pdk.Layer(
#         "ArcLayer",
#         data=school_data,
#         get_source_position=["longitude_right", "latitude_right"],
#         get_target_position=["longitude", "latitude"],
#         get_source_color=[0, 128, 200],
#         get_target_color=[200, 0, 80],
#         auto_highlight=True,
#         width_scale=1.5,
#         get_width="outbound",
#         pickable=True,
#     )

#     # Set the viewport location
#     view_state = pdk.ViewState(
#         latitude=school_data["latitude_right"].mean(),
#         longitude=school_data["longitude_right"].mean(),
#         zoom=15,
#         pitch=50,
#     )

#     # Render the deck.gl map
#     r = pdk.Deck(
#         layers=[arc_layer],
#         initial_view_state=view_state,
#         tooltip={
#             "text": """
# المدرسة: {school}
# الطالب: {studentName}
# {distance_km} km
# {distanceCategoryLabel}
# """
#         },
#     )

#     st.pydeck_chart(r)





# if uploaded_file_students_schools_routes is not None and st.checkbox('Show students_schools_routes data'):
#     st.subheader('Raw data')
#     st.write(df_students_schools_routes.head(100))


# st.button("rerun")
