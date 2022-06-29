
import os
import time

# HEADER
def head():
  time.sleep(.8)
  os.system('cls')
  print("  ___     __     __      ___   __  __   __       __     ____   _____   ____  ") 
  print(" / __)   /__\   (  )    / __) (  )(  ) (  )     /__\   (_  _) (  _  ) (  _ \ ") 
  print("( (__   /(__)\   )(__  ( (__   )(__)(   )(__   /(__)\    )(    )(_)(   )   / ") 
  print(" \___) (__)(__) (____)  \___) (______) (____) (__)(__)  (__)  (_____) (_)\_) \n\n")


# VALIDATE NUMBER INPUT
def checkNumberInput(answer):

  try:
    convert = float(answer)
    if convert > 0 or convert < 1 :
      return answer
      
  except:
    print("Invalid input")
    answer = False
    return answer

# VALIDATE OPERATOR INPUT
def checkOperatorInput(operator):

  if operator in ('+', '-', '/', '*', '%'):
    return operator
  
  print("Invalid operator")
  operator = False
  return operator

# CHECK AND PRINT THE FINAL OUTPUT
def output(computedOutput):
  head()
  print("Your input : ", firstAnswer, operatorAnswer, secondAnswer)

  if computedOutput % 1 == 0:
      print("The answer is : ", int(computedOutput))
  else:
      print("The answer is : ", format(computedOutput, '.2f'))


  
# START

while True:  

  firstAnswer = operatorAnswer = secondAnswer = False

# GET AND VALIDATE 1st NUMBER
  while firstAnswer == False:
    head()
    firstAnswer = checkNumberInput(input("Enter first number : "))
  
# GET AND VALIDATE OPERATOR
  while operatorAnswer == False:
    head()
    print("Your input : ", firstAnswer)
    operatorAnswer = checkOperatorInput(input("Enter operator : "))

# GET AND VALIDATE 2nd NUMBER 
  while secondAnswer == False:
    head()
    print("Your input : ", firstAnswer, operatorAnswer)
    secondAnswer = checkNumberInput(input("Enter second number : "))

  

# START OF CALCULATIONS
  
  if operatorAnswer == '+':
    computedOutput = float(firstAnswer) + float(secondAnswer)
    output(computedOutput)

  elif operatorAnswer == '-':
    computedOutput = float(firstAnswer) - float(secondAnswer)
    output(computedOutput)

  elif operatorAnswer == '/':
    while float(secondAnswer) == 0:
      print("Cannot divided by zero")
      time.sleep(1)
      secondAnswer = False

      while secondAnswer == False:
        head()
        print("Your input : ", firstAnswer, operatorAnswer)
        secondAnswer = checkNumberInput(input("Enter second number : "))
    
    computedOutput = float(firstAnswer) / float(secondAnswer)
    output(computedOutput)

  elif operatorAnswer == '*':
    computedOutput = float(firstAnswer) * float(secondAnswer)
    output(computedOutput)

  else:
    computedOutput = float(firstAnswer) % float(secondAnswer)
    output(computedOutput)
  
  
  
  # END
  input("\nPress enter to continue....")
