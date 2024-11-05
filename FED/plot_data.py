import matplotlib.pyplot as plt
# import clean_data as cd
from typing import Dict
import pandas as pd

# Create a function to create a dictionary with country
# keys and GDP pc over the years as tuples


def group_country_data(clean_data: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    countries = clean_data['country'].unique()

    country_data_dict = {}

    for country in countries:
        country_data = clean_data[clean_data['country'] == country]
        country_data_dict[country] = country_data

    return country_data_dict


# Create a function to plot the GDP of countries over time
def plot_country_gdp_data(country_data_dict: Dict[str, pd.DataFrame]) -> None:
    for country, data in country_data_dict.items():
        plt.plot(data['year'],
                 data['gdp_per_capita'],
                 label=country,
                 marker='o')
    plt.title('Change in the GDP per capita of Countries over Time')
    plt.xlabel('Year')
    plt.ylabel('GDP per capita (USD)')
    plt.legend()
    plt.show()

# Apply our data to our functions to create the
# relevant plot of GDP over time for the 7 countries
# country_data_dict=group_country_data(cd)
# plot_country_gdp_data(country_data_dict)
