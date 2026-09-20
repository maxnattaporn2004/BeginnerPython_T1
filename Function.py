def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        choice = menuSelect()
        if choice == 1 :
            print(gradeCalculator())
        elif choice == 2 :
            print(priceCalculator())

    else:
        print("Login Failed")

def showMenu():
    print("----- iShop -----")
    print("1. gradeCalculator")
    print("2. Price Calculator")

def menuSelect():
    showMenu()
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)
def gradeCalculator():
    score = int(input("Score:"))
    if score >= 80:
        return ("Grade A")
    elif score >= 75:
        return ("Grade B+")
    elif score >= 70:
        return ("Grade B")
    elif score >= 65:
        return ("Grade C+")
    elif score >= 60:
        return ("Grade C")
    elif score >= 55:
        return ("Grade D+")
    elif score >= 50:
        return ("Grade D")
    else:
        return ("Grade F")
login()