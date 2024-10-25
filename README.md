# first_repo

We use the World Bank API (WBGAPI) to obtain GDP data for various countries ...

## Modules

### load_data.py

This contains the function:

**load_data(countries, indicator, start_year, end_year)**, with the parameters:

* **countries**: This expects a list of country strings. The function will use this to query the API for relevant country codes and use them to obtain the relevant data

* **indicator**: This is the economic indicator for which you want to find data. `print(wb.series.info(q="search term")` can be used to query the API for the relevant indicator keyword. The string will then be used as a parameter

* **start_year**: intiger for start year of the data to extract

* **end_year**: intiger for end year of the data to extract

The function returns a data. If there are any years for which there is no data for all countries that year will be omitted.

### clean_data.py

This contains the function that cleans and wrangles GDP per capita data for specified economies:

* **Reset Index**: Resets the dataframe index for proper formatting

* **Melt Dataframe**: Converts the wide dataframe into a long dataframe, using 'economy' as an unique id and 'Year_str' as the variable name for years

* **Extract Year**: Creates a new 'year' column by converting the 'Year_str' values from strings to integers

* **Convert GDP Values**: Ensures that the 'gdp_per_capita' values are numeric

* **Reset Index Again**: Resets the index of the cleaned dataframe.
