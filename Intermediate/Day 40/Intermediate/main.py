# API - Application Programming interface
# set of commands, functions, protocols and objects that programmers can use to create software or interact with an
# external system

# various systems from online have APIs - Yahoo weather, Coinbase, NBA etc...

# it is like a menu where you order data from another system

# 1. API endpoint - location from where the data is stored - usually just a URL link
# 2. in addition to the endpoint you will need to make an API request

import requests

# 1. get the data from the url - API endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response.status_code)  # prints the response code
# response codes -> tells if the request exceeded or failed
# response codes:
# 1XX - Hold on;
# 2XX - Here you go;
# 3XX - Go away - no permission;
# 4XX - I requested missing data, screwed up;
# 5XX - Server screwed up
# all response codes - https://www.webfx.com/web-development/glossary/http-status-codes/

if response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorise to access the data!")
# instead of writing the code above we can do like this:

response.raise_for_status()  # it will raise an error for the specific error with an explanation

data = response.json()["iss_position"]  # this is the actual data
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
print(data)
print(longitude)
print(latitude)

# API parameters
# usually they are provided in the API documentation and some of them are required and some of them are optional

# Parameters required for https://api.sunrise-sunset.org/json are lat and lng in order to give us the
# sunset and sunrise at a specific location

MY_LAT = 44.426765
MY_LONG = 26.102537

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response_2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_2.raise_for_status()

data_2 = response_2.json()
print(data_2)