from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
# import plotly.graph_objs as go
import plotly.graph_objects as go
import plotly.io as pio


# --------------------------IMPORT COMPONENTS---------------------------------------
import components.Dashboard as Dashboard # Main Dashboard
import components.dropdown  as dropdown  # Dropdown List
import components.chartTitle as title    # Custom Chart Title, Axis 
import components.Query as query       # Query parameter
import components.barChart as Bar
# --------------------------Bootstrap CSS---------------------------------------
css= ['https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

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


# --- Variables
data = {
    "Categories": ["Category A", "Category B", "Category C", "Category D"],
    "Values": [25, 35, 20, 20],
}
# -- Assigning Dashboard color theme
# Chart colors
# colors = ['#eb862a','#277f71']
# colors = ['#cf291e','#f7f7f7']
colors = ['#d95f01','#232323','#eb862a','#277f71','#565656']
# --------------------------App Initialization---------------------------------------

# App Initialization
app = Dash(__name__, external_stylesheets=css,title='Canada - Immigrant Analytics Dashboard')

# App Layout Design---------------------------------------
app.layout = html.Div(
    style={'background':'#e9d9c5'},
    children= [
        html.Div(
            className="container",
            children=[
                html.Div(
                    children=[
                        html.Img(src="https://flagcdn.com/w80/ca.png"),
                    ],
                    className='d-flex justify-content-center align-items-center pt-3'
                ),
                html.H3("Canada Immigrant Labour Force Market", className="text-center pt-3 text-dark"),
                html.H4("Analysis & Trend", className="text-center text-muted"),
                html.P("Note: Age (24 - 55) | Year (2019 - 2024) ", className="text-center text-muted font-weight-bold"),
                #--Row Class Drop Down--
                html.Div(
                    className="row",
                    children=[
                        # Year
                        html.Div(
                            children=[
                                dcc.Dropdown(dropdown.immigrantStatusList, id='immigrantStatus-selection',placeholder='Select Immigrant Status'),
                            ],
                            style={'backgroundColor':'#e9d9c5'},
                            className="col-md-2"
                        ),
                        # Provinces
                        html.Div(
                            children=[
                                dcc.Dropdown(dropdown.genderList, id='gender-selection',placeholder='Select Gender'),
                            ],
                            style={'backgroundColor':'#e9d9c5'},
                            className="col-md-2"
                        ),
                        # Labour Status
                        html.Div(
                            children=[
                                dcc.Dropdown(dropdown.yearList, 2024, id='year-selection',placeholder='Select Year'),
                            ],
                            style={'backgroundColor':'#e9d9c5'},
                            className="col-md-2"
                        ),
                        
                        # Age Group
                        html.Div(
                            children=[
                                dcc.Dropdown(dropdown.labourList, id='labour-selection',placeholder='Select Labour'),
                            ],
                            style={'backgroundColor':'#e9d9c5'},
                            className="col-md-2"
                        ),
                        # Gender
                        html.Div(
                            children=[
                                dcc.Dropdown(dropdown.ageGroupList, 'Canada', id='ageGroup-selection',placeholder='Select Age Group'),
                            ],
                            style={'backgroundColor':'#e9d9c5'},
                            className="col-md-2"
                        ),
                    ]
                ),
            ]
        ),

# --- DATA VISUALIZATION AREA
        html.Div(
            className="container-full p-4",
            children= [
                html.Div(
                    className="row",
                    children= [
                        html.Div(
                            className="col-md-4",
                            children=[
                                dcc.Graph(id='gender-content')
                            ]
                        ),
                        html.Div(
                            className="col-md-4",
                            children=[
                                dcc.Graph(id='age-content')
                            ]
                        ),
                        html.Div(
                            className="col-md-4",
                            children=[
                                dcc.Graph(id='labour-content')
                            ]
                        )
                    ]
                ),
# ------------------New Row----------------------
                html.Div(
                    className="row py-3",
                    children= [
                        html.Div(
                            className="col-md-6",
                            children=[
                                dcc.Graph(id='age_group-content')
                            ]
                        ),
                        html.Div(
                            className="col-md-6",
                            children=[
                                dcc.Graph(id='line-content')
                            ]
                        )
                    ]
                ),
# ------------------New Row----------------------
                html.Div(
                    className="row py-3",
                    children= [
                        html.Div(
                            className="col-md-6",
                            children=[
                                # dcc.Graph(id='age_group-content')
                            ]
                        ),
                        html.Div(
                            className="col-md-4",
                            children=[
                                dcc.Graph(id='pie-content')
                            ]
                        ),
                        html.Div(
                            className="col-md-6",
                            children=[
                                # dcc.Graph(id='line-content')
                            ]
                        )
                    ]
                ),
            ]
        )
    ]
)

# --------------------------CALL BACK FUNCTIONS---------------------------------------

@callback(
    Output('gender-content', 'figure'),
    Output('age-content', 'figure'),
    Output('labour-content', 'figure'),
    Output('age_group-content', 'figure'),
    Output('pie-content', 'figure'),
    Output('line-content', 'figure'),

    # Input
    Input('gender-selection', 'value'),
    Input('year-selection', 'value'),
    Input('labour-selection', 'value'),
    Input('ageGroup-selection', 'value'),
    Input('immigrantStatus-selection', 'value')
    
)
# --------------------------UPDATE FUNCTIONS---------------------------------------
def update_graph(gender,year,labour,age_group,immigrantStatus):
    # Return Values
    result = query.yearFun(year)
    dff = Dashboard.check
    # Check
    bar_employment = Bar.test(year,colors)
    age_employment = Bar.ageGroup(year,colors)
# --------New Code-------
    # bar_employment = px.bar(
    #     dff, 
    #     x='year',
    #     y='total',
    #     color='gender',
    #     barmode='group',
    #     title=f"Total Labour Force Participation with Gender Distribution",
    #     text='total',
    #     color_discrete_sequence=colors)
    # Chart
    # age_employment = px.bar(
    #     result, 
    #     x='age_group',
    #     y='total',
    #     color='gender',
    #     barmode='group',
    #     title=f"Age Group and Gender Distribution- {year}",
    #     text='total',
    #     color_discrete_sequence=colors)

    # Labour force participation
    labour_force = px.bar(
        query.main_labour_force_participation, 
        x='year',
        y='total',
        color='labour_force_character',
        barmode='group',
        title=f"Labour Force Participation VS Gender Distribution",
        text='total',
        color_discrete_sequence=colors)

# --------New Code------- 
    # Age Group
    age_group_bar = px.bar(
        query.main_age_group, 
        x='year',
        y='total',
        color='age_group',
        barmode='group',
        title=f"Labour Force Participation VS Gender Distribution",
        text='total',
        color_discrete_sequence=colors)

# Pie chart
    pieChart = px.pie(
        data_frame=query.pie_group,
        names="year",
        values="total",
        title="Labour force Distribution over the years",
        color_discrete_sequence=colors)
# Line chart
    lineChart = px.line(
       query.line_chart, 
        x='year', 
        y='total',
        color='labour_force_character',
        labels={'value': 'total', 'year': 'year'},
        title="Emply",
        text='total',
        color_discrete_sequence=['#d95f01','#232323','#277f71']
        )
    
# --------New Code-------
    # Group all the chart name into one list 
    barChartLists= [bar_employment,age_employment,labour_force,age_group_bar]

# ------ Layout Functions ---------
    for i in range(0,len(barChartLists)):
        # Custom Function for the title custtomizatin
        title.BarChartTitle(barChartLists[i],barChartLists[i]['layout']['title'].text)
        
    # LINE CHARTS LIST
    lineChartLists = [lineChart]
    for i in range(0,len(lineChartLists)):
        title.LineChartTitle(lineChartLists[i])

# RETURN THE CHARTS
    return bar_employment,age_employment,labour_force,age_group_bar,pieChart,lineChart


# --------------------------APP RUN---------------------------------------


if __name__ == '__main__':
    app.run(debug=True)