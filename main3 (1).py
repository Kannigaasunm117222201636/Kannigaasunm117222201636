class Student:
  def __init__(self,name, roll_number, cgpa):
    self. name=name
    self. roll_number=roll_number
    self. cgpa=cgpa

def sort_students(student_list):
  sorted_students=sorted(student_list, key=lambda student:student.cgpa,reverse=True)
  
  return sorted_students

students=[
  Student("hari", "A123",7.8), 
  Student("suriya", "A125",8.9), 
  Student("mani", "A167", 9.7), 
  Student("dhanesh", "A114", 8.3), 
  ]

sorted_students=sort_students(students)

for student in sorted_students:
  print("Name :{}, Roll_number:{}, CGPA:{}". format(student.name,student.roll_number,
student.cgpa))