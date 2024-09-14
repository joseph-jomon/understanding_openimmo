import xmlschema

# Load the XSD schema
schema = xmlschema.XMLSchema('./data_openimmo/openimmo_127c.xsd')

# Validate the XML file and capture detailed error information
try:
    # Validate the XML file against the schema
    schema.validate('./data_openimmo/openimmo-data_127.xml')
    print("XML is valid!")
except xmlschema.XMLSchemaValidationError as e:
    # Print detailed error information if validation fails
    print(f"XML is invalid. Error: {e}")



