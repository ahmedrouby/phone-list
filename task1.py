contacts_list = []
while True:
    name = input("Enter your name:\n")
    number = input ("Enter your phone number:\n")
    number_type = input ("Enter your phone number type:\n")
    contact = name +", "+ number +", "+ number_type
    contacts_list.append (contact)
    for i in range(len(contacts_list)):
        print (contacts_list[i])
