def showBill():
    result = 0
    print("My Food".center(40,"-"))
    for num in range(len(menuList)):
        print("ชื่ออาหาร : %s ราคาอาหาร : %d Bath"%(menuList[num],priceList[num]))

def totalPrice():
    total = 0
    for num in range(len(priceList)):
        total += priceList[num]
    return total

def vatShowBill(total):
    vat = total+(total*0.07)
    print("ราคารวม = %f Bath" %vat)

menuList =[]
priceList = []

while True:
    meunName =input("Please enter menu").capitalize()
    if meunName == "Exit":
        print("Thank You")
        break
    else:
        menuPrice = int(input("Please enter price"))
        menuList.append(meunName)
        priceList.append(menuPrice)

showBill()
vatShowBill(totalPrice())