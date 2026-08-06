import sys

print("*" * 20,"Welcome", "*" * 20)
print("*" * 20,"Developed by Mannu", "*" * 20)

def userNameWrite ():
    user_name_input = input("Type Notes here: ")
    with open("UserName.txt" , "a") as userfile :
        userfile.write(f"{user_name_input}\n")
        print("Notes added Successfully!")

def userNameRead ():
    with open("UserName.txt" , "r") as userfile :
        user_list = userfile.read()
        print()
        print(user_list)
        total_users = user_list.splitlines()
        print(f"Total Notes: {len(total_users)}")

while True:
    print()
    print("=" * 20, "=" * 20)
    print("1. To Write ")
    print("2. To Read")
    print("3. To Exit!")
    option = input("Select above options : ")
    if option == '1' :
        userNameWrite()
    elif option == '2' :
        userNameRead()
    elif option == '3' :
        print("Goodbye!")
        sys.exit()
    else:    
        print("\nyou selected invalid options, Try Again!")
        






