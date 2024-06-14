add = lambda a, b : float(a) + float(b)
def main():
    no1 = input("Input first number:")
    no2 = input("Input second number:")
    try:
        print(add(no1, no2))
    except Exception as e:
        print(e)
while True:
    main()