import argparse
from types import SimpleNamespace

import requests


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
    url="https://freegeoip.net/json/",
    verify=False
)
coordinates = SimpleNamespace(
    lat=response.json()["latitude"],
    long=response.json()["longitude"]
)

response = requests.post(
    url="https://maps.googleapis.com/maps/api/place/nearbysearch/json",
    params={
        "key": "AIzaSyCRbZdcQnUi_fHi_QISRsv2BhCyDgNcMtk",
        "location": "{},{}".format(coordinates.lat, coordinates.long),
        "radius": 10000,
        "keyword": args.q
    }
)

for result in response.json()["results"]:
    print("{}: {}".format(result['name'], result['vicinity']))
