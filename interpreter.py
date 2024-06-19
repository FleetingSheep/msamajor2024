
'''
def main():
    while True:
        try:
            answer = input("Expression: ")
            answer = answer.split(" ")
            if answer[0].isdigit() and answer[1] in ("+", "-", "*", "/", "**", "%", "//") and answer[2].isdigit() and len(answer) == 3 and answer[2] != 0:
                x = int(answer[0])
                y = answer[1]
                z = int(answer[2])
                match y:
                    case "+": #add
                        output = x + z
                    case "-": #subtract
                        output = x - z
                    case "*": #multiply
                        output = x * z
                    case "/": #division
                        output = x / z
                    case "**": #exponentiation
                        output = x ** z
                    case "%": #modulation
                        output = x % z
                    case "//": #floor division
                        output = x // z
                print(f"{output:.1f}")
        except Exception as e:
            print(e)
            continue
'''
def do_operation(x, z, operation):
    match operation:
        case "+": #add
            output = x + z
        case "-": #subtract
            output = x - z
        case "*": #multiply
            output = x * z
        case "/": #division
            output = x / z
        case "**": #exponentiation
            output = x ** z
        case "%": #modulation
            output = x % z
        case "//": #floor division
            output = x // z
    return output

def find_p(answer):
    print(answer)
    for item in answer:
        start = item.find("(")
        if start != -1:
            if item != "(":
                temp_item = []
                for letter in item:
                    temp_item.append(letter)
                temp_item.insert(temp_item.index(item), " ")
                temp_item = "".join(temp_item)
                answer.remove(item)
        end = item.find(")")
        if end != -1:
            if item != ")":
                temp_item = []
                for letter in item:
                    temp_item.append(letter)
                temp_item.insert(temp_item.index(item), " ")
                answer.remove(item)
    print(answer)
        


def main():
    while True:
        #try:
            answer = input("Expression: ")
            answer = answer.split(" ")
            find_p(answer)
            for item in answer:
                if item not in ("+", "-", "*", "/", "**", "%", "//", "(", ")"):
                    item = float(item)
            answer = do_operation(x, z, y)
            print(f"{answer:.2f}")
        #except Exception as e:
        #    print(e)
        #    continue
main()