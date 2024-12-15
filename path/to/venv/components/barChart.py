import plotly.express as px
import pandas as pd
# import Dashboard as Dashboard
import components.Dashboard as db
import components.Query as query

# df = pd.read_csv('./clean_immigrant_data.csv')
def test(name,colors):
    name = px.bar(
        db.check, 
        x='year',
        y='total',
        color='gender',
        barmode='group',
        title=f"Total Labour Force Participation with Gender Distribution",
        text='total',
        color_discrete_sequence=colors)
    return name


def ageGroup(year,colors):
    result = query.yearFun(year)
    name = px.bar(
        result, 
        x='age_group',
        y='total',
        color='gender',
        barmode='group',
        title=f"Age Group and Gender Distribution- {year}",
        text='total',
        color_discrete_sequence=colors)
    return name
