import os
from datetime import date, timedelta, datetime
import requests
import json
from flaskr.models.Reservation import ReservationSlot, Restaurant, VenueInfo


class ResyClient:

    # http://subzerocbd.info/#introduction
    def __init__(self):
        self.baseUrl = "https://api.resy.com"
        self.headers = {
            'Authorization': "ResyAPI api_key=\"" + os.getenv("RESY_API_KEY") + "\""
        }


    def parse_reservation_slots(self, json_data):
        date_start_str = json_data['date']['start']
        date_end_str = json_data['date']['end']

        date_start = datetime.strptime(date_start_str, '%Y-%m-%d %H:%M:%S')
        date_end = datetime.strptime(date_end_str, '%Y-%m-%d %H:%M:%S')    

        return ReservationSlot(date_start, date_end)

    def parse_venue_info(self, json_data):
        return VenueInfo(json_data["id"], json_data["name"], json_data["type"], json_data["price_range"], json_data["rating"], json_data["total_ratings"], json_data["location"])


    def parse_restaurant(self, json_data):
        venue_info = self.parse_venue_info(json_data["venue"])
        reservation_slot_data = json_data["slots"]

        slots = list(map(self.parse_reservation_slots, reservation_slot_data))
        return Restaurant(venue_info, slots)   


    def find_open_reservations(self, resy_req_info):
        
        day = (resy_req_info.date).strftime("%Y-%m-%d")
        params = {
            'lat': '40.696235726060294',
            'long': '-73.97968099999999',
            'day': day,
            'party_size': str(resy_req_info.party_size),
            'limit': 10
        }
        response = requests.get(self.baseUrl + "/4/find", params=params, headers=self.headers)
        
        if response.status_code != 200:
            return "ERROR: " + status_code


        data = json.loads(response.content)

        restaurants_with_availability = list(map(self.parse_restaurant, data["results"]["venues"]))


        return restaurants_with_availability










