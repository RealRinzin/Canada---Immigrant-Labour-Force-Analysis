import plotly.express as px
import pandas as pd

# import Dashboard as Dashboard
import components.Dashboard as db
import components.Query as query

# Color Variable
colors = ["#d95f01", "#232323", "#277f71", "#eb862a", "#565656"]


# ---------- New Function ----------
# df = pd.read_csv('./clean_immigrant_data.csv')
def total_labour_force(year):
    result = query.main_labour(year)
    chartName = px.bar(
        result,
        x="year",
        y="total",
        color="gender",
        # orientation="h",
        barmode="group",
        title=f"Total Labour Force Participation with Gender Distribution",
        text="total",
        color_discrete_sequence=colors,
    )
    return chartName


# ---------- New Function ----------
def ageGroup(year):
    # Use the Query functions to assign the return values
    # Which will be use as Dataframe for the chart
    result = query.yearFun(year)
    # Creating the bar chart for the return data (result)
    chartName = px.bar(
        result,
        x="age_group",
        y="total",
        color="gender",
        barmode="group",
        title=f"Age Group and Gender Distribution- {year}",
        text="total",
        color_discrete_sequence=colors,
    )
    return chartName


# ---------- New Function ----------
def emp_fullPart_time():
    data = query.full_vs_part_time_emp
    chartName = px.bar(
        data,
        x="year",
        y="total",
        color="labour_force_character",
        title="Full Time vs Part Time Employment",
        color_discrete_sequence=["#277f71", "#d95f01"],
        # color_discrete_sequence=colors
    )
    return chartName


# ---------- New Function ----------
def labourForce_ageGroup():
    data = query.labourForce_ageGroup
    chartName = px.bar(
        data,
        x="year",
        y="total",
        color="age_group",
        barmode="group",
        title=f"Age Group and Gender Distribution",
        text="total",
        color_discrete_sequence=colors,
    )
    return chartName


# ---------- New Function ----------
def pie_distribution(year):
    chartName = px.pie(
        data_frame=query.pie_group,
        names="year",
        values="total",
        title="Labour force Distribution over the years",
        color_discrete_sequence=colors,
    )
    return chartName
