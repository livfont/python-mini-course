def shopper():
  shoppingList = {}
  product = ""

  total = 0

  while product != "stop":
    # ask user for a product they want to add
    product = input("Enter a product you want to buy: ")

    # ask user for the price
    price = float(input("Enter the price of the product: "))

    total += price

    # add item to the shoppingList
    shoppingList[product] = price

  shoppingList.pop("stop")

  # print shoppingList
  print(shoppingList)

  print(shoppingList.keys())

  # print total
  print(total)

shopper()