import matplotlib.pyplot as plt

from data_cleaning import *

print(candidates_df.info())

print(skills_df.head())

skills_df["skill_name"].value_counts().head(10).plot(
    kind="bar"
)

plt.title("Top Skills")

plt.show()