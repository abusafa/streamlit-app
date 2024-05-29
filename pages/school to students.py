import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pydeck as pdk
st.set_page_config(layout="wide")

@st.cache_data
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)


df_students_schools = load_data("https://s3.tatweertransit.com/uploads/students_schools.csv")



distance_counts = df_students_schools['distanceCategoryLabel'].value_counts().reset_index()
distance_counts.columns = ['distanceCategoryLabel', 'count']
fig = px.pie(distance_counts, names='distanceCategoryLabel', values='count', title='Count by Distance Category')

with st.container(border=False):
    st.markdown("""# Schools to Students
        """)

pivot_table = df_students_schools.pivot_table(index='administration', columns='distanceCategoryLabel', aggfunc='size', fill_value=0)
# st.write(pivot_table)
with st.container(border=True):
    col11, col22 = st.columns([1,1])
    with col11:
        st.subheader('Pie Chart: Count by Distance Category')
        st.plotly_chart(fig)
    with col22:
        st.subheader('Pivot Table: Administration Row Counts for Each Distance Category')
        st.write(pivot_table)



with st.container(border=True):
    col1, col2 = st.columns([1,4])
    with col1:
        selected_administration = st.selectbox(
            'Select Administration',
            df_students_schools['administration'].unique()
        )
        selected_school = st.selectbox(
            'Select School',
            df_students_schools[df_students_schools['administration'] == selected_administration]['school'].unique()
        )
        school_data = df_students_schools[(df_students_schools['administration'] == selected_administration) & (df_students_schools['school'] == selected_school)]




    # Create the arc layer
    arc_layer = pdk.Layer(
        "ArcLayer",
        data=school_data,
        get_source_position=["longitude_right", "latitude_right"],
        get_target_position=["longitude", "latitude"],
        get_source_color=[0, 128, 200],
        get_target_color=[200, 0, 80],
        auto_highlight=True,
        width_scale=1.5,
        get_width="outbound",
        pickable=True,
    )

    # Set the viewport location
    view_state = pdk.ViewState(
        latitude=school_data["latitude_right"].mean(),
        longitude=school_data["longitude_right"].mean(),
        zoom=14,
        pitch=50,
    )

    # Render the deck.gl map
    r = pdk.Deck(
        layers=[arc_layer],
        initial_view_state=view_state,
        tooltip={
            "text": """
    المدرسة: {school}
    الطالب: {studentName}
    {distance_km} km
    {distanceCategoryLabel}
    """
        },
    )
    with col2:
        st.pydeck_chart(r)


with st.container(border=True):
    st.subheader('Students data for selected school:')
    # show school data
    st.write(school_data)
