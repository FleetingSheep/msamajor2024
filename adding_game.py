'''
Features:

Addition, subtraction, multiplication, division problems

Custom difficulty parameters for all types of problems

Cheat code

TODO: Expanded, algorithmic difficulty beyond 3

Repeat question prevention

TODO: Exponent problems, root problems using fractional exponents

TODO: Negative answers on high difficulties
'''


import random as rand
counter = 0 # number of correct answers
def get_num(length): #for addition, subtraction, and multiplication
    num = ""
    for i in range(length): #concatenates 3 random integers together, which is more robust than a predetermined randint(100, 999) for instance
        if i == 0: #so as to always generate 3 digit numbers and not 099...
            num += str(rand.randint(1, 9))
        else:
            num += str(rand.randint(0, 9))
    return int(num)

def get_right_answer(num1, num2, operator): #get the actual answer depending on operator
    match operator:
        case "+":
            true_answer = num1 + num2
        case "-":
            true_answer = num1 - num2
        case "*":
            true_answer = num1 * num2
        case "/":
            true_answer = num1 / num2
    return true_answer


def get_answer(num1, num2, operator): #prompt answers

    global counter
    true_answer = get_right_answer(num1, num2, operator)
    wrong_counter = 0 #number of incorrect questions, quit asking at third failure


    while True:

        answer = input(f"{num1} {operator} {num2} = ")

        if answer == "cheat": #bypass to check if operations are performing correctly
            print(f"Correct Answer: {num1} {operator} {num2} = {true_answer}")
            counter += 1
            break

        elif not answer.isdigit(): #if not an integer
            print("Enter an integer!")

        else:
            if int(answer) == true_answer:
                print("Correct!\n")
                counter += 1
                break
            else:
                print("Wrong!\n")
                wrong_counter += 1
                if wrong_counter == 3:
                    print(f"Correct Answer: {num1} {operator} {num2} = {true_answer}")
                    break
def main():

    global counter #number of correct answers
    try:

        while True:
            operator = input("Choose your type of problem: Addition (+), subtraction (-), multiplication (*), or division (/):\n").lower().strip()
            if operator in ["+", "-", "*", "/"]:
                break
            else:
                print("Enter the operator using its symbol, not plain text!")


        while True:
            difficulty = input("Choose your difficulty 1, 2 or 3:\n")
            if difficulty in ["1", "2", "3"]:
                difficulty = int(difficulty)
                break
            else:
                print("Invalid input.")
                

        while True:
            question_no = input("How many questions, from 3 to 10?\n")
            if question_no.isdigit():
                question_no = int(question_no)
                if question_no >= 3 and question_no <= 10:
                    break
                else:
                    print("Invalid input.")
            else:
                print("Invalid input.")


        questions_list = [] #prevent repeat questions by adding their num1 and num2 to a list, saving it to here, and checking if they are already present

        for i in range(question_no):
            while True: #this loop goes until a non-repeat question is found



                if operator == "+" or operator == "-":

                    num1 = get_num(difficulty) #get random numbers
                    num2 = get_num(difficulty)

                    if operator == "-":
                        if num1 < num2: #shuffle numbers around such that num1 is greater and avoiding negative answers
                            temp = num2
                            num2 = num1
                            num1 = temp



                if operator == "*": #difficulty one: 1 digit times 1 digit, two is 2 digit times 1 digit,three is 2 digit times 2 digits

                    if difficulty == 3: #if difficulty is 3, reduce the length of num1 to compensate
                        num1 = get_num(difficulty - 1)
                    else:
                        num1 = get_num(difficulty)
                    if difficulty == 1: #prevent difficulty from being 0
                        num2 = get_num(difficulty)
                    else:
                        num2 = get_num(difficulty - 1)



                if operator == "/":
                    do_complex = rand.randint(0, 1) #do a more complex problem for variety on difficulties 2 and 3

                    match difficulty:

                        case 1: #basic problems, usually 2 digit divided by 1 digit

                            while True:
                                num2 = get_num(1) #make sure you're not dividing by 1 lmao
                                if num2 != 1:
                                    break #generate the smaller number first to guarantee that it is divisible
                            num1 = num2 * get_num(1)

                        case 2: #large 2 digit numbers divided by even larger, sometimes 2 digit factors

                            num2 = get_num(1)
                            num1 = num2 * get_num(2)

                        case 3: #3 digit numbers divided by 1, 2, or 3 digit factors

                            num2 = get_num(1) * get_num(1)
                            num1 = num2 * get_num(2)



                temp_question = [num1, num2] #define a temporary identifier for the question

                if temp_question not in questions_list:
                    get_answer(num1, num2, operator) #perform the question
                    questions_list.append(temp_question)
                    break



        grade = (counter / question_no) * 100 #calculate final grade
        print(f"You got {counter} out of {question_no} questions correct: {grade:.2f}%")
        if grade == 100: #if aces
            print("Good job!")

    except Exception as e:
       print(e)

main()