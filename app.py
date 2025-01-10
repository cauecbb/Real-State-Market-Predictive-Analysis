import pandas as pd
import streamlit as st

dataset = pd.read_csv('data/ZHVI-NY-dataset.csv')

print(dataset.head())