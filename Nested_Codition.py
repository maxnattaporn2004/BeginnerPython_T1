username = input("Enter your username: ")
password = input("Enter your password: ")
unsernameT = "Admin"
passwordT = "12345"
if username == unsernameT and password == passwordT:
    print("Login Successful")
    print("Welcome " + unsernameT)
    print("1 : Grade calculate")
    print("2 : Vat calculate")
    userSelect = int(input("Enter your choice: "))
    if userSelect == 1:
        score = int(input("Score:"))
        if score >= 80:
            print("Grade A")
        elif score >= 75:
            print("Grade B+")
        elif score >= 70:
            print("Grade B")
        elif score >= 65:
            print("Grade C+")
        elif score >= 60:
            print("Grade C")
        elif score >= 55:
            print("Grade D+")
        elif score >= 50:
            print("Grade D")
        else:
            print("Grade F")
    elif userSelect == 2:
        price = int(input("Enter your price: "))
        vat = 0.07
        result = price + (price * vat)
        print("ราคาสุทธิ",result)
else:
    print("Login Failed")

print("Bye :D")