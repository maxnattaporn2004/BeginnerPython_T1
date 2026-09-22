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

systemMenu = {
                "ข้าวมันไก่":50,"ข้าวผัด":50,"ข้าว":10,"เส้น":15,
                "1":"ข้าวมันไก่","2":"ข้าวผัด","3":"ข้าว","4":"เส้น"
              }
menuList =[]
print("ข้าวมันไก่  = 1")
print("ข้าวผัด    = 2")
print("ข้าว      = 3")
print("เส้น      = 4")
while True:
    meunName =input("Please enter menu").capitalize()
    if meunName == "Exit":
        print("Thank You")
        break
    else:
        menuList.append([systemMenu[meunName],systemMenu[systemMenu[meunName]]])
        print(menuList)


showBill()
vatShowBill(totalPrice())