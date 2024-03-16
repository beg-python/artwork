from datetime import date
from Artwork import Artwork, ArtworkItem
from Exhibition import Exhibition
from Visitor import Visitor, Adult, Others
from Group import Group, Member
from Ticket import Ticket

#test cases
############(a) addition of new art############
new_artwork = Artwork(1, "Starry Night", "Vincent van Gogh", date(1889, 1, 1), "Post-Impressionist masterpiece")
new_artwork_item = ArtworkItem(new_artwork, "Gallery B")
new_artwork_item.display_info()
print()
new_artwork1 = Artwork(2, "Mona Lisa", "Leonardo da Vinci", date(1503, 1, 1), "Iconic portrait")
new_artwork_item1 = ArtworkItem(new_artwork1, "Gallery B") 
new_artwork_item1.display_info()
print()

############(b) opening a new museum exhibition############
new_exhibition = Exhibition(1, "Impressionist Masterpieces", date(2024, 7, 1), date(2024, 9, 30), "East Wing")
#adding artworks to exhibition
new_exhibition.add_artwork(new_artwork_item) 
new_exhibition.add_artwork(new_artwork_item1)
new_exhibition.display_info()
print()

############(c) purchase of ticket############
#adult purchases ticket
adult_visitor = Adult(1, "Alice Johnson", 25, "engineer")
adult_ticket = Ticket(1, "Inperson", date.today(), 63, new_exhibition, adult_visitor, None)

#student purchases ticket
student_visitor = Others(1, "Adam Newman", 20, "student")
student_ticket = Ticket(2, "Online", date.today(), 63, new_exhibition, student_visitor, None)

#group purchases ticket
group1 = Group(1, "tour guide")
member1 = Member(1, "Joden Dick", 30, "content creator")
member2 = Member(2, "Jane Smith", 25, "doctor")
group1.add_member(member1)
group1.add_member(member2)
member_ticket1 = Ticket(3, "Inperson", date.today(), 63, new_exhibition, None, member1)
member_ticket2 = Ticket(4, "Online", date.today(), 63, new_exhibition, None, member2)

############(d) ticket reciepts + final price############
adult_ticket.display_info()
print("ticket final price: ",adult_ticket.calculate_price())
print()
student_ticket.display_info()
print("ticket final price: ",student_ticket.calculate_price())
print()
member_ticket1.display_info()
print("ticket final price: ",member_ticket1.calculate_price())
print()
member_ticket2.display_info()
print("ticket final price: ",member_ticket2.calculate_price())