import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
import pydeck as pdk
from PIL import Image
import cv2
import io

st.set_page_config(page_title="Streamlit Comprehensive Demo 🚀", page_icon="📝", layout="wide")

def main():
    st.title("🎨 Streamlit Comprehensive Showcase")
    st.markdown("Explore the various features of Streamlit in this interactive demo!")

    # Sidebar for navigation
    demo_type = st.sidebar.selectbox(
        "Choose a Demo",
        ["Basic Elements", "Data Visualization", "Interactive Widgets", "Advanced Features"]
    )

    if demo_type == "Basic Elements":
        show_basic_elements()
    elif demo_type == "Data Visualization":
        show_data_visualization()
    elif demo_type == "Interactive Widgets":
        show_interactive_widgets()
    elif demo_type == "Advanced Features":
        show_advanced_features()

def show_basic_elements():
    st.header("1. Basic Elements")

    st.subheader("1.1 Text Elements")
    st.text("This is simple text")
    st.markdown("This is **markdown** with _styling_")
    st.latex(r"\begin{pmatrix}a & b \\ c & d\end{pmatrix}")

    st.subheader("1.2 Data Display")
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    st.dataframe(df)
    st.table(df)
    st.json({"foo": "bar", "baz": "boz"})

    st.subheader("1.3 Media Elements")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)
    st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg")
    st.video("https://youtu.be/B2iAodr0fOo")

def show_data_visualization():
    st.header("2. Data Visualization")

    @st.cache_data
    def load_data():
        return pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])

    data = load_data()

    st.subheader("2.1 Streamlit Charts")
    st.line_chart(data)
    st.area_chart(data)
    st.bar_chart(data)

    st.subheader("2.2 Altair Chart")
    chart = alt.Chart(data).mark_circle().encode(
        x='A', y='B', size='C', color='C', tooltip=['A', 'B', 'C'])
    st.altair_chart(chart, use_container_width=True)

    st.subheader("2.3 Plotly Chart")
    fig = px.scatter(data, x="A", y="B", size="C", color="C")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("2.4 PyDeck Chart")
    chart_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(latitude=37.76, longitude=-122.4, zoom=11, pitch=50),
        layers=[pdk.Layer('HexagonLayer', data=chart_data, get_position='[lon, lat]', radius=200, elevation_scale=4, elevation_range=[0, 1000], pickable=True, extruded=True)]
    ))

def show_interactive_widgets():
    st.header("3. Interactive Widgets")

    st.subheader("3.1 Input Widgets")
    text_input = st.text_input("Enter some text")
    number = st.number_input("Enter a number", min_value=0, max_value=100)
    date = st.date_input("Pick a date")

    st.subheader("3.2 Selection Widgets")
    option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
    options = st.multiselect("Choose multiple options", ["A", "B", "C", "D"])
    slider_val = st.slider("Pick a number", 0, 100)

    st.subheader("3.3 Button and Download")
    if st.button("Click me!"):
        st.write("Button clicked!")

    @st.cache_data
    def get_sample_data():
        return pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    csv = get_sample_data().to_csv(index=False)
    st.download_button("Download CSV", csv, "sample_data.csv", "text/csv")

def show_advanced_features():
    st.header("4. Advanced Features")

    st.subheader("4.1 Layouts")
    col1, col2 = st.columns(2)
    with col1:
        st.write("This is column 1")
    with col2:
        st.write("This is column 2")

    with st.expander("Click to expand"):
        st.write("This content is hidden by default")

    st.subheader("4.2 Progress and Status")
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
    st.success("This is a success message!")
    st.error("This is an error message!")
    st.warning("This is a warning message!")
    st.info("This is an info message!")

    st.subheader("4.3 Cache and Performance")
    @st.cache_data
    def expensive_computation(a, b):
        return a * b

    result = expensive_computation(2, 21)
    st.write(f"2 * 21 is {result}")

    st.subheader("4.4 Session State")
    if 'count' not in st.session_state:
        st.session_state.count = 0

    if st.button('Increment'):
        st.session_state.count += 1

    st.write('Count = ', st.session_state.count)

    st.subheader("4.5 Forms")
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
        submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Slider", slider_val, "Checkbox", checkbox_val)

    st.subheader("4.6 Popover")
    with st.popover("Click for Popover"):
        st.write("This is a popover")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)

if __name__ == "__main__":
    main()