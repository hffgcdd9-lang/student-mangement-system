while True:
  print("////Calulator////")
  print("1.multi")
  print("2.mini multi table")
  print("3.add")
  print("4.sub")
  print("5.divide")
  choice = input("Enter your choice:")
  if choice=="1":
      print("Enter 2 numbers")
      num1 = float(input("Enter first number:"))
      num2 = float(input("Enter second number:"))
      result = num1 * num2
      print(f"{num1}*{num2}={result}")
  elif choice=="2":
    i=float(input("Enter number :"))
    for num in range(1,11):
         result = num * i
         print(f"{num}*{i}={result}")
  elif choice=="3":
      print("Enter 2 numbers")
      num1 = float(input("Enter first number:"))
      num2 = float(input("Enter second number:"))
      result = num1 + num2
      print(f"{num1}+{num2}={result}")
  elif choice=="4":
      print("Enter 2 numbers")
      num1 = float(input("Enter first number:"))
      num2 = float(input("Enter second number:"))
      result = num1 - num2
      print(f"{num1}-{num2}={result}")
  elif choice=="5":
      print("Enter 2 numbers")
      num1 = float(input("Enter first number:"))
      num2 = float(input("Enter second number:"))
      result = num1 / num2
      print(f"{num1}/{num2}={result}")
  else:
    print("Wrong Choice!")
    break
