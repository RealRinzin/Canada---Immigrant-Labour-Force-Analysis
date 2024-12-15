import pandas as pd
df = pd.read_csv('./clean_immigrant_data.csv')
# Gender List
genderList = df['gender'].unique()
# Year List
yearList = df['year'].unique()
# Labour Character List
labourList = df['labour_force_character'].unique()
# Age Group
ageGroupList = df['age_group'].unique()
# Immigratn Status
immigrantStatusList = df['immigrant_status'].unique()

