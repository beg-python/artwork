from datetime import date
from Visitor import Visitor
from Member import Member

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