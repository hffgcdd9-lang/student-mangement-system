#--GPA Calculator--
from typing import final
student_gpa=3.8
bonus= student_gpa*10
final_score = student_gpa+(bonus/100)
passed = final_score>3.0
print(f"GPA :{student_gpa}")
print(f"Bonus (x10) : {bonus} ")
print(f"Final Score : {final_score:.2f}")
print(f"Passed : {passed}")
# part of candies--------(another question)
candies=13
kids=3
share=candies//kids
remain=candies%kids
print(f"One child take: {share} ")
print(f" remain candies: {remain} ")
#part of money--------(third question)
balance = float(input("Enter your balance: "))
take=float(input("Enter your need of money: "))
update=balance-take
print(f"Your balance is: {update}")
put=float(input("How much do you want to put : "))
print(f"Your put is: {put} ")
print(f"Your money now is: {balance+put}")
