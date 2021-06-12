print("Welcome to the tip calculator ")

pay_amount = int(input("What was the total bill "))
tip = int(input("What percenttage would you like to give 10 , 12, or 15? "))
person = int(input("How many people to split the bill "))


tip_cal = tip/100
total_tip = tip_cal*pay_amount
total_bill = total_tip + pay_amount
final_bill = int(total_bill/person)
print(f"Each person should pay {final_bill}")






