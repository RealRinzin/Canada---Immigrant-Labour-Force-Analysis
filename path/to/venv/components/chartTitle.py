from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
# import plotly.graph_objs as go
import plotly.graph_objects as go
import plotly.io as pio

# ------------------ Bar Chart | Title & Axis - Customization ------------------
def BarChartTitle(name,title):
    name.update_layout(
                title={
                    'text':title,
                    'font': {'size': 16, 'weight': 'bold'},  # Title font size and weight
                    'x': 0.5                              # Center align the title
                },
                xaxis_title={
                    "text":'Year',
                    'font':{'size': 14,'weight': 'bold'}  
                },  # Change x-axis label text
                yaxis_title={
                    'text':"Total Population",
                    'font':{'size': 14,'weight': 'bold'}  
                },
                # Change y-axis label text
                legend=dict(
                    title="Labour Force Characteristics",  # Add title to the legend
                    orientation="h",  # Horizontal orientation
                    x=0.5,  # Center the legend horizontally
                    xanchor="center",
                    y=1.1  # Position above the chart
                ),
                yaxis_tickformat="d"
        )
    name.update_traces(
        textposition='outside',  # Places text outside the bars
        texttemplate='%{text:.2s}',  # Optional: Format text (e.g., shorten large numbers)
    )

# ------------------ Line Chart | Title & Axis - Customization ------------------

def LineChartTitle(name):
    name.update_layout(
        title={
            "text": "Unemployment Trend Line",
            "x": 0.5,
            "xanchor": "center",
            "font": {"size": 16, "weight": "bold"}
        },
        xaxis={
            "title": {"text": "Years", "font": {"size": 14, "weight": "bold"}},
            # "tickfont": {"size": 14, "weight": "bold"}
        },
        yaxis={
            "title": {"text": "Total Population ", "font": {"size": 14, "weight": "bold"}},
            # "tickfont": {"size": 14, "weight": "bold"}
        },
        yaxis_tickformat="d"
    )
    name.update_traces(
        marker=dict(
            size=15,  # Assign marker sizes dynamically
            opacity=0.8,  # Add transparency
        )
    )
