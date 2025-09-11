basic_pay=float(input("Enter the basic pay:"))
hra=0.2*basic_pay
ta=0.5*basic_pay
salary=basic_pay+hra+ta
print("HRA:",hra)
print("TA:",ta)
print("Total Salary:",salary)