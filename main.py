income = int(input("Enter the family income: "))
if income <= 100000:
    print("Below poverty line")
elif 100000< income <= 500000 :
    print("Middle class family ")
else:
    print("Elite")