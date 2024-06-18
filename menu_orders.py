menu = {

    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00

}

def main():
    total_cost = 0
    print("Menu:\n")
    for item in menu:
        print(f"{item}: ${menu[item]}")
    print("\n")
    while True:
        try:
            order = input("Item:\n").title().rstrip().lstrip()
            if order.lower().strip() == "end":
                break
            elif order in menu:
                total_cost += menu[order]
                print(f"Total: ${total_cost}")
        except:
            continue

main()