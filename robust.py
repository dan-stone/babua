import argparse
import numbers
from types import SimpleNamespace

import requests


API_KEY = "AIzaSyCRbZdcQnUi_fHi_QISRsv2BhCyDgNcMtk"


def retrieve_gps_coordinates():
    # Get approximate GPS coordinates
    response = requests.get(
        url="https://freegeoip.net/json/"
    )

    return SimpleNamespace(
        lat=response.json()["latitude"],
        long=response.json()["longitude"]
    )


def find_nearby_places(lat, long, search_string, api_key=API_KEY):
    assert isinstance(lat, numbers.Real)
    assert -90 <= lat <= 90
    assert isinstance(long, numbers.Real)
    assert -180 <= long <= 180

    response = requests.post(
        url="https://maps.googleapis.com/maps/api/place/nearbysearch/json",
        params={
            "key": api_key,
            "location": f"{lat},{long}",
            "radius": 10000,
            "keyword": search_string
        }
    )

    return response.json()["results"]


def main(query):
    coordinates = retrieve_gps_coordinates()

    for place in find_nearby_places(coordinates.lat, coordinates.long, query):
        print(f"{place['name']}: {place['vicinity']}")


if __name__ == "__main__":
    # Get a search string as a command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-q",
        type=str,
        required=True,
        help="Search string"
    )
    args = parser.parse_args()

    main(query=args.q)
