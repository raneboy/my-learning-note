# keep looping until user choose leave
name_list = []

def main_screen():
    """Show The Main Screen"""

    print("*" * 40)
    print("The program function provided: ")
    print("1. Add new name card")
    print("2. Check the all name card list info")
    print("3. Check the name card user info")
    print("")
    print("0. Exit the program")
    print("*" * 40)

def add_new_name_card():
    print("-" * 60)

    print("Start to add new card name")

    # Input name
    while True:
        name = input("Please enter name: ")
        bool_reply = True
        # Check whether the name is valid
        for character in name:
            if not character.isalpha():
                if not character.isspace():
                    print("Are you sure your name has character other than alphabet?")

                    while True:
                        reply = input("yes/no?: ")
                        if reply == "yes" or reply == 'y':
                            bool_reply = True
                            break  # break the inner while loop
                        elif reply == "no" or reply == 'n':
                            bool_reply = False
                            break
                        else:
                            print("Please reply yes or y to confirm, no or n to reject")

                    # Break the for loop
                    break
                else:
                    continue

        if bool_reply:
            break

    # Input age
    while True:
        try:
            age = int(input("Please enter age: "))
            if age < 0:
                print("Are you sure your age is negative value?")
            elif age > 150:
                print("Are you sure you are not elf?")
            else:
                break
        except ValueError:
            print("Please Enter Integer")

    # Input phone number
    while True:
        try:
            phone = int(input("Please enter phone number: "))
            if len(str(phone)) < 4 or len(str(phone)) > 20:
                print("The phone number is too short or too long please re-enter")
            else:
                break
        except ValueError:
            print('Please enter correct phone number without "-" or "." or alphabet or etc')

    # Input email
    while True:
        email = input("Please enter email address: ")
        if '@' not in email or "." not in email:
            print("Are you sure this is the correct email?")
        elif email.count('@') > 1:
            print("There are two or more @ symbol in the email list")
        else:

            # Check whether the email name valid
            email_part = email.split('@')
            number_count = 0
            for character in email_part[0]:
                if character.isnumeric():
                    number_count += 1

            if number_count == len(email_part[0]):
                print("Are you sure your email name is all integer?")
            else:
                break

    name_card = {"name": name,
                 "age": age,
                 "phone": phone,
                 "email": email}

    name_list.append(name_card)

    print("-" * 60)


def check_name_list():
    print("-" * 60)
    if not name_list:
        print("The name list is empty")
        print("-" * 60)
        return
    else:
        print("-" * 80)
        print("%-20s%-20s%-20s%-30s" % ("name", "age", "phone", "email"))
        print("-" * 80)
        for card in name_list:
            print("%-20s%-20s%-20s%-30s" % (card["name"], card["age"], card["phone"], card["email"]))
        print("-" * 80)

def check_name_and_info():
    print("-" * 60)
    if not name_list:
        print("The name list is empty")
    else:
        bool_reply = True
        while True:
            name = input("Please enter the name you want to check: ")

            # Find out the user and info
            name_list_index_count = -1
            for card in name_list:
                name_list_index_count += 1
                if name == card["name"]:
                    print("-" * 80)
                    print("%-20s%-20s%-20s%-30s" % (card["name"], card["age"], card["phone"], card["email"]))
                    print("-" * 80)

                    print("What is your next action? \n1. Edit this member\n2. Delete this member")
                    print("3. Check other name\n4. Exit")

                    # Further action on this user
                    try:
                        action_two = int(input("Please enter the number based on what you want to do: "))
                        if action_two == 1:
                            count = 0
                            value_name = ['name', 'age', 'phone', 'email']
                            while count <= 3:
                                while True:
                                    reply = input("Do you want to change %s?(y/n): " % (value_name[count]))
                                    if reply == 'y' or reply == 'yes':
                                        temp_val = input("Please enter your new %s: " % value_name[count])
                                        card[value_name[count]] = temp_val
                                        break
                                    elif reply == "n" or reply == 'no':
                                        break
                                    else:
                                        print("Please enter correct command")

                                count += 1

                        elif action_two == 2:
                            while True:
                                reply = input("Do you want to delete this card member?(y/n): ")
                                if reply == 'y' or reply == 'yes':
                                    name_list.pop(name_list_index_count)
                                    break
                                elif reply == "n" or reply == 'no':
                                    break
                                else:
                                    print("Please enter correct command")
                        elif action_two == 3:
                            check_name_and_info()
                            break
                        elif action_two == 4:
                            break
                        else:
                            print("Please enter correct command")
                    except ValueError:
                        print("Please enter correct action number")

                    break

            else:
                print("No this name.")
                while True:
                    reply = input("Are you want to continue on searching. yes/no?: ")
                    if reply == "yes" or reply == 'y':
                        check_name_and_info()
                        break
                    elif reply == "no" or reply == 'n':
                        break
                    else:
                        print("Please reply yes or y to confirm, no or n to reject")

            if bool_reply:
                break

        print("-" * 40)

def main():
    while True:
        main_screen()

        try:
            action = int(input("Please choose your action: "))
            if action == 1:
                print("You chose to add new name card")
                add_new_name_card()
            elif action == 2:
                print("You chose to open name list")
                check_name_list()
            elif action == 3:
                print("You chose to check name card user info")
                check_name_and_info()
            elif action == 0:
                print("Thank for using this program")
                break
            else:
                print("Please chose correct action number")
        except ValueError:
            print("Please enter the value 1, 2, 3, or 0")


if __name__ == "__main__":
    main()
