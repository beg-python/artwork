from Visitor import Visitor

class Others(Visitor):
    def apply_discount(self):
        if self.get_age() <18 or self.get_age() >60 or self.get_profession() == "student" or self.get_profession() == "teacher":
            return 1 #free ticket
        else:
            return 0 #no discount