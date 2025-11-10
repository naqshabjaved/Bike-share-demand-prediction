import streamlit as st
import pandas as pd
import joblib
import datetime

try:
    model = joblib.load('bike_model.pkl')
    model_columns = joblib.load('model_columns.pkl')
except FileNotFoundError:
    st.error("Model files not found. Please run the notebook to generate 'bike_model.pkl' and 'model_columns.pkl'.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

st.set_page_config(page_title="Bike Share Demand Prediction", layout="wide")
st.title('🚲 Bike Share Demand Prediction')
st.write("This app predicts the daily count of shared bike rentals based on environmental and seasonal factors.")

col1, col2 = st.columns(2)

with col1:
    st.header("🗓️ Date & Season")
    d = st.date_input("Select a Date", datetime.date(2019, 7, 6))
    
    year = d.year
    month = d.month
    weekday = d.weekday()
    
    yr = 1 if year == 2019 else 0  
    
    season_map = {1:1, 2:1, 3:2, 4:2, 5:2, 6:3, 7:3, 8:3, 9:4, 10:4, 11:4, 12:1}
    season = season_map[month]
    
    holiday = st.selectbox('Holiday?', (0, 1), format_func=lambda x: 'Yes' if x == 1 else 'No')
    workingday = st.selectbox('Working Day?', (0, 1), format_func=lambda x: 'Yes' if x == 1 else 'No')

with col2:
    st.header("☀️ Weather Conditions")
    weathersit = st.selectbox('Weather Situation', (1, 2, 3), 
                              format_func=lambda x: {
                                  1: '1: Clear/Few clouds',
                                  2: '2: Mist/Cloudy',
                                  3: '3: Light Snow/Rain'
                              }[x])
    
    temp = st.slider('Temperature (°C)', min_value=0.0, max_value=40.0, value=25.0, step=0.1)
    hum = st.slider('Humidity (%)', min_value=0.0, max_value=100.0, value=60.0, step=0.1)
    windspeed = st.slider('Windspeed (km/h)', min_value=0.0, max_value=70.0, value=10.0, step=0.1)

if st.button('Predict Demand', type="primary", use_container_width=True):
    input_data = {
        'yr': yr,
        'holiday': holiday,
        'workingday': workingday,
        'temp': temp,
        'hum': hum,
        'windspeed': windspeed,
        'season': season,
        'weathersit': weathersit,
        'weekday': weekday,
        'month': month
    }
    
    input_df = pd.DataFrame([input_data])
    
    categorical_cols = ['season', 'weathersit', 'weekday', 'month']
    input_df_processed = pd.get_dummies(input_df, columns=categorical_cols, drop_first=False) # Keep drop_first=False for reindexing
    
    input_df_aligned = input_df_processed.reindex(columns=model_columns, fill_value=0)
    
    try:
        prediction = model.predict(input_df_aligned)
        predicted_count = int(prediction[0])
        
        st.success(f"**Predicted Bike Rentals:** `{max(0, predicted_count)}`") # Ensure prediction is not negative
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")