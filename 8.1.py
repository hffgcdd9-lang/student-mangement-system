from operator import index
i=True
toDoList=[]
while i==True:
 print("***Menu***")
 print(f"1.add\n2.remove\n3.update\n4.exit")
 choice=int(input("Enter your choice:"))

 if choice==1:
    toDoList.append(input("Add:"))
 elif choice==2:
    if not toDoList:
     print("Error, you must add items fristly to remove")

    elif toDoList[0]!="":
      toDoList.remove(input("Remove:"))

 elif choice==3:
    print(toDoList)
 elif choice==4:
      i=False
      print("Exiting")
 else:
    print("Invalid choice")
