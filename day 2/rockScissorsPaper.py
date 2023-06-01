# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def whatIsIt(num):
  if num < 0 or num > 2: 
    return "You gave a wrong number! Number has to be between 0 and 2"
  choices = ["rock", "scissors", "paper"]
  return choices[num]

#gives back 0-2 at random
def computerChoice():
  return random.randint(0, 2)

def rockScissorsPaper():
  #Code Here
  #ask for a choice of rock paper or scissors 
  
  choice = input("""Pick your fighter:
  rock
  paper
  scissors
  Your fighter is: """)

  # if statement that chekcs if use choice is correct 
  # if choice == "rock":
  #   print("you picked rock!")
  # elif choice == "scissors":
  #   print("you chose scissors!")
  # elif choice == "paper":
  #   print("you picked paper!")
  # else:
  #   print("your response is not valid!")

  if choice == "rock" or choice == "paper" or choice == "scissors":
    print("your response is valid!")
  else:
    print("your repsonse is not valid! please try again!")

  #print random computer response
  # print(whatIsIt(computerChoice()))

  computer_choice = whatIsIt(computerChoice())
  print("computer choice is:")
  print(computer_choice)
  
  if choice == computer_choice:
    print("you guys tied!")
  else:
    if choice == "rock":
      if computer_choice == "paper":
        print("the computer won!")
      if computer_choice == "scissors":
        print("you won!")
    elif choice == "paper":
      if computer_choice == "rock":
        print("you won!")
      if computer_choice == "scissors":
        print("the computer won!")
    elif choice == "scissors":
      if computer_choice == "paper":
        print("you won!")
      if computer_choice == "rock":
        print("the computer won!")

rockScissorsPaper()
