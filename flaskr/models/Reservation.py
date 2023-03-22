
class Restaurant:
    def __init__(self, venue_info, slots):
        self.venue_info = venue_info
        self.slots = slots

    def to_string(self):
        slots_str = ', '.join(slot.to_string() for slot in self.slots)
        return f"{self.venue_info.to_string()} Available reservations include: {slots_str}"


# These classes come directly off of what is returned when querying find_open_reservations
# ['venue', 'templates', 'slots', 'notifies', 'pickups']

class VenueInfo:
    def __init__(self, resy_id, name, cuisine, price_range, rating, num_ratings, location):
        self.resy_id = resy_id
        self.name = name
        self.cuisine = cuisine
        self.price_range = price_range
        self.rating = rating
        self.num_ratings = num_ratings
        self.location = location
    
    def to_string(self):
        return f"{self.name} is a {self.price_range} {self.cuisine} restaurant with a rating of \
        {self.rating} ({self.num_ratings} ratings) located in {self.location}."


class ReservationSlot:
    def __init__(self, date_start, date_end):
        self.date_start = date_start
        self.date_end = date_end

    def to_string(self):
       return f"({self.date_start}:{self.date_end})"





