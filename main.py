# Saqqaf Al-Yazidi
# TP075880
def get_users():
    user = []
    with open("users.txt", "r") as file:
        for line in file:
            data = line.strip().split("\t")
            userid = data[0]
            name = data[1]
            password = data[2]
            type = data[3]
            user.append(userid + name + password + type)
    return user

def authenticate_user(userid, password):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            user_data = line.strip().split()
            if len(user_data) == 4 and user_data[0] == userid and user_data[2] == password:
                return user_data[3]  # Return the user type
    return None  # User not found or incorrect credentials

def is_userid_exists(userid):
    with open("users.txt", "r") as user_file:
        users = user_file.readlines()
        for user in users:
            if user.split('\t')[0] == userid:
                return True
    return False

def add_new_user():
    while True:
        userid = input("Please enter the User ID (letters and numbers only): ")
        if userid.isalnum() and not is_userid_exists(userid):
            break
        elif is_userid_exists(userid):
            print("User ID already exists. Please choose a different User ID.")
        else:
            print("Invalid User ID. It must contain only letters and numbers.")
            continue

    while True:
        password = input("Please enter the password (at least 4 characters, letters and numbers only, no spaces): ")
        if len(password) >= 4 and password.isalnum():
            break
        else:
            print("Invalid password. It must be at least 4 characters long, contain only letters and numbers, and have no spaces.")
            continue

    while True:
        name = input("Please enter your name (letters only, spaces allowed if there are letters): ")
        if any(char.isalpha() for char in name) and all(char.isalpha() or char.isspace() for char in name):
            break
        else:
            print("Invalid name. The name must contain letters, and spaces are allowed only between letters.")
            continue

    while True:
        user_type = input("Please enter the user type (admin, staff): ").lower()
        if user_type in ['admin', 'staff']:
            break
        else:
            print("Invalid user type. Please enter 'admin' or 'staff'.")
            continue

    # Append the new user data to the userdata.txt file
    with open("users.txt", "a") as user_file:
        user_file.write(f"{userid}\t{name}\t{password}\t{user_type}\n")

    print("New user added successfully.")
 
def modify_user():
    # Taking user input
    userid_to_modify = input("Enter the user ID to modify: ")
    new_name = input("Enter the new name: ")
    new_password = input("Enter the new password: ")
    new_user_type = input("Enter the new user type: ")

    # Reading the data from the file
    with open('users.txt', 'r') as user_file:
        lines = user_file.readlines()

    # Modifying the name, password, and user type of the specified user
    modified = False
    for i, line in enumerate(lines):
        values = line.strip().split('\t')
        if len(values) == 4:  # Check if there are enough values to unpack
            userid, _, _, _ = values
        if userid == userid_to_modify:
            lines[i] = f"{userid}\t{new_name}\t{new_password}\t{new_user_type}\n"
            modified = True

    # Writing the modified data back to the file
    if modified:
        with open('users.txt', 'w') as user_file:
            user_file.writelines(lines)
        print(f"User {userid_to_modify} modified successfully.")
    else:
        print("User not found.")

def search_user(): 

    with open('users.txt', 'r') as file:
        lines = file.readlines()
        
    # Printing all user IDs
    print("Available User IDs:")
    for line in lines:
        userid, name, password, user_type = line.strip().split('\t')
        print(userid)
    
    user_id_to_search = input("Enter the user ID to search: ")

    user_found = False
    for i, line in enumerate(lines):
        userid, name, password, user_type = line.strip().split('\t')
        
        if userid == user_id_to_search:
            user_found = True
            print(f"User Found: {userid}\t{name}\t{password}\t{user_type}")

            action = input("Enter 'delete' to remove the user, 'modify' to update the user details, or any other key to exit: ")

            if action.lower() == 'delete':
                lines.pop(i)
                print(f"User {userid} deleted.")

            elif action.lower() == 'modify':
                new_username = input("Enter the new username: ")
                new_password = input("Enter the new password: ")
                new_user_type = input("Enter the new user type: ")
                lines[i] = f"{userid}\t{new_username}\t{new_password}\t{new_user_type}\n"
                print(f"User {userid} modified.")

            # Writing the modified data back to the file
            with open('users.txt', 'w') as file:
                file.writelines(lines)

            break  # exit the loop once the user is found and the action is performed

    if not user_found:
        print("User not found.")

def delete_user():
    # Open the file in read mode
    with open('users.txt', 'r') as file:
        # Read all the lines from the file
        lines = file.readlines()

    # Create a dictionary to store the username as the key and the entire line as the value
    user_lines = {}

    # Iterate over each line in the file
    for line in lines:
        # Split the line into a list of strings
        user_info = line.split()

        # Add the line to the user_lines dictionary with the username as the key
        user_lines[user_info[0]] = line

    # Ask the user for the username they want to delete
    username_to_delete = input("Enter the username of the user you want to delete: ")

    # If the username exists in the user_lines dictionary
    if username_to_delete in user_lines:
        # Get the line to be deleted
        line_to_delete = user_lines[username_to_delete]

        # Create a list to store the lines of the file excluding the line to be deleted
        new_lines = []

        # Iterate over each line in the file
        for line in lines:
            # If the current line does not match the line to be deleted
            if line != line_to_delete:
                # Add the line to the new_lines list
                new_lines.append(line)

        # Open the file in write mode
        with open('users.txt', 'w') as file:
            # Write all the lines in the new_lines list to the file
            file.writelines(new_lines)
            print("User succefuly deleted.")
    else:
        print("Username not found.")

def get_supplier_codes():
    try:
        with open("suppliers.txt", "r") as file:
            supplier_codes = [line.split(',')[0] for line in file.readlines()]
            return supplier_codes
    except FileNotFoundError:
        return []

def get_existing_item_codes():
    try:
        with open("ppe.txt", "r") as file:
            item_codes = [line.split(',')[0] for line in file.readlines()]
            return item_codes
    except FileNotFoundError:
        return []

def stock_ppe_item():
    valid_item_codes = ["HC", "FS", "MS", "GL", "GW", "SC"]
    supplier_codes = get_supplier_codes()
    existing_item_codes = get_existing_item_codes()

    print("Available item codes:")
    for code in valid_item_codes:
        print(code)

    while True:
        item_code = input("Please enter the item code from the list above: ")
        if item_code in valid_item_codes and item_code not in existing_item_codes:
            break
        elif item_code in existing_item_codes:
            print("This item code already exists. Please enter a unique item code.")
        else:
            print("Invalid item code. Valid codes are HC, FS, MS, GL, GW, SC.")

    item_name = ""
    if item_code == "HC":
        item_name = "Head Cover"
    elif item_code == "FS":
        item_name = "Face Shield"
    elif item_code == "MS":
        item_name = "Mask"
    elif item_code == "GL":
        item_name = "Gloves"
    elif item_code == "GW":
        item_name = "Gown"
    elif item_code == "SC":
        item_name = "Shoe Covers"

    print(f"Item name for item code {item_code} is: {item_name}")

    print("Available supplier codes:")
    for code in supplier_codes:
        print(code)

    while True:
        supplier_code = input("Please enter the supplier code from the list above: ")
        if supplier_code in supplier_codes:
            break
        else:
            print("Invalid supplier code. Please enter a code from the existing suppliers.")

    while True:
        quantity_ordered = input("Please enter the quantity of the items in stock: ")
        if quantity_ordered.isdigit() and int(quantity_ordered) > 0:
            quantity_ordered = int(quantity_ordered)
            break
        else:
            print("Invalid quantity. It must be a positive number.")

    with open("ppe.txt", "a") as file:
        file.write(f"{item_code},{supplier_code},{quantity_ordered},{item_name}\n")

def supply_ppe_items():
    # Taking user input
    available_item_codes = set()
    with open('ppe.txt', 'r') as file:
        for line in file:
            item_code, _, _, _ = line.strip().split(',')[:4]
            available_item_codes.add(item_code)

    if not available_item_codes:
        print("No items available for supply.")
        return

    print("Available item codes for supply:")
    for item_code in available_item_codes:
        print(item_code)

    # Taking user input for item to supply
    item_code_to_modify = input("Enter the item code to supply: ")

    # Check if the entered item code is valid
    if item_code_to_modify not in available_item_codes:
        print("Invalid item code. Please enter a valid item code.")
        return

    while True:
        quantity_to_add = int(input("Enter the quantity of boxes to add (should be a number above 1): "))
        if quantity_to_add > 1:
            break
        else:
            print("Invalid quantity. Please enter a number above 1.")
            
    supply_date = input("Enter the supply date (YYYY-MM-DD): ")

    # Reading the data from the file
    with open('ppe.txt', 'r') as file:
        lines = file.readlines()

    modified = False
    for i, line in enumerate(lines):
        item_code, supplier_code, quantity_ordered, item_name = line.strip().split(',')[:4]
        if item_code == item_code_to_modify:
            new_quantity = int(quantity_ordered) + quantity_to_add
            lines[i] = f"{item_code},{supplier_code},{new_quantity},{item_name}\n"
            modified = True

            # Record the transaction with a plus sign if quantity increases
            quantity_change = f"+{quantity_to_add}" if quantity_to_add > 0 else quantity_to_add
            with open('transactions.txt', 'a') as trans_file:
                trans_file.write(f"{item_code},{supplier_code},{quantity_change},{supply_date}\n")

    # Writing the modified data back to the file
    if modified:
        with open('ppe.txt', 'w') as file:
            file.writelines(lines)
        print(f"Quantity of item code {item_code_to_modify} from supplier {supplier_code} increased by {quantity_to_add}.")
    else:
        print("Item not found.")

def distribute_ppe_item():
    # Reading and displaying available item codes from the file
    available_item_codes = set()
    with open('ppe.txt', 'r') as file:
        for line in file:
            item_code, _, _, _ = line.strip().split(',')[:4]
            available_item_codes.add(item_code)

    if not available_item_codes:
        print("No items available for distribution.")
        return

    print("Available item codes for distribution:")
    for item_code in available_item_codes:
        print(item_code)

    # Taking user input for item to distribute
    item_code_to_distribute = input("Enter the item code to distribute: ")

    # Check if the entered item code is valid
    if item_code_to_distribute not in available_item_codes:
        print("Invalid item code. Please enter a valid item code.")
        return

    while True:
        quantity_to_distribute = int(input("Enter the quantity of boxes to distribute (should be a number above 1): "))
        if quantity_to_distribute > 1:
            break
        else:
            print("Invalid quantity. Please enter a number above 1.")

    hospital_code_to_distribute = input("Enter the hospital code: ")
    distribution_date = input("Enter the distribution date (YYYY-MM-DD): ")

    # Checking if the hospital code is valid
    with open('hospitals.txt', 'r') as hospital_file:
        hospital_codes = [line.strip().split(',')[0] for line in hospital_file.readlines()]
        if hospital_code_to_distribute not in hospital_codes:
            print("Invalid hospital code.")
            return

    # Reading the data from the ppe file
    with open('ppe.txt', 'r') as ppe_file:
        lines = ppe_file.readlines()

    # Distributing the quantity of the specified item
    distributed = False
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        item_code, supplier_code, quantity_ordered, item_name = data[:4]  # Include the item_name
        if item_code == item_code_to_distribute:
            if int(quantity_ordered) >= quantity_to_distribute:
                lines[i] = f"{item_code},{supplier_code},{int(quantity_ordered) - quantity_to_distribute},{item_name}\n"  # Include item_name
                distributed = True

                # Recording the transaction with a plus sign if quantity increases
                quantity_change = f"-{quantity_to_distribute}" if quantity_to_distribute > 0 else quantity_to_distribute
                with open('transactions.txt', 'a') as trans_file:
                    trans_file.write(f"{item_code},{hospital_code_to_distribute},{quantity_change},{distribution_date}\n")
            else:
                print("Not enough stock to distribute.")
                print(f"Current stock for item code {item_code_to_distribute}: {quantity_ordered}")
                return

    # Writing the modified data back to the ppe file
    if distributed:
        with open('ppe.txt', 'w') as ppe_file:
            ppe_file.writelines(lines)
        print(f"Quantity of item code {item_code_to_distribute} distributed to hospital {hospital_code_to_distribute} decreased by {quantity_to_distribute}.")
    else:
        print("Item not found.")

def supplier_list():
    while True:
        supplier_code = input("Please enter the supplier code (Two capital letters): ")
        if len(supplier_code) == 2 and supplier_code.isalpha() and supplier_code.isupper():
            break
        else:
            print("Invalid supplier code. It must be two capital letters.")
            continue

    while True:
        supplier_name = input("Please enter the supplier name (Letters and spaces allowed): ")
        if any(char.isalpha() for char in supplier_name) and all(char.isalpha() or char.isspace() for char in supplier_name):
            break
        else:
            print("Invalid supplier name. The name must contain letters, and spaces are allowed only between letters.")
            continue


    while True:
        supplier_contact = input("Please enter the supplier contact number (At least 7 digits): ")
        if supplier_contact.isdigit() and len(supplier_contact) >= 7:
            break
        else:
            print("Invalid contact number. It must be at least 7 digits long and contain only numbers.")
            continue

    while True:
        supplier_email = input("Please enter the supplier's email ID (Should end with .com): ")
        if supplier_email.endswith('.com'):
            break
        else:
            print("Invalid email ID. It must end with .com.")
            continue

    with open("suppliers.txt", "a") as file:
        file.write(f"{supplier_code},{supplier_name},{supplier_contact},{supplier_email}\n")

def hospital_list():
    while True:
        hospital_code = input("Please enter the hospital code (Two capital letters): ")
        if len(hospital_code) == 2 and hospital_code.isalpha() and hospital_code.isupper():
            break
        else:
            print("Invalid hospital code. It must be two capital letters.")
            continue

    while True:
        hospital_name = input("Please enter the hospital name (Letters and spaces allowed): ")
        if any(char.isalpha() for char in hospital_name) and all(char.isalpha() or char.isspace() for char in hospital_name):
            break
        else:
            print("Invalid hospital name. The name must contain letters, and spaces are allowed only between letters.")
            continue


    while True:
        hospital_contact = input("Please enter the hospital contact number (At least 7 digits): ")
        if hospital_contact.isdigit() and len(hospital_contact) >= 7:
            break
        else:
            print("Invalid contact number. It must be at least 7 digits long and contain only numbers.")
            continue

    while True:
        hospital_email = input("Please enter the hospital's email ID (Should end with .com): ")
        if hospital_email.endswith('.com'):
            break
        else:
            print("Invalid email ID. It must end with .com.")
            continue

    with open("hospitals.txt", "a") as file:
        file.write(f"{hospital_code},{hospital_name},{hospital_contact},{hospital_email}\n")

def read_inventory(filename="ppe.txt"):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

def display_menu():
    print("\nItem Inventory Tracking")
    print("1. Total available quantity of all items")
    print("2. Items with stock quantity less than 25 boxes")
    print("3. Track available quantity for a particular item")
    print("4. Exit")

def display_total_inventory():
    inventory = read_inventory()
    inventory.sort(key=lambda x: x[2])  # Sorting by item code in ascending order
    for item in inventory:
        print(f"Item Code: {item[0]}, Item Name: {item[3]}, Quantity: {item[2]} boxes.")

def display_low_stock():
    inventory = read_inventory()
    low_stock_found = False  # Flag to check if any low stock item is found
    for item in inventory:
        # Ensure the quantity field is not empty and is numeric before attempting conversion
        if item[2].isdigit() and int(item[2]) < 25:
            print(f"Item Code: {item[0]}, Item Name: {item[3]}, Quantity: {item[2]} boxes.")
            low_stock_found = True  # Set the flag to True if a low stock item is found

    if not low_stock_found:  # If the flag is still False, no low stock item was found
        print("No low stock items.")

def track_item():
    valid_item_codes = ["HC", "FS", "MS", "GL", "GW", "SC"]
    while True:
        item_code = input("Enter item code (HC, FS, MS, GL, GW, SC): ")
        if item_code in valid_item_codes:
            inventory = read_inventory()
            for item in inventory:
                if item[0] == item_code:
                    print(f"Item Code: {item[0]}, Item Name: {item[3]}, Quantity: {item[2]} boxes.")
                    return
            print("Item not found.")
        else:
            print("Invalid item code. Please enter a valid code (HC, FS, MS, GL, GW, SC).")

def item_inventory_tracking():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            display_total_inventory()
        elif choice == '2':
            display_low_stock()
        elif choice == '3':
            track_item()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def search_ppe_item():
    # Read available item codes from ppe.txt
    available_item_codes = set()
    with open('ppe.txt', 'r') as ppe_file:
        for line in ppe_file:
            item_code, _, _, _ = line.strip().split(',')[:4]
            available_item_codes.add(item_code)

    # Prompt the user to enter a valid item code
    print("Available item codes:")
    for item_code in available_item_codes:
        print(item_code)

    item_code_to_search = input("Enter the item code to search: ")

    # Check if the entered item code is valid
    if item_code_to_search not in available_item_codes:
        print("Invalid item code. Please enter a valid item code from above.")
        return

    # Initialize variables to keep track of the sum of transactions
    total_received = 0
    total_distributed = 0

    # Read and search transactions in transactions.txt
    print("\nTransaction Details:")
    with open('transactions.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            item_code, entity_code, quantity, date = line.strip().split(',')
            quantity = int(quantity)

            # Check if the item code matches
            if item_code == item_code_to_search:
                if quantity > 0:
                    # Item supplied by a supplier
                    total_received += quantity
                    entity_type = "Boxes receievd from Suppliers"
                elif quantity < 0:
                    # Item distributed to a hospital
                    total_distributed -= quantity  # Convert negative quantity to positive
                    entity_type = "Boxes distrubited to Hospitals"

                # Print the individual transaction
                print(f"Date: {date}, {entity_type}: {entity_code}, Quantity: {abs(quantity)} boxes.")

    # Print the sum of transactions
    print(f"Total boxes Received: {total_received}")
    print(f"Total boxes Distributed: {total_distributed}")

def ordinal_number(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def main_menu():
    option = input("To start the Inventory creation please select (1) or select (2) to exit the program: ")
    if option == "1":
        num_item = 3
        nums_item = 6
        supplier_counter = 1
        hospital_counter = 1
        item_counter = 1

        for i in range(num_item):
            supplier_list()
            print(f"{ordinal_number(supplier_counter)} supplier information created successfully!")
            supplier_counter += 1

        for i in range(num_item):
            hospital_list()
            print(f"{ordinal_number(hospital_counter)} hospital information created successfully!")
            hospital_counter += 1

        for i in range(nums_item):
            stock_ppe_item()
            print(f"{ordinal_number(item_counter)} stock information created successfully!")
            item_counter += 1

    elif option == "2":
        while True:
            exit()
    else:
        print("\nInvalid Option, Please try again.")
        main_menu()

def sub_menu():    
    print(end="\n")
    print(" WELCOME TO THE INVENTORY MANAGEMENT SYSTEM FOR PERSONAL PROTECTIVE EQUIPMENT (PPE) ")
    print("====================================================================================")
    print("1. Sign up")
    print("2. Login")
    print("3. Exit")

    option = input("Enter your choice: ")

    while True:
        if option == "1":
            add_new_user()
            return sub_menu()
        elif option == "3":
            print("Exiting")
            break
        elif option == "2":
            # User authentication
            userid = input("User ID: ")
            password = input("Password: ")
            user_type = authenticate_user(userid, password)

            if user_type is None:
                print("Incorrect user ID or password.")
                return sub_menu()

            print("Login successful.")

            # Access control based on user type
            if user_type == "admin":
                print(f"Access granted: ADMIN {userid}")
                # Display admin menu with all tasks
                while True:
                    print("\n1. Add a new User.")
                    print("2. Modify a User.")
                    print("3. Search Users.")
                    print("4. Delete a User.")
                    print("5. Supply PPE Items.")
                    print("6. Distribute PPE Items.")
                    print("7. Item inventory tracking.")
                    print("8. Search PPE Items.")
                    print("9. Exit.")

                    choice = int(input("Please select an operation from above: "))

                    if choice == 1:
                        add_new_user()
                    elif choice == 2:
                        modify_user()
                    elif choice == 3:
                        search_user()
                    elif choice == 4:
                        delete_user()
                    elif choice == 5:
                        supply_ppe_items()
                    elif choice == 6:
                        distribute_ppe_item()
                    elif choice == 7:
                        item_inventory_tracking()
                    elif choice == 8:
                        search_ppe_item()
                    elif choice == 9:
                        print("Exiting the program.")
                        exit()  # This terminates the entire program
                    else:
                        print("Invalid choice. Please choose from the list above.")


            elif user_type == "staff":
                print(f"Access granted: STAFF {userid}")
                # Display inventory-checker menu with relevant tasks
                while True:
                    print("\n1. Supply PPE Items.")
                    print("2. Distribute PPE Items")
                    print("3. Item inventory tracking.")
                    print("4. Search PPE Items")
                    print("5. Exit")

                    choice = int(input("Please select an operation from above: "))

                    if choice == 1:
                        supply_ppe_items()
                    elif choice == 2:
                        distribute_ppe_item()
                    elif choice == 3:
                        item_inventory_tracking()
                    elif choice == 4:
                        search_ppe_item()
                    elif choice == 5:
                        print("Exiting the program.")
                        exit()  # This terminates the entire program
                    else:
                        print("Invalid choice. Please choose from the list above.")
        else:
            print("Option is unavailable try again!")
            return sub_menu()

sub_menu()
