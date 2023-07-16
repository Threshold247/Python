# This file will need to use the DataManager,
# FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager


datamanager = DataManager()
sheet_data = datamanager.get_sheet_data()
print(sheet_data)
# if column is empty check for the IATA code
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        # go through the data from Tequila and access the IATA code for each city
        row["iataCode"] = flight_search.get_country_code(row['city'])
    print(sheet_data)
    # update the datamanager data attribute with the new data
    datamanager.data = sheet_data
    # method takes the new sheet data and loops through it to add each city IATA code
    datamanager.update_destination_codes()






