from Visitor import Visitor

class Adult(Visitor):
    def apply_discount(self):
        if 18 <= self.get_age() <= 60:
            return 0  #no discount
        else:
            return -1  #invalid age for adult