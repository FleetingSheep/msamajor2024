
def main():
    while True:
        try:
            no = int(input("Highway number?").lower().replace("i-", ""))
            if no < 1:
                print("Please enter a positive highway number and try again.")
                continue
            elif no % 2 == 0:
                direction = "east to west"
            else:
                direction = "north to south"
            print(f"This highway goes {direction}.")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Please enter a valid highway number and try again.")
    return direction

while True:
    main()
    try:
        choice = input("Would you like to find the highway direction again?")
        if choice == "y" or choice == "yes":
            continue
        elif choice == "n" or choice == "no":
            break
        else:
            x = 5 > "throw an error"
    except:
        print("Please enter a valid answer and try again.")

