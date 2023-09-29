# calculator
from calculator_art import logo
from replit import clear
# add
def add(n1,n2):
  return n1+n2

# sub
def sub(n1,n2):
  return n1-n2

# multiply
def mul(n1,n2):
  return n1*n2

# divide
def div(n1,n2):
  return n1/n2

basic_operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div,
}
def calculator():
  print(logo)
  num1=float(input("Enter the first number: "))
  
  for key in basic_operations:
    print(key)
    
  should_continue=True
  
  while should_continue:
    operation_symbol=input("Pick an operation from the above lines: ")
    num2=float(input("Enter the next number: "))
    
    calculation_func = basic_operations[operation_symbol]
    
    answer=calculation_func(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calulating with the {answer}, or type 'n' to continue to the new calculation.: ")=="y":
      num1=answer
    else:
      should_continue=False
      clear()
      calculator()

calculator()
