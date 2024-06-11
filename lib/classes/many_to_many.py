# band.py
 #Class representing a Band
class Band:
    def __init__(self, name, hometown):
         # Initialize Band with a name, hometown, and an empty list of concerts
        self._name = name
        self._hometown = hometown
        self._concerts = []

 # Getter method for the band's name
    @property
    def name(self):
        return self._name

# Setter method for the band's name
    @name.setter
    def name(self, new_name):
        # Ensure the new name is a non-empty string
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")

# Getter method for the band's hometown
    @property
    def hometown(self):
        return self._hometown

 #Getter method for the band's concerts
    @property
    def concerts(self):
        return self._concerts

# Method to add a new concert for the band at a venue and date
    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        self._concerts.append(new_concert)
        venue.concerts.append(new_concert)
        return new_concert

# Method to generate introductions for all concerts the band has played
    def all_introductions(self):
        introductions = []
        for concert in self._concerts:
            introductions.append(concert.introduction())
        return introductions

# Method to get all unique venues where the band has performed
    def venues(self):
        venues_set = set()
        for concert in self._concerts:
            venues_set.add(concert.venue)
        return list(venues_set)

# venue.py
# Class representing a Venue
class Venue:
     # Initialize Venue with a name, city, and an empty list of concerts.
    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._concerts = []

 # Getter method for the venue's name
    @property
    def name(self):
        return self._name
 # Setter method for the venue's name
    @name.setter
    def name(self, new_name):
       # Ensure the new name is a non-empty string 
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")

 # Getter method for the venue's city
    @property
    def city(self):
        return self._city

# Getter method for the venue's concerts
    @property
    def concerts(self):
        return self._concerts

# Method to get a concert at the venue on a specific date
    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None

# Method to get all unique bands that have performed at the venue
    def bands(self):
        bands_set = set()
        for concert in self._concerts:
            bands_set.add(concert.band)
        return list(bands_set)

# Method to get a concert at the venue on a specific date
    def concerts_on_date(self, date):
        concerts_on_date = []
        for concert in self._concerts:
            if concert.date == date:
                concerts_on_date.append(concert)
        return concerts_on_date

# concert.py
# Class representing a Concert
class Concert:
    def __init__(self, date, band, venue):
        # Initialize Concert with a date, band, and venue.
        self._date = date
        self._band = band
        self._venue = venue

# Getter method for the concert's date
    @property
    def date(self):
        return self._date

# Setter method for the concert's date
    @date.setter
    def date(self, new_date):
        # Ensure the new date is a non-empty string
        if isinstance(new_date, str) and len(new_date) > 0:
            self._date = new_date
        else:
            raise ValueError("Date must be a non-empty string.")

# Getter method for the concert's band
    @property
    def band(self):
        return self._band

# Setter method for the concert's band
    @band.setter
    def band(self, new_band):
        self._band = new_band

# Getter method for the concert's venue
    @property
    def venue(self):
        return self._venue

# Setter method for the concert's venue
    @venue.setter
    def venue(self, new_venue):
        self._venue = new_venue

# Method to check if the concert is a hometown show for the band
    def hometown_show(self):
        return self.venue.city == self.band.hometown

# Method to generate an introduction for the concert
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"