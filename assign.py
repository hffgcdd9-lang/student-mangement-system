while True:
  print("////Menu////")
  print("1.multi")
  print("2.mini multi table")
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
  else:
    print("Wrong Choice!")
    break