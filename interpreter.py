
def main():
    while True:
        try:

            answer = input("Expression: ")
            answer = answer.split(" ")
            if answer[0].isdigit() and answer[1] in ("+", "-", "*", "/", "**") and answer[2].isdigit() and len(answer) == 3 and answer[2] != 0:
                x = int(answer[0])
                y = answer[1]
                z = int(answer[2])
                match y:
                    case "+":
                        output = x + z
                    case "-":
                        output = x - z
                    case "*":
                        output = x * z
                    case "/":
                        output = x / z
                    case "**":
                        output = x ** z
                print(f"{output:.1f}")
        except Exception as e:
            print(e)
            continue


main()