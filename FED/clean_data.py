import pandas as pd
from load_data import load_data

def clean_and_wrangle_gdp_data(data):
    # Convert economy codes to a column by resetting the index
    data.reset_index(inplace=True)
    
    # Melt the Dataframe 
    data_melt = pd.melt(data, 
                        id_vars=['economy'], 
                        var_name='Year_str', 
                        value_name='gdp_per_capita')
    
    # Create a new column 'year' by converting 'Year_str' to integers
    data_melt['year'] = data_melt['Year_str'].str.replace('YR', '').astype(int)
    data_melt['gdp_per_capita'] = data_melt['gdp_per_capita'].astype(str)

    # Convert gdp_per_capita to numeric values just in case
    data_melt['gdp_per_capita'] = pd.to_numeric(data_melt['gdp_per_capita'], errors='coerce')

    # Reset index
    data_clean = data_melt.reset_index(drop=True)
    
    return data_clean

# Load data again
data = load_data(countries=["UK", "United States", "Brazil", "Japan", "China", "Germany", "Switzerland"],
                 indicator="NY.GDP.PCAP.PP.CD", 
                 start_year=2000, 
                 end_year=2022)

cleaned_data = clean_and_wrangle_gdp_data(data)

# Rename and refine variables
cleaned_data=cleaned_data.rename(
    columns={'economy':'country'})
cleaned_data=cleaned_data.loc[:,['country','gdp_per_capita','year']]

# Round GDP per capita to 0 dp
cleaned_data['gdp_per_capita']=cleaned_data['gdp_per_capita'].round(0)

# Print the first five rows of the cleaned dataframe
print(cleaned_data.head())