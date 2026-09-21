distance = int(input())
price = 0

if 0 < distance < 2:
    price =  distance * 35.5
    # 2-10
elif 1 < distance <= 10:
    price = ((distance - 1) * 5.50) + 35
    # 11-20
elif 10 < distance <= 20:
    price = 9 * 5.50 + 35 + ((distance - 10) * 6.50)
    # 21-40
elif 20 < distance <= 40:
    price = 9 * 5.50 + 35 + 10 * 6.50 + ((distance - 20) * 7.50)
    # 41-60
elif 40 < distance <= 60:
    price = 9 * 5.50 + 35 + 10 * 6.50 + 20 * 7.50 + ((distance - 40) * 8.00)
    # 61-80
elif 60 < distance <= 80:
    price = 9 * 5.50 + 35 + 10 * 6.50 + 20 * 7.50 + 20 * 8.00 + ((distance - 60) * 9.00)
# 80 UP
elif distance > 80:
    price = 9 * 5.50 + 35 + 10 * 6.50 + 20 * 7.50 + 20 * 8.00 + 20 * 9.00 + ((distance - 80) * 10.50)

print(price)



