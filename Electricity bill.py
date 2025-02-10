Units = int(input("Enter amount of units used:\n"))
if Units < 50:
    amount = Units * 2.6
    tax = 25
elif Units <= 100:
    amount = 130 + ((Units-50) * 3.25)
    tax = 35
elif Units <= 200:
    amount = 130 + 162.50 + ((Units - 100) * 5.26)
    tax = 45
else:
    amount = 130 + 162.50 + 526 + ((Units-200) * 8.45)
    tax = 75

total = amount + tax
print(total)