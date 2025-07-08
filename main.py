import streamlit as st
import plotly.express as px



st.title("weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days that you want to Forecast")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

def get_data(days):
    fake_dates = ["2024-03-07", "2024-04-07", "2024-05-07"]
    fake_temperatures = [33, 34, 28]
    fake_temperatures =[days * i for i in fake_temperatures]
    return fake_dates, fake_temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date","y":"Temparature (C)" })
st.plotly_chart(figure)