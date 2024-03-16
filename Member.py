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