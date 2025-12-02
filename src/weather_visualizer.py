import matplotlib
matplotlib.use("Agg")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "weather.csv")
IMG_DIR = os.path.join(BASE_DIR, "images")

def load_data():
    return pd.read_csv(CSV_PATH, parse_dates=['date'])

def clean_data(df):
    df=df.dropna()
    df=df[['date','temperature','rainfall','humidity']]
    df=df.sort_values('date')
    return df

def stats(df):
    return df.describe()

def plots(df):
    # Daily temperature
    plt.figure(figsize=(10,4))
    plt.plot(df['date'], df['temperature'])
    plt.savefig(os.path.join(IMG_DIR,"daily_temperature.png")); plt.close()

    # Monthly rainfall
    monthly=df.groupby(df['date'].dt.month)['rainfall'].sum()
    plt.figure(figsize=(10,4))
    plt.bar(monthly.index, monthly.values)
    plt.savefig(os.path.join(IMG_DIR,"monthly_rainfall.png")); plt.close()

    # Humidity vs temperature
    plt.figure(figsize=(8,4))
    plt.scatter(df['temperature'], df['humidity'])
    plt.savefig(os.path.join(IMG_DIR,"humidity_vs_temperature.png")); plt.close()

    # Combined plot
    plt.figure(figsize=(12,4))
    plt.subplot(1,2,1)
    plt.plot(df['date'], df['temperature'])
    plt.subplot(1,2,2)
    plt.scatter(df['temperature'], df['humidity'])
    plt.savefig(os.path.join(IMG_DIR,"combined_plot.png")); plt.close()

def save_clean(df):
    df.to_csv(os.path.join(BASE_DIR,"data","cleaned_weather.csv"), index=False)

def main():
    df=load_data()
    df=clean_data(df)
    stats(df)
    plots(df)
    save_clean(df)
    print("Processing complete")

if __name__=="__main__":
    main()
