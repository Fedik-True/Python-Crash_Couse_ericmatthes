guest_list = ['justina', 'leos mares', 'michal david', 'lady gaga']
message1 = f"Hello, i invite you {guest_list[0].title()} to a dinner"
message2 = f"Hello {guest_list[1].upper()}, i invite you to my dinner!"
message3 = f"Hi, I invite you to my dinner, hope you will come {guest_list[-2].title()}"
message4 = f"My beloved {guest_list[-1].upper()}, i hope you will come to my dinner"

print(f"{message1}\n{message2}\n{message3}\n{message4}")


remove_guest1 = 'lady gaga'
guest_list.remove(remove_guest1)
guest_list.insert(3, 'Agraelus')

print(
    f"I sadly announce you that {remove_guest1.title()} won't come to the party, but {guest_list[3].title()} said he will come instead! Are you happy {guest_list[0].upper()}, {guest_list[1].upper()}, {guest_list[2].upper()}???"
    )

print("And i just got a call that we will have more space at the table, so i'll find some more people to join us")

guest_list.insert(0, 'Fattypillow'), guest_list.insert(2, 'Neuromant'), guest_list.append('Jovinecko')

print(f"And our newest guests are {guest_list[0].upper()}, {guest_list[2].upper()} and {guest_list[6].upper()}. Are you excited?")
print(len(guest_list))

print("And again we have some changes in plan, unfortunately we now only have space for two people at the table")
print(f"I am sorry but you must leave {guest_list[0].title()}")
guest_list.pop(0)

print(f"I am sorry but you must leave {guest_list[3].title()}")
guest_list.pop(3)

print(f"I am sorry but you must leave {guest_list[4].title()}")
guest_list.pop(4)

print(f"I am sorry but you must leave {guest_list[3].title()}")
guest_list.pop(3)

print(f"I am sorry but you must leave {guest_list[2].title()}")
guest_list.pop(2)

print(f"I am happy that you two are coming, what do you think {guest_list[0].upper()} and {guest_list[1].upper()}")

del(guest_list)[0]
del(guest_list)[0]

print(guest_list)
print(len(guest_list))