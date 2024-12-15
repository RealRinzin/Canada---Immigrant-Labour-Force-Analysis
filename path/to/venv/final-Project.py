from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
# import plotly.graph_objs as go
import plotly.graph_objects as go
import plotly.io as pio
# Bootstrap CSS CDN
external_stylesheets = [
    'https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'
]

# --------------------------Default setting for plot background---------------------------------------
# Defaulting settings
# Create a custom template
custom_template = {
    "layout": {
        "paper_bgcolor": "#f2e9dd",  # Chart area background
        "plot_bgcolor": "#f2e9dd",  # Plot area background
    }
}
# Set the custom template as default
pio.templates["custom"] = custom_template
pio.templates.default = "custom"

# --------------------------End Default setting for plot background---------------------------------------

app = Dash(__name__, external_stylesheets=external_stylesheets,title='Canada - Immigrant Analytics Dashboard')

# data fetch
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
df = pd.read_csv('./Immigrant-data.csv')
df_clean_data  = df[
    (df['immigrant_status']=='Immigrants, landed 5 or less years earlier')
    &(
    (df['labour_force_characteristics']=='Employment')|
    (df['labour_force_characteristics']=='Labour force')|
    (df['labour_force_characteristics']=='Unemployment')|
    (df['labour_force_characteristics']=='Full-time employment')|
    (df['labour_force_characteristics']=='Part-time employment')
    )
    &(df['gender'] != 'Both sexes')
    &(df['age_group'] == '15 to 24 years')
]
# year_list = [i for i in range(2000, 2013, 1)]

# --------------------------Main Container---------------------------------------
# APP Layout
app.layout = html.Div(
    style={'backgroundColor': '#e9d9c5'},
    children= [ 
html.Div(
    className="container",
    children=[
        html.Div(
            children=[
                html.Img(src="https://flagcdn.com/w80/ca.png")
            ],
            className='d-flex justify-content-center align-items-center pt-3'
        ),
        html.H3("Canada Immigrant Labour Force Market", className="text-center pt-3 text-dark"),
        html.P("Note: Age (24 - 55) | Year (2019 - 2024) ", className="text-center text-muted font-weight-bold"),
        html.Div(
            className="row d-flex justify-content-center align-items-center py-1",
            children=[
                html.Div(
                    children=[
                        dcc.Dropdown(df.year.unique(),2024, id='year-dropdown-selection',className='form-select border border-warning rounded-lg',placeholder='Select Year'),
                    ],
                    style={'backgroundColor':'#e9d9c5'},
                    className="col-md-3"
                ),
                html.Div(
                    children=[
                        dcc.Dropdown(df.gender.unique(), id='gender-dropdown-selection',className='form-select border border-warning rounded',placeholder='Gender'),
                    ],
                    className="col-md-3"
                ),
                html.Div(
                    children=[
                        dcc.Dropdown(df.labour_force_characteristics.unique(), 'Labour force', id='labour_force_characteristics-dropdown-selection',className='form-select border border-warning rounded',placeholder='Labour Force Characteristics'),
                    ],
                    className="col-md-3"
                ),
            ]
        ),

    ]
),
html.Div(
    className="container-full p-4",
    children = [
        # DROPDOWN SELECTION CONTENT AREA
        # CHAT VISUAL CONTENT AREA

        html.Div(
            className="row",
            children=[
                html.Div(
                    children = [
                        dcc.Graph(id='graph-content'),
                    ],
                    className="col-md-4",
                ),
                html.Div(
                    children = [
                        dcc.Graph(id='line-chart-gdp'),
                    ],
                    className='col-md-4',
                ),
                html.Div(
                    children = [
                        dcc.Graph(id='pie-chart-gdp',    config={'displayModeBar': False}),
                    ],
                    className="col-md-4 py-2",
                    style={'backgroundColor':'#e9d9c5','fontSize':'40px'}
                ),
                html.Div(
                    children = [
                        dcc.Graph(id='bar_part_full_emp',    config={'displayModeBar': False}),
                    ],
                    className="col-md-4 py-2",
                    style={'backgroundColor':'#e9d9c5','fontSize':'40px'}
                ),
                html.Div(
                    children = [
                        # dcc.Graph(id='pie_test_chart',    config={'displayModeBar': False}),
                    ],
                    className="col-md-4 py-2",
                    style={'backgroundColor':'#e9d9c5','fontSize':'40px'}
                ),
            ]
        ),

    ]
    )
    ],
    
)
#-------------------------- Layout END--------------------------


# Callback
@callback(
    Output('graph-content', 'figure'),
    Output('line-chart-gdp', 'figure'),
    Output('pie-chart-gdp', 'figure'),
    Output('bar_part_full_emp', 'figure'),
    # Output('pie_test_chart', 'figure'),
    Input('year-dropdown-selection', 'value'),
    Input('gender-dropdown-selection', 'value')
)



def update_graph(year,gender):
    # Data

    # Chart colors
    # colors = ['#eb862a','#277f71']
    # colors = ['#cf291e','#f7f7f7']
    colors = ['#232323','#d95f01']
    # ChartNames

    # ------------------ Total Employment vs Unemployment ------------------------------------
    # Total Labour Force
    total_labour_force = df_clean_data[
        (df_clean_data['labour_force_characteristics'] == 'Employment')|
        (df_clean_data['labour_force_characteristics'] == 'Unemployment')
    ].groupby(['year','labour_force_characteristics'])['value'].sum().reset_index()
    # Bar Chart
    bar_labour_force = px.bar(total_labour_force, 
                              x='year', 
                              y='value',
                              color='labour_force_characteristics',
                              barmode='group',
                              title="Employment Vs Unemployment Distribution",
                              text='value',
                              color_discrete_sequence=colors)
    # Update layout for better text visibility

# ------------------ Full Time and Part Time Trend Analysis ------------------------------------

    full_part_employment = df_clean_data[
        (df_clean_data['labour_force_characteristics'] == 'Full-time employment')|
        (df_clean_data['labour_force_characteristics'] == 'Part-time employment')
        ].groupby(['year','labour_force_characteristics','gender'])['value'].sum().reset_index()
    # Bar Chart
    bar_part_full_emp = px.bar(full_part_employment, 
                              x='year', 
                              y='value',
                              color='labour_force_characteristics',
                              barmode='group',
                              title="Full Time and Part Time Employment Comparison",
                              text='value',
                              color_discrete_sequence=colors)
        
    
# ------------------ Total Employment Trend ------------------------------------
    if gender:
        total_employment = df_clean_data[
            (df_clean_data['year']== year) 
            &(df_clean_data['gender']==gender)
            ].groupby(['year','gender','labour_force_characteristics'])['value'].sum().reset_index()
    else:
        total_employment = df_clean_data[df_clean_data['year']== year].groupby(['year','labour_force_characteristics','gender'])['value'].sum().reset_index()
    # Line Chart
    line_employment = px.bar(
        total_employment, 
        x='labour_force_characteristics',

        y='value',
        color='gender',
        barmode='group',
        title=f"Labour Force VS Gender Distribution-{year}",
        text='value',
        color_discrete_sequence=colors)


# ------------------ Total UNEmployment Trend ------------------------------------
    total_unemployment = df_clean_data[df_clean_data['labour_force_characteristics'] == 'Unemployment'].groupby(['year','gender'])['value'].sum().reset_index()
    # Line Chart
    line_unemployment = px.line(
        total_unemployment, 
        x='year', 
        y='value',
        color='gender',
        labels={'value': 'value', 'year': 'year'},
        title="Emply",
        text='value',
        color_discrete_sequence=colors
        )
    
# ------------------ Chart Bar Value Assigns ------------------------------------

    line_unemployment.update_layout(
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
        }
    )

    line_unemployment.update_traces(
    marker=dict(
        size=15,  # Assign marker sizes dynamically
        opacity=0.8,  # Add transparency
    )
)
    # Assigning the chart name for positioin
    chartNames = [bar_labour_force,bar_part_full_emp,line_employment]
    # Looping the function for all the chart name
    for i in range(0,len(chartNames)):
        # print(chartNames[i])
        chartNames[i].update_traces(
            textposition='outside',  # Places text outside the bars
            texttemplate='%{text:.2s}',  # Optional: Format text (e.g., shorten large numbers)
        )
    # Add X-axis and Y - Label
        chartNames[i].update_layout(
            title={
                'text':chartNames[i]['layout']['title'].text,  # Chart title
                'font': {'size': 16, 'weight': 'bold'},  # Title font size and weight
                'x': 0.5                              # Center align the title
            },
            xaxis_title={
                "text":"Year" if i==0 else "Year" if i==1 else 'Labour Force Characteristics',
                'font':{'size': 14,'weight': 'bold'}  
            },  # Change x-axis label text
            yaxis_title={
                'text':"Number of People",
                'font':{'size': 14,'weight': 'bold'}  
            },
            # Change y-axis label text
            legend=dict(
                title="Labour Force Characteristics",  # Add title to the legend
                orientation="h",  # Horizontal orientation
                x=0.5,  # Center the legend horizontally
                xanchor="center",
                y=1.1  # Position above the chart
            )
        )
    return bar_labour_force,line_employment,line_unemployment,bar_part_full_emp
if __name__ == '__main__':
    app.run(port=8090,debug=True)