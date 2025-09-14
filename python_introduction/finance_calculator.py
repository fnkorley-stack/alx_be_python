#finance_calculator
monthly_income=float (input("Enter your monthly income:"))
monthly_expenses=float (input("enter your monthly expenses:"))
#calculate monthly savings
monthly_savings=monthly_income-monthly_expenses
#calculate annual savings with 5% interest
Annual_savings=monthly_savings*12 
Project_Annual_Savings= Annual_savings*0.05 + Annual_savings
print("Your Annual_savings is:", Annual_savings)
print("Your Projected_Annual_savings is:", Project_Annual_Savings)
