from Artwork import Artwork

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