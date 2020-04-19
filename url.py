
class UrlObj:
    def __init__(self):
        self.location = "southjersey" # Location(i.e. City) being searched
        self.postal_code = "08205" # Postal code of location being searched
        self.query = "furniture" # Search for the type of items that will be searched
        self.max_price = "1000" # Max price of the items that will be searched
        self.radius = "20" # Radius of the area searched derived from the postal code given previously

        self.url = f"https://{self.location}.craigslist.org/search/sss?&max_price={self.max_price}&postal={self.postal_code}&query={self.query}&20card&search_distance={self.radius}"
