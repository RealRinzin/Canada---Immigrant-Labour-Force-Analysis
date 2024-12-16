import dash
from dash import dcc, html
import plotly.graph_objs as go

# Sample Data
x_data = [1, 2, 3, 4, 5]
y_data = [10, 15, 13, 17, 20]

# Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='line-chart',
        figure={
            'data': [
                go.Scatter(
                    x=x_data,
                    y=y_data,
                    mode='lines',  # Line chart
                    line={'width': 4, 'color': 'blue'},  # Increase line thickness and set color
                    name='Sample Line'
                )
            ],
            'layout': {
                'title': 'Line Chart with Increased Thickness',
                'xaxis': {'title': 'X-axis'},
                'yaxis': {'title': 'Y-axis'}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True,port=9000)
