import argparse
from types import SimpleNamespace

import requests


API_KEY = "AIzaSyCCO8Oyd2q4_3bvviT4w8xeiBepG-QGc4Y"


# Get a search string as a command line argument
parser = argparse.ArgumentParser()
parser.add_argument(
    "-q",
    type=str,
    required=True,
    help="Search string"
)
args = parser.parse_args()

# Get approximate GPS coordinates
response = requests.get(
    url="https://freegeoip.net/json/"
)
coordinates = SimpleNamespace(
    latitude=response.json()["latitude"],
    longitude=response.json()["longitude"]
)

# response = requests.post(
#     url=f"https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}"
# )
# coordinates = SimpleNamespace(
#     latitude=response.json()["location"]["lat"],
#     longitude=response.json()["location"]["lng"],
# )

print(coordinates)

response = requests.post(
    url="https://maps.googleapis.com/maps/api/place/nearbysearch/json",
    params={
        "key": "AIzaSyCRbZdcQnUi_fHi_QISRsv2BhCyDgNcMtk",
        "location": f"{coordinates.latitude},{coordinates.longitude}",
        "radius": 10000,
        "keyword": args.q
    }
)

for result in response.json()["results"]:
    print(result["name"])
    print(result.keys())
