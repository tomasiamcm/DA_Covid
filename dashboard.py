from sys import displayhook
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

df = pd.read_csv("HIST_PAINEL_COVIDBR_2020_Parte1_19set2022.csv", sep=";")
df_states = df[(~df["estado"].isna()) & (df["codmun"].isna())]
print(df_states)

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
#fig = px.choropleth_mapbox(df_states, )

# ------------------------- LAYOUT -------------------------

# Grafico de barras
#graph1 = go.Figure()
#graph1.add_trace(go.Scatter(x=df_states["data"], y=df_states[""]))
