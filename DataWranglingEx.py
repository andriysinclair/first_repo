import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_colwidth', None)  # Show full content in each 


# Individual level dataframe
individual_df = pd.DataFrame({
"household_id": [37, 37, 37, 241, 242, 155789, 155789, 155789],
"person": [1, 2, 3, 1, 1, 1, 2, 3],
"age": [20, 19, 19, 50, 29, 58, 61, 15],
"income": [10000, 5300, 4700, 90000, 20000, 5000, 110000, 0],
"female": [False, True, False, True, False, False, True, False]
})

# zipping female and income
individual_df["female_income"] = list(zip(individual_df["female"], individual_df["income"]))

#print(individual_df)



# Transforming into household level dataframe
household_df = individual_df.groupby("household_id").agg(
    size_hh=("person", "count"),
    mean_age=("age", "mean"), 
    min_age=("age", "min"),
    max_age=("age", "max"),
    nr_children=("age", list), # collects all age values into a list for each household
    nr_female=("female", list),
    mean_income=("income", "mean"),
    total_income=("income", "sum"),
    main_earner_female=("female_income", list)  # collects a list of female_income tuples for each household

)



print(household_df)