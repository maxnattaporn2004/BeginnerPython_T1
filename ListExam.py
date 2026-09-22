def showBill():
    print("My Food".center(40,"-"))
    for num in range(len(menuList)):
        print("ชื่ออาหาร : %s ราคาอาหาร : %d Bath"%(menuList[num][0],menuList[num][1]))

def totalPrice():
    pass
    total = 0
    for num in range(len(menuList)):
        total += menuList[num][1]
    return total

def vatShowBill(total):
    vat = total+(total*0.07)
    print("ราคารวม = %f Bath" %vat)

menuList =[]


while True:
    meunName =input("Please enter menu").capitalize()
    if meunName == "Exit":
        print("Thank You")
        break
    else:
        menuPrice = int(input("Please enter price"))
        menuList.append([meunName,menuPrice])


showBill()
vatShowBill(totalPrice())