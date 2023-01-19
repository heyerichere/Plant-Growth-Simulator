'''graph.py
12/10/2022
CS151 F22  Final project
Eric Appiah'''


import matplotlib.pyplot as plt
import pandas as pd
import graphicsPlus as gr


def graph():
    '''graphs the data set'''
    df = pd.read_csv('carbon_emission_in_africa.csv', delimiter=',')
    plt.figure(figsize=(5,8))
    plt.plot(df['Year'], df['Annual CO2 emission'], color = "SaddleBrown", lw = 0.5)
    plt.xlabel("Years")
    plt.ylabel("Carbon dioxide emission")
    plt.fill_between(df['Year'], 0, df['Annual CO2 emission'], facecolor = 'SaddleBrown')
    plt.show()