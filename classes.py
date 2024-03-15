from datetime import date

class Artwork:
    def __init__(self,  id, title, artist, date_of_creation, historical_sig):
        self.__id = id
        self.__title = title
        self.__artist = artist
        self.__date_of_creation = date_of_creation
        self.__historical_sig = historical_sig

    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id
    def get_title(self):
        return self.__title
    def set_title(self, new_title):
        self.__title = new_title
    def get_artist(self):
        return self.__artist
    def set_artist(self, new_artist):
        self.__artist = new_artist
    def get_date_of_creation(self):
        return self.__date_of_creation
    def set_date_of_creation(self, new_date):
        self.__date_of_creation = new_date
    def get_historical_sig(self):
        return self.__historical_sig
    def set_historical_sig(self, new_sig):
        self.__historical_sig = new_sig
    
    def get_info(self):
        return f"ID: {self.__id}\nTitle: {self.__title}\nArtist: {self.__artist}\nDate of Creation: {self.__date_of_creation}\nHistorical Significance: {self.__historical_sig}"
    
class ArtworkItem:
    def __init__(self, artwork, location):
        self.__artwork = artwork
        self.__location = location

    def get_artwork(self):
        return self.__artwork
    def set_artwork(self, new_artwork):
        self.__artwork = new_artwork
    def get_location(self):
        return self.__location
    def set_location(self, new_location):
        self.__location = new_location
    
    def display_info(self):
        print("--Artwork--")
        print({self.__artwork.get_info()})
        print(f"Location: {self.__location}")

class Exhibition:
    def __init__(self, id, name, start_date, end_date, location):
        self.__id = id
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__location = location
        self.__artworks = [] #creating a list to store the diffreent artworks in an exhibition

    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_start_date(self):
        return self.__start_date
    def set_start_date(self, new_start_date):
        self.__start_date = new_start_date
    def get_end_date(self):
        return self.__end_date
    def set_end_date(self, new_end_date):
        self.__end_date = new_end_date
    def get_location(self):
        return self.__location
    def set_location(self, new_location):
        self.__location = new_location

    def get_duration(self):
        return self.__end_date - self.__start_date
    
    def add_artwork(self, artwork_item):
        self.__artworks.append(artwork_item) #adding artwork in list
    def remove_artwork(self, artwork_item):
        self.__artworks.remove(artwork_item) #removing artwork from list
    
    def get_info(self):
        print("--Exhibition--")
        print("ID: ", self.__id)
        print("Name: ", self.__name)
        print("Start Date: ", self.__start_date)
        print("End Date: ", self.__end_date)
        print("Location: ", self.__location)
        print("Artworks in Exhibition: ", self.__artworks)

class Visitor:
    def __init__(self, id, name, age, profession):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__profession = profession

    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        self.__age = new_age
    def get_profession(self):
        return self.__profession
    def set_profession(self, new_profession):
        self.__profession = new_profession

    def apply_discount(self):
        return 0
    
class Adult(Visitor):
    def apply_discount(self, original_price):
        if 18 <= self.__age <= 60:
            return 0  #no discount
        else:
            return -1  #invalid age for adult
        
class Others(Visitor):
    def apply_discount(self, original_price):
        if self.__age <18 or self.__age >60 or self.__profession == "student" or self.__profession == "teacher":
            return 0.5

class Group:
    def __init__(self, group_id, leader):
        self.__group_id = group_id
        self.__leader = leader
        self.__members = [] #people in a group

    def get_group_id(self):
        return self.__group_id
    def set_group_id(self, new_group_id):
        self.__group_id = new_group_id
    def get_leader(self):
        return self.__leader
    def set_leader(self, new_leader):
        self.__leader = new_leader
    def get_members(self):
        return self.__members
    
    def add_member(self, member):
        self.__members.append(member)

    def remove_member(self, member):
        if member in self.__members:
            self.__members.remove(member)
        else:
            print(f"{member} is not a member of this group.")
    
    def member_count(self):
        return len(self.__member) #count of mmebers
    
    def apply_discount(self, original_price):
        return 0.5  #50% discount 
    

class Ticket:
    def __init__(self, id, visitor_id, ticket_type, event_id, purchase_date, price, exhibition, visitor):          
        self.__id = id
        self.__ticket_type = ticket_type
        self.__purchase_date = purchase_date
        self.__price = price
        self.__exhibition = exhibition
        self.__visitor = visitor

    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id
    def get_ticket_type(self):
        return self.__ticket_type
    def set_ticket_type(self, new_ticket_type):
        self.__ticket_type = new_ticket_type
    def get_purchase_date(self):
        return self.__purchase_date
    def set_purchase_date(self, new_purchase_date):
        self.__purchase_date = new_purchase_date
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price
    def get_exhibition(self):
        return self.__exhibition
    def set_exhibition(self, new_exhibition):
        self.__exhibition = new_exhibition
    def get_visitor(self):
        return self.__visitor
    def set_visitor(self, new_visitor):
        self.__visitor = new_visitor

    def validate_ticket(self):
        current = date.today()
        if current >= self.__exhibition.get_start_date() and current <= self.__exhibition.get_end_date():
            return True
        else:
            return False
        
    def calculate_price(self):
        discount_percent = self.visitor.apply_discount(self.__price)
        if discount_percent == -1:
            return None  
        else:
            discounted_price = self.__price - (self.__price * discount_percent)
            final_price = discounted_price * 1.05  #5% VAT
            return final_price
        
    def ticket_info(self):
        print("--Ticket--")
        print("ID: ",self.__id)
        print("Ticket Type: ", self.__ticket_type)
        print("Purchase Date: ", self.__purchase_date)
        print("Price: ", self.__price)
        print("Visitor ID: ", self.__visitor.get_id()) #visitor ID
        print("Location: ", self.__exhibition.get_location()) #exhibition location






