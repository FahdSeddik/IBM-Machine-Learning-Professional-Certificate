import streamlit as st
import pandas as pd

#1. Create a streamlit title widget, this will be shown first
st.title("This is a sample app")
#2. Then create a streamlit title widget, this will be shown after title
button1 = st.button("Click to show a dataframe")
print(button1)
if button1:
    df = pd.DataFrame({
    'column1': [1, 2, 3, 4],
    'column2': [10, 20, 30, 40]
    })
    # Show the Pandas dataframe using st.dataframe() method
    st.dataframe(df)
    # Visualize the column1 series using st.line_chart() method
    st.line_chart(df['column1'])

#3. Create two streamlit slider widget for receiving a numerical value input
slider1 = st.slider("Slider1", min_value=1, max_value=10, value=1)
print(slider1)
slider2 = st.slider("Slider2", min_value=1, max_value=10, value=2)
print(slider2)

#4. Create a streamlit text widget to show the sum result of two slider values
# Create a streamlit subheader widget
st.subheader("The sum of slider1 and slider2 is: ")
st.text(slider1 + slider2)