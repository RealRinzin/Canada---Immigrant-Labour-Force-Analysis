from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# import plotly.graph_objs as go
import plotly.graph_objects as go
import plotly.io as pio

# Data Frame
df = pd.read_csv("./clean_immigrant_data.csv")
#
check = (
    df[df["labour_force_character"] == "Labour force"]
    .groupby(["year", "gender"])["total"]
    .sum()
    .reset_index()
)
age_group = (
    df[(df["labour_force_character"] == "Labour force") & (df["year"] == 2020)]
    .groupby(["gender", "age_group"])["total"]
    .sum()
    .reset_index()
)
