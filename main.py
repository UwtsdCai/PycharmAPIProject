#Importing requests library to make HTTP requests
import requests

api_key = 'd5cf560adb174542b29a62db4e592b36'  #OpenCage Api Key
base_url = 'https://api.opencagedata.com/geocode/v1/json' #OpenCage Base URI

#Normal geocoding (Addresses to coordinates)
def geo_add(address):
   #error checking the address (cannot be empty)
    if not address.strip():
        print("Error, the address cannot be empty")
        return

    params = {
        'q': address,  #The GeoCode address
        'key': api_key  #The API Key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        geo_data = response.json()
        if geo_data['results']:
            #print the results latitude and longitude
            result = geo_data['results'][0]
            print(f"Address: {result['formatted']}")
            print(f"Latitude: {result['geometry']['lat']}")
            print(f"Longitude: {result['geometry']['lng']}")
        else:
            print("No results found")
    else:
        print("Error getting data")

#Reverse Geocoding: Coordinates to Address
def rev_geo(lat, lng):
    #error checking the input (cannot be left blank)
    if not lat.strip() or not lng.strip():
        print("Error: Latitude and Longitude cannot be empty.")
        return
    params = {
        'q': f"{lat},{lng}",  #Latitude and Longitude
        'key': api_key  #The Api Key
    }

    response = requests.get(base_url, params=params)

    #if the response is successful, print the address
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            print(f"Reverse Geocoding - Address: {data['results'][0]['formatted']}")
        else:
            print("No results found for the coordinates.")
    else:
        print("Error fetching data for reverse geocoding.")

#Where the user will select either geocoding or reverse geocoding
if __name__ == "__main__":
    while True:
        try:
            print("Geocoding: (Address to coordinates | Reverse Geocoding: Coordinates to address)")
            usr_choice = int(input("Please select 1 for geocoding and 2 for reverse geocoding:"))

            if usr_choice == 1:
                address = input("Enter an address, or place name you would like to geocode:")
                geo_add(address)

            elif usr_choice == 2:
                latitude = input("Please enter latitude")
                longitude = input("Please enter longitude")
                rev_geo(latitude,longitude)

            else:
                print("Error with option, please make sure you only input 1 or 2")

        except ValueError:
            #In case the user inputs something that can't be converted to an integer
            print("Error: Invalid input. Please enter a valid number (1 or 2).")