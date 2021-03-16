"""
Program Name: Wk2P2_Mark_Vang
Student Name: Mark Vang
Course: ENTD200 D001 Winter 2021
Instructor: Professor Nigatu
Date: 3/21/2021
Description: This code is an improvment of Wk2P2_Mark_Vang. Instead of using variables, I have used functions,
so that I could recall them at different points in my code. main() is my starting point of my code, it prompts 
for input. If the while-loop condition is met, it moves onto my isinrange(). If the if statment is met, it 
will go to then execute total(). If the condition is not met, it will print that it is not in range. After the 
while loop is ran, it will prompt again if you would like to enter another calculation.

In week 2 I was having the issue of trying to set my conditions in my range statement. I initally had one if, 
three elif, and one else. This week, I was able to condense it to a if and else.

I initially wasn't carrying the values into the functions, so I was getting a lot of errors. For some reason it 
worked without it, but when I made my main(), it started to throw traceback errors.

Copy Wrong: This is my work.
"""

def add(x, y):
    print("The result of ", x, "+", y, "=", x + y)
    #removed this variable "add = x + y:, and replaced it with this function so i can recall it in my total(), 
    #applied to all below.
def sub(x, y):
    print("The result of ", x, "-", y, "=", x - y)

def product(x, y):
    print("The result of ", x, "*", y, "=", x * y)

#two divide functions are used, since we are still not allowing try-except.
def divide(x, y):
    print("The result of ", x, "/", y, "=", x / y)

def divide0(x, y):
    print("The result of ", x, "/", y, "=", x, " You cannot divide by Zero.")

def thankyou():
    print("\nThank you for using my calculator!")

def total(x, y): #This really cleaned up from original function from last week.
    while True:
        if y != 0:
            add(x, y)
            sub(x, y)
            product(x, y)
            divide(x, y)
            thankyou()
            break
        else:
            add(x, y)
            sub(x, y)
            product(x, y)
            divide0(x, y)  # This is still utilizing the while True to accept / 0.
            thankyou()
            break

def isinrange(x, y, low, high): #This sets my range to the input from the user, my if condition allows for either x or y
                                #to be tested againts high/low, as the user may input the numbers in any order.
    if low > x | y or high < x | y: #This allows me to condense my original code to 1 lines, originally I had a 2
                                    #x and y statments.
        print("The input values are outside the input ranges." #My error catch statment.
              "\nPlease check the numbers and try again"
              "\nThank you for using my calculator")
    else:
        total(x, y) #if the if conidtion is not meet, the error message is applied, if it passes, it refers to
                    #my total() and executes that portion of the code.

def main():
    calculate = input("Would you like to use the calculator? Yes or No: ") #This initiates my program to prompt a yes    
    calculate = calculate.lower()   #This makes any variation of Yes to lowercased to meet my while statement.
    while calculate == "yes":   #This is my while loop, it asks for user input, applies it to my main(x, y), low and
                                #high are applied to my isinrange(), then it prints the results and prompts to continue.
        low = int(input("Please enter your Lower range: "))
        high = int(input("Please enter your Higher range: "))
        x = int(input("Please enter your first number: "))
        y = int(input("Please enter your second number: "))
        isinrange(x, y, low, high)
        calculate = input("Would you like to calculate again? Yes or No: ")
        calculate = calculate.lower()   #As long as this is yes, it will loop, this will also prompt if ranges are not
                                        #within the user's ranges they input earlier.
    else:
        print("Have a great day!") #This catches anything that is not a variation of yes.

main()
"""At the very end, I decided to add main(), because this would allow my me to put my while loop
into a function, when I did this, a few of my parameters did not carry over into the functions
so I had to add either x, y, low, or high within the functions."""