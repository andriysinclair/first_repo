import pandas as pd
from typing import List, Tuple

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
individual_df["female_income"] = list(
    zip(individual_df["female"], individual_df["income"]))

# print(individual_df)


# Transforming into household level dataframe
household_df = individual_df.groupby("household_id").agg(
    size_hh=("person", "count"),
    mean_age=("age", "mean"),
    min_age=("age", "min"),
    max_age=("age", "max"),
    # collects all age values into a list for each household
    nr_children=("age", list),
    nr_female=("female", list),
    mean_income=("income", "mean"),
    total_income=("income", "sum"),
    # collects a list of female_income tuples for each household
    main_earner_female=("female_income", list)

)

# function to count the number of children


def nr_children(x: List[int]) -> int:
    count = len([i for i in x if i < 18])
    return count

# function to count the number of females


def nr_female(x: List[bool]) -> int:
    count = len([i for i in x if i])
    return count


def main_earner_female(x: List[Tuple[bool, float]]) -> str:
    female_income = x[0]   # collects the first tuple in the list
    for tup in x:  # loops through each tuple
        # if value is a female and income is higher than the first tuple
        if tup[0] and tup[1] > female_income[1]:
            female_income = tup   # change the first tuple with that tuple
    if female_income[0]:
        # if at the end the tuple is a female - thus with higher incomee
        return "yes"
    else:
        return "no"


# applying functions to columns
household_df["nr_children"] = household_df["nr_children"].apply(nr_children)
household_df["nr_female"] = household_df["nr_female"].apply(nr_female)
household_df["main_earner_female"] = household_df["main_earner_female"].apply(
    main_earner_female)


print(household_df)
