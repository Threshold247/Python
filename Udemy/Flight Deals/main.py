# This file will need to use the DataManager,
# FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from pprint import pprint


datamanager = DataManager()
sheet_data = datamanager.get_sheet_data()
pprint(sheet_data)
flight_search = FlightSearch()
notification = NotificationManager()

ORIGIN_CITY_IATA = "LON"

# if column is empty check for the IATA code
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        # go through the data from Tequila and access the IATA code for each city
        row["iataCode"] = flight_search.get_country_code(row['city'])
    print(sheet_data)
    # update the datamanager data attribute with the new data
    datamanager.data = sheet_data
    # method takes the new sheet data and loops through it to add each city IATA code
    datamanager.update_destination_codes()

today_date = datetime.now()
# timedelta allows for days to be added to a date
tomorrow_date = today_date + timedelta(days=1)
return_date = today_date + timedelta(days=(30*6))

for destination in sheet_data:
    flight_data = flight_search.get_flight_data(departure_city_code=ORIGIN_CITY_IATA,
                                                arrival_city_code=destination['iataCode'],
                                                date_from=tomorrow_date,
                                                date_to=return_date)
    # flight search price is lower than the google sheet price
    if flight_data.price < destination['lowestPrice']:
        # run the notification method with a custom message argument
        notification.send_sms(message=
                              f"Flight Alert! Pay R{flight_data.price} to "
                              f"fly from {flight_data.departure_city}-{flight_data.departure_airport}"
                              f"to{flight_data.destination_city}-{flight_data.destination_airport} "
                              f"from {flight_data.out_date} to {flight_data.return_date}"
                              )







