# Conditional logic

def MySwitch(credits_at_pass, credits_at_defer, credits_at_fail):
    if credits_at_pass == 120 and credits_at_defer == 0 and credits_at_fail == 0:
        print("Progress")
        return 1

    elif credits_at_pass == 100 and credits_at_defer == 20 and credits_at_fail == 0:
        print("Progress – module trailer")
        return 2

    elif credits_at_pass == 100 and credits_at_defer == 0 and credits_at_fail == 20:
        print("Progress – module trailer")
        return 2

    elif credits_at_pass == 80 and credits_at_defer == 40 and credits_at_fail == 0:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 80 and credits_at_defer == 20 and credits_at_fail == 20:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 80 and credits_at_defer == 0 and credits_at_fail == 40:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 60 and credits_at_defer == 60 and credits_at_fail == 0:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 60 and credits_at_defer == 40 and credits_at_fail == 20:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 60 and credits_at_defer == 20 and credits_at_fail == 40:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 60 and credits_at_defer == 0 and credits_at_fail == 60:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 40 and credits_at_defer == 80 and credits_at_fail == 0:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 40 and credits_at_defer == 60 and credits_at_fail == 20:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 40 and credits_at_defer == 40 and credits_at_fail == 40:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 40 and credits_at_defer == 20 and credits_at_fail == 60:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 40 and credits_at_defer == 0 and credits_at_fail == 80:
        print("Exclude")
        return 4

    elif credits_at_pass == 20 and credits_at_defer == 100 and credits_at_fail == 0:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 20 and credits_at_defer == 80 and credits_at_fail == 20:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 20 and credits_at_defer == 60 and credits_at_fail == 40:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 20 and credits_at_defer == 40 and credits_at_fail == 60:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 20 and credits_at_defer == 20 and credits_at_fail == 80:
        print("Exclude")
        return 4

    elif credits_at_pass == 20 and credits_at_defer == 0 and credits_at_fail == 100:
        print("Exclude")
        return 4

    elif credits_at_pass == 0 and credits_at_defer == 120 and credits_at_fail == 0:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 0 and credits_at_defer == 100 and credits_at_fail == 20:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 0 and credits_at_defer == 80 and credits_at_fail == 40:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 0 and credits_at_defer == 60 and credits_at_fail == 60:
        print("Do not progress – module retriever")
        return 3

    elif credits_at_pass == 0 and credits_at_defer == 40 and credits_at_fail == 80:
        print("Exclude")
        return 4

    elif credits_at_pass == 0 and credits_at_defer == 20 and credits_at_fail == 100:
        print("Exclude")
        return 4
    elif credits_at_pass == 0 and credits_at_defer == 0 and credits_at_fail == 120:
        print("Exclude")
        return 4
    else:
        print("Invalid Grade")

# Function for grade calculation
def FindGrade():
    Student = 1
    Count = [0, 0, 0, 0]
    quitP = False
    while not quitP:
        Range = False
        credits_at_pass = 0
        credits_at_defer = 0
        credits_at_fail = 0
        credit = [0, 20, 40, 60, 80, 100, 120]
        try:
            credits_at_pass = int(input("Enter credits_at_pass for student " + str(Student) + " : "))
            if credits_at_pass in credit:
                credits_at_defer = int(input("Enter credits_at_defer " + str(Student) + " : "))
                if credits_at_defer in credit:
                    credits_at_fail = int(input("Enter credits_at_fail " + str(Student) + " : "))
                    if credits_at_fail in credit:
                        Range = True
            if not Range:
                print("\nRange error! Try again\n")
                continue
            elif credits_at_pass + credits_at_defer + credits_at_fail != 120:
                print("\nTotal incorrect! Try again\n")
                continue
            else:
                Option = MySwitch(credits_at_pass, credits_at_defer, credits_at_fail)
                if Option == 1:
                    Count[0] += 1
                elif Option == 2:
                    Count[1] += 1
                elif Option == 3:
                    Count[2] += 1
                else:
                    Count[3] += 1
                Status = input("\nEnter 'Q' to Exit or Any Key to Continue\n")
                Status = Status.lower()
                if Status == "q":
                    quitP = True
                    print("Progress          trailer          retriever          Exclude")
                    for i in range(Student):
                        if Count[0] > 0:
                            print("    *             ", end="")
                            Count[0] -= 1
                        else:
                            print("                  ", end="")
                        if Count[1] > 0:
                            print("    *             ", end="")
                            Count[1] -= 1
                        else:
                            print("                  ", end="")
                        if Count[2] > 0:
                            print("    *             ", end="")
                            Count[2] -= 1
                        else:
                            print("                  ", end="")
                        if Count[3] > 0:
                            print("    *             ")
                            Count[3] -= 1
                        else:
                            print("                  ")

                    print(str(Student) + " outcomes in total. ")
                else:
                    Student += 1

        except ValueError:
            print("\nIntegers required! Try again\n")
            continue


FindGrade()
