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