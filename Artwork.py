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
    