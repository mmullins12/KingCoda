# Income Tax/Earnings Calculator (by week)

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    fRate = float(rate)
    fHours = float(hours)
except:
    print("Error. Use Numeric Digits only.")
    quit()

OtRate = 1.5 * fRate 

if fHours > 40 :
    pay = ((fHours - 40) * OtRate) + (40 * fRate)
else:
    pay = fHours * fRate
    
if fHours > 40 : 
    print("Overtime")
else: 
    print("Regular")



print("pay:", pay)
 
tax = (pay * 1.13) - pay
print("Tax:", tax)
net = (pay - tax)
print("Net Income:", net)