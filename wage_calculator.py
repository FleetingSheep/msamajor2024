
import time

def get_pay_advice():

    #obtain hours worked, ask again if invalid
    while True:
        try:
            hours = input("Hours worked daily?")
            hours = float(hours)
            if hours < 0:
                print("Please enter a positive number of hours, and try again.")
            elif hours > 24:
                print("More than 24 hours a day is not possible. Please try again.")
            else:
                break
        except:
            print("Please enter a positive number of hours, and try again.")

    #obtain hourly wage, ask again if invalid
    while True:
        try:
            wage = input("Hourly wage?")
            wage = float(wage)
            if wage < 0:
               print("Please enter a positive wage, and try again.")
            else:
                break
        except:
            print("Please enter a positive wage, and try again.")

    #obtain days worked per year, ask again if invlaid
    while True:
        try:
            days = input("Days worked per year?")
            days = int(days)
            if days < 0:
                print("Please enter a positive number of days, and try again.")
            elif days > 365:
                print("That's just not possible dude")
            else:
                break
        except:
            print("Please enter a positive number of days, and try again.")

    #obtain tax rate, ask again if invalid
    while True:
        try:
            tax = input("Tax rate, in percentage?").replace("%", "")
            tax = float(tax)
            if tax < 0:
                print("Please enter a positive tax rate, and try again.")
            elif tax < 1:
                print("Please enter the tax rate in whole percents, and try again (i.e. 12 for 12%).")
            elif tax > 100:
                print("A tax rate higher than 100 percent is not possible. Please try again.")
            else:
                break
        except:
            print("Please enter a positive tax rate and try again.")

    #fake loading :)
    print("\nProcessing...\n")
    time.sleep(1)

    #calculations

    total_hours = days * hours
    annual_wage = wage * hours * days
    daily_earnings = hours * wage
    yearly_tax = annual_wage * (tax / 100)
    total_annual_wage = annual_wage - yearly_tax

    #pay advice
    print("Pay advice: \n \n")
    print(f"Hours worked: {hours:.2f}")
    print(f"Annual hours worked: {total_hours:.2f}")
    print(f"Hourly wage: ${wage:.2f}")
    print(f"Daily earnings: ${daily_earnings:.2f}")
    print(f"Annual wage before taxes: ${annual_wage:.2f}")
    print(f"Yearly tax amount: ${yearly_tax:.2f}")
    print(f"Annual wages after taxes: ${total_annual_wage:.2f}")

#repeat program if desired
while True:
    get_pay_advice()
    while True:
        breakout = input("Would you like to use the calculator again? (y/n)")
        if breakout == "n" or breakout == "no":
            exit()
        elif breakout != "yes" and breakout != "y":
            print("Please enter a valid input (y/n, yes or no) and try again.")
        else:
            break
        