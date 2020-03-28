print("Electricity bill estimator")


# collect base user inputs for estimation
price_per_kWh = float(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
days_in_billing = float(input("Enter number of billing days: "))

bill_total = ((price_per_kWh/100)*daily_use_kwh)*days_in_billing  # equation for bill total

print("Estimated bill: ${:.2f}".format(bill_total))  # print bill total
