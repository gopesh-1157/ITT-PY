class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  

    def display(self):
        print()
        print(f"Name: {self.name}")
        print("Marks: ", end="") 
    
        for m in self.marks:
            print(m, end=" ")
    
try:
    n = int(input("Enter number of students: "))
    all_students = []

    for i in range(n):
        print(f"\n--- Entering details for Student {i+1} ---")
        name = input("Enter Name: ")
        marks_input = list(map(int, input("Enter 3 marks (separated by space): ").split()))
        if len(marks_input) != 3:
            print("Enter exactly 3 marks")

        student_obj = Student(name, marks_input)
        all_students.append(student_obj)

    print("\n--- Student Details ---")
    for s in all_students:
        s.display()

except ValueError:
    print("Invalid input!")
