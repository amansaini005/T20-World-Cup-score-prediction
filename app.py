
import streamlit as st
import pickle
import pandas as pd
import numpy as np




st.title('T20 World Cup 1st Inning score Predictor')

teams = ['Ireland', 'Afghanistan', 'Bangladesh', 'Zimbabwe', 'Australia',
       'South Africa', 'Netherlands', 'England', 'West Indies',
       'Pakistan', 'United Arab Emirates', 'Scotland', 'New Zealand',
       'India', 'Oman', 'Sri Lanka', 'Papua New Guinea']

cities = ['Derry', 'Dehra Dun', 'Rajkot', 'Harare', 'Barbados',
       'Johannesburg', 'Chittagong', 'Dubai', 'Mirpur', 'Abu Dhabi',
       'Perth', 'Sylhet', 'London', 'Cape Town', 'Mount Maunganui',
       'Pallekele', 'King City', 'Canberra', 'Edinburgh', 'Durban',
       'Melbourne', 'Al Amarat', 'Kanpur', 'Manchester', 'Nagpur',
       'Hambantota', 'Christchurch', 'Basseterre', 'Mumbai', 'Lucknow',
       'Birmingham', 'Colombo', 'Pune', 'The Hague', 'Bready', 'Brisbane',
       'Greater Noida', 'Delhi', 'Centurion', 'Sydney', 'Karachi',
       'Dublin', 'Amstelveen', 'Nottingham', 'Sharjah', 'Auckland',
       'Kolkata', 'Lahore', 'Southampton', 'Port Elizabeth', 'Wellington',
       'Khulna', 'Chandigarh', 'Dominica', 'Bulawayo', 'St Lucia',
       'Dhaka', 'Bengaluru', 'Cuttack', 'Nelson', 'Deventer', 'St Kitts',
       'Adelaide', 'Lauderhill', 'Kandy', 'Dharamsala', 'Hamilton',
       'Chennai', 'Guyana', 'Jamaica', 'Napier', 'Kimberley', 'Bangalore',
       'Ahmedabad']

pipe = pickle.load(open('my_pipeline.pkl', 'rb'))

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select batting_team ", sorted(teams))

with col2:
    bowling_team = st.selectbox("Select bowling_team ", sorted(teams))

city = st.selectbox("Select city", sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
       current_score = st.number_input("current score")

with col4:
       overs = st.number_input('Overs done(Works for over > 5)')

with col5:
       wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
       ball_left = 120 - overs * 6
       wicket_left = 10 - wickets
       crr = current_score / overs

       input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team],
                                'city': [city], 'current_score': [current_score],
                                'ball_left': [ball_left], 'wicket_left': [wicket_left],
                                'crr': [crr], 'last_five': [last_five]})
       result = pipe.predict(input_df)
       st.header("Predict Score  " + str(int(result)))


