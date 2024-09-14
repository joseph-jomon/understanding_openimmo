import xmltodict
import pandas as pd
#1. Extract Data from XML

with open('./data_openimmo/openimmo-data_127.xml') as fd:
    xml_data = xmltodict.parse(fd.read())

# Now xml_data is a Python dictionary you can work with
print("Dictionary Keys are :", xml_data['openimmo'].keys())

############################
#2. Transform XML Data to Pandas DataFrame
df = pd.DataFrame(xml_data['openimmo'])  # Adjust 'root_element' to match your XML structure
print(df.head())