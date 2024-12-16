import pandas as pd

df = pd.read_csv("./clean_immigrant_data.csv")


# ------------------------------ Main Dashboard Queries ------------------------------
# Total Labour Participation in
# Year Base for the Age Group
# Year
def yearFun(year):
    if year:
        return (
            df[(df["labour_force_character"] == "Labour force") & (df["year"] == year)]
            .groupby(["gender", "age_group"])["total"]
            .sum()
            .reset_index()
        )
    else:
        year = 2024
        return (
            df[(df["labour_force_character"] == "Labour force") & (df["year"] == year)]
            .groupby(["gender", "age_group"])["total"]
            .sum()
            .reset_index()
        )


# ---------- New Query ----------
# Total Labour force Participation
def main_labour(year):
    if year:
        return (
            df[(df["labour_force_character"] == "Labour force")]
            .groupby(["year", "gender"])["total"]
            .sum()
            .reset_index()
        )
    else:
        return (
            df[df["labour_force_character"] == "Labour force"]
            .groupby(["year", "gender"])["total"]
            .sum()
            .reset_index()
        )


# ---------- New Query ----------
#  Age Group
# Total Labour Force Participation with age group in different years
labourForce_ageGroup = df.groupby(["year", "age_group"])["total"].sum().reset_index()

# ---------- New Query ----------
# Pie
pie_group = (
    df[(df["labour_force_character"] == "Labour force")]
    .groupby(["year"])["total"]
    .sum()
    .reset_index()
)

# ---- New Query -----
employed_unemployed = (
    df[
        (df["labour_force_character"] == "Employment")
        | (df["labour_force_character"] == "Unemployment")
    ]
    .groupby(["year", "labour_force_character"])["total"]
    .sum()
    .reset_index()
)

# ---- New Query -----
# Full time and Part Time labour participation in Total Labour Market
# Full Time vs Part Time
full_vs_part_time_emp = (
    df[
        (df["labour_force_character"] == "Full-time employment")
        | (df["labour_force_character"] == "Part-time employment")
    ]
    .groupby(["year", "labour_force_character"])["total"]
    .sum()
    .reset_index()
)
