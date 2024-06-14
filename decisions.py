import time
from datetime import date, time, datetime, timezone

'''
def main():
    while True:
        try:
            grade = float(input("What was your test score out of 100?").replace("%", ""))
            if grade < 0:
                x = 5 > "throw an error!"
            break
        except:
            print("Please enter a valid test score and try again.")
    if grade < 60:
        letter_grade = "F"
    elif grade < 70:
        letter_grade = "D"
    elif grade < 80:
        letter_grade = "C"
    elif grade < 90:
        letter_grade = "B"
    else:
        letter_grade = "A"
    
    if grade < 93 and letter_grade != "F":
        if grade % 10 < 3:
            letter_grade += "-"
        elif grade % 10 > 7:
            letter_grade += "+"
    print(f"Your letter grade: {letter_grade}")

while True:
    main()
    while True:
        try:
            choice = input("Would you like to calculate your letter grade again? (y/n)")
            if choice == ("y" or "yes"):
                break
            elif choice != ("n" or "no"):
                x = 5 > "throw an error!"
            else:
                print("Shutting down...")
                time.sleep(1)
                exit()
        except Exception as e:
            print(e)
            print("Please enter a valid answer and try again.")


def main():
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    while True:
        try:
            month = input("What month is it?")
            if month.lower() not in months:
                x = 5 > "throw an error!"
            month_no = months.index(month) + 1
            print(month_no)
            if month_no == 12 or month_no == 1 or month_no == 2:
                season = "Winter"
            if month_no == 3 or month_no == 4 or month_no == 5:
                season = "Spring"
            if month_no == 6 or month_no == 7 or month_no == 8:
                season = "Summer"
            if month_no == 9 or month_no == 10 or month_no == 11:
                season = "Fall"
            print(f"The season is {season.lower()}")
            break
        except Exception as e:
            print(e)
            print("Please enter a valid month and try again.")
'''

def get_season(month_no):
    if month_no in [12, 1, 2]:
            season = "Winter"
    if month_no in [3, 4, 5]:
        season = "Spring"
    if month_no in [6, 7, 8]:
        season = "Summer"
    if month_no in [9, 10, 11]:
        season = "Fall"
    return season

def main():
    try:
        d = date.today()
        print(f"The date is {d}")
        month_no = d.month
    except Exception as e:
        print(e)
    print(f"The season is {get_season(month_no)}")

while True:
    main()
    while True:
        try:
            choice = input("Would you like to find the season again? (y/n)")
            if choice == ("y" or "yes"):
                break
            elif choice != ("n" or "no"):
                x = 5 > "throw an error!"
            else:
                print("Shutting down...")
                exit()
        except Exception as e:
            print(e)
            print("Please enter a valid answer and try again.")

