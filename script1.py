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