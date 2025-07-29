def personal_info_manager():
    person = ("Aissara", 20, "Chonburi", "TH")
    hobbies = []
 
    while True:
        choice = input("Please select choice 1.person 2.add hobby 3.del hobbies 4.edit age 5.Exit : ")
 
        if choice == "1":
            print("Name:", person[0])
            print("Age:", person[1])
            print("City:", person[2])
            print("Country:", person[3])
            print("Hobbies:", hobbies)
 
        elif choice == "2":
            hobby = input("What is your hobby: ")
            hobbies.append(hobby)
 
        elif choice == "3":
            if hobbies:
                removed = hobbies.pop(0)
                print(f"Removed hobby: {removed}")
            else:
                print("No hobbies to delete.")
 
        elif choice == "4":
            person_list = list(person)
            age = int(input("How old are you? : "))
            person_list[1] = age
            person = tuple(person_list)
 
        elif choice == "5":
            print("Exiting program.")
            break
 
        else:
            print("Invalid choice. Please select again.")
 
if __name__ == "__main__":
    personal_info_manager()
 