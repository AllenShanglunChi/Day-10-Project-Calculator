#Calculator

from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide 
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key) 
  
  end_game = False
  while not end_game:
    symbol = input("Pick an operation symbol: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[symbol](num1, num2) 
    
    print(f"{num1} {symbol} {num2} = {answer}")
    should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if should_continue == "y":
      num1 = answer
    else:
      end_game = True
      calculator()

calculator()


  
  