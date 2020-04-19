

class UrlObj:
    def __init__(self):
        self.location = "southjersey"#self.get_location()  # Location(i.e. City) being searched
        self.postal_code = "08205" #self.get_postal_code()  # Postal code of location being searched
        self.query = "furniture" #self.get_query()  # Search for the type of items that will be searched
        self.max_price = "1000" #self.get_max_price()  # Max price of the items that will be searched
        self.radius = "20" #self.get_radius()  # Radius of the area searched derived from the postal code given previously

        self.url = f"https://{self.location}.craigslist.org/search/sss?&max_price={self.max_price}&postal={self.postal_code}&query={self.query}&20card&search_distance={self.radius}"

    def get_location(self):
        location = input("Please enter the location: ")
        return location

    def get_postal_code(self):
        postal_code = input("Please enter the postal code: ")
        return postal_code

    def get_query(self):
        query = input("Please enter the item: ")
        return query

    def get_max_price(self):
        max_price = input("Please enter the max price: ")
        return max_price

    def get_radius(self):
        radius = input("Please enter the radius: ")
        return radius

