
def create_menu():
    menu = {}
    data_file = open("menu.txt")
    for line in data_file:
         new_line = line.split(",")
         item = new_line[0].replace("'", "")
         price = float(new_line[1].replace("\n", ""))
         menu[item] = price
    return menu


def main():
    menu = create_menu()
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