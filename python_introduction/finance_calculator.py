#finance_calculator
monthly_income=float (input("enter your monthly income"))
monthly_expenses=float (input("enter your monthly expenses"))
#calculate monthly savings
monthly_savings=monthly_income-monthly_expenses
#calculate annual savings with 5% interest
Annual_savings=monthly_savings*12 + (monthly_savings*12*0.05)
print("Your Annual_savings is:", Annual_savings)
