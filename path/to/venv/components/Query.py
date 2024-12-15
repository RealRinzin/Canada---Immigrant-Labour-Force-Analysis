import pandas as pd
df = pd.read_csv('./clean_immigrant_data.csv')


# Year Base for the Age Group
def yearFun(year):  
    if year:
        return  df[(df['labour_force_character']=='Labour force') & (df['year'] == year)].groupby(['gender','age_group'])['total'].sum().reset_index()
    else:
        year = 2024
        return  df[(df['labour_force_character']=='Labour force') & (df['year'] == year)].groupby(['gender','age_group'])['total'].sum().reset_index()

# ---------------------------Main Dashboard---------------------------

main_labour_force_participation = df[
    (df['labour_force_character'] =='Labour force')|
    (df['labour_force_character'] =='Not in labour force')
    ].groupby(['year','labour_force_character'])['total'].sum().reset_index()
# Age Group
main_age_group = df.groupby(['year','age_group'])['total'].sum().reset_index()

# Pie
pie_group = df.groupby('year')['total'].sum().reset_index()

# Line

line_chart = df[
    (df['labour_force_character'] =='Labour force')|
    (df['labour_force_character'] =='Not in labour force')|
    (df['labour_force_character'] =='Population')
    ].groupby(['year','labour_force_character'])['total'].sum().reset_index()
