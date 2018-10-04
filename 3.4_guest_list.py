guest_list = ["Oprah Winfrey", "Michael Jackson", "Kandi Burruss"]

message = ("You are invited to my party, " + (guest_list[0] + "!"))
print(message) 
message = ("You are invited to my party, " + (guest_list[1] + "!"))
print(message)
message = ("You are invited to my party, " + (guest_list[2] + "!"))
print(message)

canceled_guest = ("Oprah Winfrey cannot make it to the event.")
print(canceled_guest)

guest_list[0] = ("Beyonce' Knowles")
print(guest_list)

message = ("You are invited to my party, " + (guest_list[0] + "!"))
print(message) 
message = ("You are invited to my party, " + (guest_list[1] + "!"))
print(message)
message = ("You are invited to my party, " + (guest_list[2] + "!"))
print(message)

new_guest = ("I found a bigger table. More are guest invited!")
print(new_guest)

guest_list.insert(0 , "Tina Turner")
guest_list.insert(2 , "Oliva Pope")
guest_list.insert(5 , "Wendy Williams")
print(guest_list)

message = ("You are invited to my party, " + (guest_list[0] + "!"))
print(message) 
message = ("You are invited to my party, " + (guest_list[1] + "!"))
print(message)
message = ("You are invited to my party, " + (guest_list[2] + "!"))
print(message)
message = ("You are invited to my party, " + (guest_list[3] + "!"))
print(message) 
message = ("You are invited to my party, " + (guest_list[4] + "!"))
print(message)
message = ("You are invited to my party, " + (guest_list[5] + "!"))
print(message)

new_update=("I apologize, but I can only invite two guest.")
print(new_update)

uninvited_guest = guest_list.pop(0)
print("You are univited to the party, " + uninvited_guest + "." )
uninvited_guest = guest_list.pop(1)
print("You are univited to the party, " + uninvited_guest + "." )
uninvited_guest = guest_list.pop(2)
print("You are univited to the party, " + uninvited_guest + "." )



