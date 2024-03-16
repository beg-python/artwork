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
        print(self.__artwork.get_info())
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
    
    def display_info(self):
        print("--Exhibition--")
        print("ID: ", self.__id)
        print("Name: ", self.__name)
        print("Start Date: ", self.__start_date)
        print("End Date: ", self.__end_date)
        print("Location: ", self.__location)
        print("Artworks in Exhibition: ", end=" ")
        for artwork_item in self.__artworks:
            print(artwork_item.get_artwork().get_title(), end="   ")
        print() 

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
    def apply_discount(self):
        if 18 <= self.get_age() <= 60:
            return 0  #no discount
        else:
            return -1  #invalid age for adult
        
class Others(Visitor):
    def apply_discount(self):
        if self.get_age() <18 or self.get_age() >60 or self.get_profession() == "student" or self.get_profession() == "teacher":
            return 1 #free ticket
        else:
            return 0 #no discount

class Group:
    def __init__(self, group_id, guide):
        self.__group_id = group_id
        self.__guide = guide
        self.__members = [] #members in a group
        if len(self.__members) < 15:
            print()
            print("--Error!!: Cannot create group with less than 15 members--")
            print()
        self.__max = 40
        self.__min = 15

    def get_group_id(self):
        return self.__group_id
    def set_group_id(self, new_group_id):
        self.__group_id = new_group_id
    def get_guide(self):
        return self.__guide
    def set_guide(self, new_guide):
        self.__guide = new_guide

    def display_members(self):
        print("Group Members: " , end=" ")
        for i in self.__members:
            print(i.get_name(), end="     ")
        print()

    def add_member(self, member):
        if self.member_count() <= self.__max:
            self.__members.append(member)

    def remove_member(self, member):
        if member in self.__members and self.member_count() >= self.__min:
            self.__members.remove(member)
        else:
            print(f"{member} is not a member of this group.")
    
    def member_count(self):
        return len(self.__members) #count of mmebers
    
    
class Member:
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
        return 0.5  #50% discount 


class Ticket:
    def __init__(self, id, type, purchase_date, price, exhibition, visitor, group_member):          
        self.__id = id
        self.__type = type
        self.__purchase_date = purchase_date
        self.__price = price
        self.__exhibition = exhibition
        self.__visitor = visitor
        self.__group_member = group_member

    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id
    def get_type(self):
        return self.__type
    def set_type(self, new_type):
        self.__type = new_type
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
    def get_group_member(self):
        return self.__group_member
    def set_group_member(self, new_group_member):
        self.__group_member = new_group_member

    def validate_ticket(self):
        current = date.today()
        if current >= self.__exhibition.get_start_date() and current <= self.__exhibition.get_end_date():
            return True
        else:
            return False
        
    def calculate_price(self):

        if self.__visitor != None:
            discount_percent = self.__visitor.apply_discount()
        else:
            discount_percent = self.__group_member.apply_discount()

        if discount_percent == -1:
            return None
        elif isinstance(self.__group_member, Member):  #group member
            discount_percent = self.__group_member.apply_discount()  
        elif isinstance(self.__visitor, Visitor):  #visitor
            discount_percent = self.__visitor.apply_discount()

        discounted_price = self.__price - (self.__price * discount_percent)
        final_price = discounted_price * 1.05  # 5% VAT

        return final_price
    
    def display_info(self):
        print("--Ticket--")
        print("ID: ",self.__id)
        print("Purchase Date: ", self.__purchase_date)
        print("Price: ", self.__price)

        if self.__visitor != None:
            print("Visitor Name: ",self.__visitor.get_name())
            print("Visitor ID: ", self.__visitor.get_id()) 
        if self.__group_member != None:
            print("Group Member Name: ", self.__group_member.get_name())          
            print("Group Member ID: ", self.__group_member.get_id()) 

        print("Exhibition Location: ", self.__exhibition.get_location()) #exhibition location
        print("Exhibition Name: ", self.__exhibition.get_name()) #name of exhibition
        print("Exhibition Duration: ", self.__exhibition.get_duration()) #time of exhibition







