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
