def main():
    due = 50
    print("Vending Machine\n-----------------")
    while True:
        try:
            if due <= 0:
                print(f"Change Owed: {abs(due)}")
                break 
            coin = int(input(f"Amount Due: {due} \nInsert Coin:\n"))
            if coin in (1, 5, 10, 25):
                due -= coin
        except:
            continue
main()