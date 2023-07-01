class Student:
    def __init__(self,name,surname,gender):
        self.name=name
        self.surname= surname
        self.gender=gender
        self.finished_courses = []
        self.courses_in_progress = []  
        self.grades_dict = {}            

    def add_courses (self,course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  

    def add_grades(self,student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades_dict:
                student.grades_dict[course] +=[grades]
            else:
                student.grades_dict[course] = [grades]
        else:
            print('Ошибка')


class Lecturer(Mentor):
    pass
class Reviewer(Mentor):
    pass

lecturer_1 = Lecturer('Елена','Догузова')
lecturer_1.courses_attached.append('Словарь')

reviewer_1 = Reviewer ('Елизавета','Петрова')
reviewer_1.courses_attached.append('Python')

print(lecturer_1.name)                
print(lecturer_1.surname)            
print(lecturer_1.courses_attached)    

print(reviewer_1.name)              
print(reviewer_1.surname)           
print(reviewer_1.courses_attached)    