import streamlit as st
from PIL import Image
import time
import pandas as pd
import numpy as np
import joblib
import datetime as DT
from GetModel import GetModel
import altair as alt

st.set_page_config(layout="wide")

st.markdown("<center><h2>🤖Your Customized, Real-Time Temperature Predictor.📸<small><br> Computer Science Capstone Project of Wenzhou Kean University, 2023 </small></h1>", unsafe_allow_html=True)
st.divider()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

intro = Image.open('Introduction.png')
st.image(intro,width=1760)
st.divider()

# update vars
col1, col2, col3, = st.columns([1, 1.7, 1])
all_ave_t = []
all_high_t = []
all_low_t = []
all_rainfall = []
winds = []
humids = []

with col1:
   st.subheader("🔴 Arduino Input")
   st.dataframe(pd.read_csv('updateDate.csv').tail(9))

with col2:
    st.subheader("🟠 Prediction Results")
    colA, colB, colC, colD = st.columns([1.3, 1, 1, 1])

    r = GetModel()
    st.write("Mean Absolute Error (MAE):",r[0])
   
    model = joblib.load('Model.pkl')
    preds = model.predict(r[1])


    for a in range(1, 6):
        #Date
        today = DT.datetime.now()
        time = (today + DT.timedelta(days=a)).date()
        showDate = str(time.year) + '/' + str(time.month) + '/' + str(time.day)
        colA.metric("Date", showDate)
        with colA:
            st.write(" ")

        # Temperature
        showTemperature = "{:.2f} °C".format(0.5*(preds[a][0] + preds[a][1]))
        deltaTem = 0.5 * (preds[a][0] + preds[a][1]) - 0.5 * (preds[a-1][0] + preds[a-1][1])
        deltaTem_str = "{:.2f} °C".format(deltaTem)
        all_high_t.append(preds[a][0])
        all_low_t.append(preds[a][1])
        colB.metric("Temperature", showTemperature, deltaTem_str)

        # Wind
        wind = np.random.uniform(1.35, 1.62)
        showWind = "{:.2f} mph".format(wind)
        winds.append(wind)
        if a==1:
            deltaWind = winds[a-1]
        else:
            deltaWind = winds[a-1] - winds[a-2]
        deltaWind_str = "{:.2f} °C".format(deltaWind)
        colC.metric("Wind", showWind, deltaWind_str) 

        #Humidity
        humid = np.random.uniform(77, 85)
        showHumid = "{:.2f}%".format(humid)
        humids.append(humid)
        if a==1:
            deltaHumid = humids[a-1]
        else:
            deltaHumid = humids[a-1] - humids[a-2]
        deltaHumid_str = "{:.2f} °C".format(deltaHumid)
        colD.metric("Humidity", showHumid, deltaHumid_str)

   

with col3:
    st.subheader("🟡 Visualization")
    # Sample data
    all_high_t = [30, 32, 35, 28, 33, 31]
    all_low_t = [20, 22, 18, 19, 21, 23]
    temp = {"high_t": all_high_t, "low_t": all_low_t}

    # Creating a DataFrame from the data
    data = pd.DataFrame(temp)
    data['day'] = range(0, 6)
    data = data.melt('day', var_name='Temperature Type', value_name='Temperature (°C)')

    # Registering a custom theme
    def custom_theme():
        return {
            'config': {
                'view': {'continuousWidth': 400, 'continuousHeight': 500},
                'axis': {'labelFontSize': 12, 'titleFontSize': 16},
                'legend': {'labelFontSize': 12, 'titleFontSize': 16},
                'title': {'fontSize': 20}
            }
        }

    alt.themes.register('custom_theme', custom_theme)
    alt.themes.enable('custom_theme')

    # Creating the Altair chart
    lines = alt.Chart(data).mark_line().encode(
        x=alt.X('day:Q', title='Days After Today'),
        y=alt.Y('Temperature (°C):Q'),
        color=alt.Color('Temperature Type:N', scale=alt.Scale(range=['darkred', 'lightcoral']), legend=alt.Legend(title='Temperature Type', orient='bottom')),
    )

    points = alt.Chart(data).mark_point().encode(
        x=alt.X('day:Q'),
        y=alt.Y('Temperature (°C):Q'),
        color=alt.Color('Temperature Type:N', scale=alt.Scale(range=['darkred', 'lightcoral']), legend=None)
    )

    chart = alt.layer(lines, points)

    st.title("Let's See!")
    st.altair_chart(chart)







quotes = [
    "“Red sky at night, sailors delight. Red sky in morning, sailors take warning.”",
    "“The higher the clouds, the finer the weather.”",
    "“Clear Moon, frost soon.”",
    "“When clouds appear like towers, the Earth is refreshed by frequent showers.”",
    "“Rainbow in the morning gives you fair warning.”",
    "“Rain foretold, long last. Short notice, soon will pass.”"
]

container = st.container()
with container:
    current_quote = st.empty()

    #update quotes
    while True:
        for quote in quotes:
            current_quote.markdown(
                f'<p style="text-align: center; font-size: 40px;">{quote}</p>', unsafe_allow_html=True
            )
            T.sleep(4)

