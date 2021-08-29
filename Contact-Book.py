print("Welcome to Contact Book! :)") 

my_array = []

save = input("If you want to save a contact enter save: ")

if save == "save":
    name = input("Enter the name of the person: ")
    number = input("Enter the phone number of the person: ")
    my_array.append(name)
    my_array.append(number)
    print("Successfully saved the contact! :)")

see = input("If you want to take a look at the saved contacts, enter see: ")

if see == "see":
    for i in my_array:
        print(i)