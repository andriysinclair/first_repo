import wbgapi as wb   #WorldBank API for Economic Data
import pandas as pd

# Expects a list of countries to obtain country codes and query the data
# A code for the Economic indicator can be found by using:
# print(wb.series.info(q="GDP")
# The start year for the data
# The end year for the data

def load_data(countries, indicator, start_year, end_year):

    # Loops through your list of countries and obtains the country code
    country_codes_list = []
    for country in countries:
        country_code = wb.economy.info(q=country).items[0]["id"] # Returns a table and the country code is the 0th entry
        country_codes_list.append(country_code)
        print(country_code)
        print("Printing country code for '{}' ...".format(country))
        print("If you are thrown an error or you obtain an unexpected country code")
        print("Please try a different query")
        print("")

    print("This is your list of country codes used to query the data")
    print(country_codes_list)
    print("")

    # Filters the WB API for the relevant data
    relevant_data = wb.data.DataFrame(indicator, country_codes_list, range(start_year, end_year))

    # Drops years where there is no values across countries, for your indicator
    relevant_data.dropna(axis=1, how="all", inplace=True)

    # returns data frame
    return relevant_data


data = load_data(countries=["UK", "United States", "Brazil", "Japan", "China", "Germany", "Switzerland"], indicator="NY.GDP.PCAP.PP.CD", start_year=1995, end_year=2024)

print(type(data))

#print(wb.economy.info(q="States"))