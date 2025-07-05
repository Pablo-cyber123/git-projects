import json, os
ruta = "data.json"
actualUser = None

loginMenu = """

    Welcome to the login menu 👤

    1. 🔒 Login
    2. 🔑 Register
    3. ❌ Exit

"""

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def setJson(data):
    global ruta
    try:
        with open(ruta, "w") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(e)
        return

def getJson():
    global ruta
    try:
        with open(ruta, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(e)
        data = []
        setJson([])
    return data

def setId():
    idd = 0
    data = getJson()
    for i in data:
        if i["id"] == idd:
            idd += 1
        else:
            idd = idd
            break
    return idd

def login():
    clearConsole()
    print("🔒 Login")
    global actualUser
    data = getJson()
    if data == []:
        print("❔ No accounts available.")
        input("Continue...")
        return
    user = input("Enter your user name: ")
    if user == "":
        print("❌ User cannot be empty.")
        input("Continue...")
        return
    if any(u["user"] == user for u in data):
        print("This user exists.")
    else:
        print("❌ This user not exists")
        input("Continue...")
        return
    
    for u in data:
        if u["user"] == user:
            id = u["id"]

    password = input("Enter your password: ")
    if password == "":
        print("❌ Password cannot be empty.")
        input("Continue...")
        return
    if data[id]["password"] != password:
        print("❌ The password does not match.")
        input("Continue...")
        return

    actualUser = id
    print("✅ User loged successfuly")
    input("Continue...")

def register():
    clearConsole()
    data = getJson()
    print("🔑 Register")
    if data == []:
        user = input("Enter your user name: ")
        if user == "":
            print("❌ User cannot be empty.")
            input("Continue...")
            return
        elif user.count(" "):
            print("❌ User cannot contain spaces.")
            input("Continue...")
            return
        
        password = input("Enter your password: ")
        if password == "":
            print("❌ Password cannot be empty.")
            input("Continue...")
            return
        elif password.count(" ") > 0:
            print("❌ Password cannot contain spaces.")
            input("Continue...")
            return
        elif len(password) < 4:
            print("❌ Password have to contain four characters.")
            input("Continue...")
            return
        else:
            data.append({"id": 0, "user": user, "password": password, "post": []})
            setJson(data)
            print("✅ User saved successfuly.")
            input("Continue...")
    else:
        user = input("Enter your user name: ")
        if user == "":
            print("❌ User name cannot be empty.")
            input("Continue...")
            return
        elif user.count(" ") > 0:
            print("❌ User cannot contain spaces.")
            input("Continue...")
            return
        elif any(u["user"] == user for u in data):
            print("❌ This User name already exists.")
            input("Continue...")
            return
        
        password = input("Enter your password: ")
        if password == "":
            print("❌ Password cannot be empty.")
            input("Continue...")
            return
        elif password.count(" ") > 0:
            print("❌ Password cannot contain spaces.")
            input("Continue...")
            return
        elif len(password) < 4:
            print("❌ Password have to contain four characters.")
            input("Continue...")
            return
        else:
            data.append({"id": setId(),"user": user, "password": password, "post": []})
            setJson(data)
            print("✅ User saved successfuly.")
            input("Continue...")

while True:
    clearConsole()
    print(loginMenu)
    op = input("Select an option: ")
    if op == "1":
        login()
    elif op == "2":
        register()
    elif op == "3":
        pass
    else:
        print("Invalid option, please try again.")