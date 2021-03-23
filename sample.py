import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("coronanet.csv")

my_page = st.sidebar.radio('Page Navigation', ['page 1', 'page 2', 'page 3'])

if my_page == 'page 1':
    # st.write tells streamlit to write the content in the web app.
    st.title("Data")
    st.header("COVID-19 Policies obtained from CoronaNet")

    data_load_state = st.text('Loading data...')
    st.write(df.head())

    if st.checkbox('Show data', value=False):
        top10 = df.head(10)
        top10

    data_load_state.markdown('Loading data...**done!**')

elif my_page == 'page 2':
    tests = (df[df["total_tests"]>0.0].groupby('country')["new_tests"].sum()
                                      .to_frame()
                                      .sort_values(by="new_tests", ascending=False))
    tests = tests.head(10)

    fig = plt.figure(figsize=(12,6)) 

    st.header("Countries Visualized")
    # the main code to create the graph
    plt.barh(tests.index, tests["new_tests"]) 

    # additional elements that can be customzed
    plt.title("Top 10 Countries with Most Number of People Vaccinated", fontsize=16)
    plt.xlabel("Number of People", fontsize=12)
    plt.gca().invert_yaxis()

    # display graph
    plt.show()
    st.pyplot(fig)
    
elif my_page == 'page 3':
    #Create dropdown box
    option = st.sidebar.selectbox(
        'Which country do you want to see?',
         df['country'].unique())

    'You selected: ', option

    # Filter the entry in the plot
    country_stats = (df[df["country"]==option].groupby("country")
                    [["confirmed_cases", "deaths", "recovered"]].sum())
    stats = country_stats.T

    fig = plt.figure(figsize=(8,4)) 
    plt.bar(stats.index, stats[option])
    plt.show()
    st.pyplot(fig)