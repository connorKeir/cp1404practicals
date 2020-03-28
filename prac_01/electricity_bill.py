TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print("Electricity bill estimator 2.0")

    # collect base user inputs for estimation
    # price_per_kWh = float(input("Enter cents per kWh: "))  # removed when updated to 2.0
    tariff = float(input("Which tariff? 11 or 31: "))
    if tariff == 11:
        tariff = float(TARIFF_11)
    elif tariff == 31:
        tariff = float(TARIFF_31)

    daily_use_kwh = float(input("Enter daily use in kWh: "))
    days_in_billing = float(input("Enter number of billing days: "))
    print(tariff)
    bill_total = bill_calculator(tariff, daily_use_kwh, days_in_billing)

    print("Estimated bill: ${:.2f}".format(bill_total))  # print bill total


def bill_calculator(cost, daily_use, period):
    return (cost * daily_use) * period  # equation bill estimate


main()
