username =input("Enter your username: ")
password = input("Enter your password: ")
usernameT = "User1"
passwordT = "Password"
if username == usernameT and password == passwordT:
    print("Login Successful")
    print("Welcome " + usernameT)
    print("===== Welcome To MAMAX SHOP =====")
    print("รายการสินค้าชิ้นที่ 1 : ", "Pen" + "    " + "ราคา" + " " + "10THB")
    print("รายการสินค้าชิ้นที่ 2 : ", "Apple" + "  " + "ราคา" + " " + "12THB")
    print("รายการสินค้าชิ้นที่ 3 : ", "Banana" + " " + "ราคา" + " " + "30THB")
    print("รายการสินค้าชิ้นที่ 4 : ", "mouse" + "  " + "ราคา" + " " + "100THB")
    print("=================================")
    userAddItem = int(input("Enter your choice: "))
    amount = int(input("Enter your amount: "))
    if userAddItem == 1:
        result = amount * 10
        print("รายการสินค้าชิ้นที่ 1 : ", "Pen","จำนวน ",amount,"ชิ้น")
        print("ราคารวม",result)
    if userAddItem == 2:
        result = amount * 12
        print("รายการสินค้าชิ้นที่ 2 : ", "Apple","จำนวน ",amount,"ชิ้น")
        print("ราคารวม",result)
    if userAddItem == 3:
        result = amount * 30
        print("รายการสินค้าชิ้นที่ 3 : ", "Banana","จำนวน ",amount,"ชิ้น")
        print("ราคารวม", result)
    if userAddItem == 4:
        result = amount * 100
        print("รายการสินค้าชิ้นที่ 4 : ", "mouse","จำนวน ",amount,"ชิ้น")
        print("ราคารวม", result)
else:
    print("Login Failed")