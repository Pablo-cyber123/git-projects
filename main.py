import json 
ruta = "database.json"
actualUser = None

loginMenu = """

    Welcome to the login menu 👤

    1. 🔒 Login
    2. 🔑 Register
    3. ❌ Exit

"""

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

def register():
    data = getJson()
    if data == []:
        user = input("Enter your user name: ")
        if user == "":
            print("User cannot be empty.")
            return
        elif user.count(" "):
            print("User cannot contain spaces.")
            return
        
        password = input("Enter your password: ")
        if password == "":
            print("Password cannot be empty.")
            return
        elif password.count(" ") > 0:
            print("Password cannot contain spaces.")
            return
        elif len(password) < 4:
            print("Password have to contain four characters.")
            return
        else:
            data.append({"id": 0, "user": user, "password": password, "post": ""})
            setJson(data)
            print("User saved successfuly.")
    else:
        user = input("Enter your user name: ")
        if user == "":
            print("User name cannot be empty.")
            return
        elif user.count(" ") > 0:
            print("User cannot contain spaces.")
            return
        elif any(u["user"] == user for u in data):
            print("This User name already exists.")
            return
        
        password = input("Enter your password: ")
        if password == "":
            print("Password cannot be empty.")
            return
        elif password.count(" ") > 0:
            print("Password cannot contain spaces.")
            return
        elif len(password) < 4:
            print("Password have to contain four characters.")
            return
        else:
            data.append({"id": setId(),"user": user, "password": password, "post": ""})
            setJson(data)
            print("User saved successfuly.")

while True:
    print(loginMenu)
    op = input("Select an option: ")
    if op == "1":
        pass
    elif op == "2":
        register()
    elif op == "3":
        pass
    else:
        print("Invalid option, please try again.")