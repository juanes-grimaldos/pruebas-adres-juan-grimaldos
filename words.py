import pandas as pd
from fuzzywuzzy import fuzz
from string import ascii_letters

# Function to find close matches between two dataframes
def find_close_matches(df1, df2, column1, column2, max_distance=3):
    # Extract columns
    values_df1 = df1[column1].tolist()
    values_df2 = df2[column2].tolist()
    
    # Initialize results list
    results = []
    
    # Iterate through each pair of values
    for i, value1 in enumerate(values_df1):
        for j, value2 in enumerate(values_df2):
            distance = fuzz.ratio(value1, value2)  # Use fuzz.ratio for similarity
            if distance >= 100 - max_distance:  # Convert max_distance to a ratio threshold
                results.append({
                    'df1_id': df1.loc[i, 'id'],
                    'df2_id': df2.loc[j, 'id'],
                    'df1_value': value1,
                    'df2_value': value2,
                    'distance': distance
                })
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    
    return results_df


data_gov = pd.read_excel("src/data/Municipios.xlsx")
data_p = pd.read_excel("src/data/Prestadores.xlsx")



# Extract unique municipio values and transform to Latin-ASCII and uppercase
val1 = data_gov['municipio'].drop_duplicates().reset_index(drop=True)
val1 = val1.apply(lambda x: x.translate(str.maketrans("", "", ascii_letters)).upper())

# Extract unique muni_nombre values from data_p and transform to Latin-ASCII
val2 = data_p['muni_nombre'].drop_duplicates().reset_index(drop=True)
val2 = val2.apply(lambda x: x.translate(str.maketrans("", "", ascii_letters)).upper())


import pandas as pd
from sodapy import Socrata

# Example authenticated client (needed for non-public datasets):
client = Socrata("www.datos.gov.co",
                "UrELrjJl5Qtq8TXxiQ9G8UNg0",
                username="est.juan.grimaldos@unimilitar.edu.co",
                password="LAVUELTA_almundo2020*")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("xdk5-pm3f", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
