class Mentor:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] 
        self.grades_dict_lecturer = {} 


class Student:
    def __init__(self,name,surname,gender):
        self.name=name
        self.surname= surname
        self.gender=gender
        self.finished_courses = []
        self.courses_in_progress = []  
        self.grades_dict_student = {}         
 
    def add_courses (self,course_name):
        self.finished_courses.append(course_name)

    
    def add_grades_lecturer(self, lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades_dict_lecturer:
                lecturer.grades_dict_lecturer[course] += [grades]
            else:
                lecturer.grades_dict_lecturer[course] = [grades]
        else:
            print('Ошибка')


class Lecturer(Mentor):
    pass

class Reviewer(Mentor):
    def add_grades_student(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades_dict_student:
                student.grades_dict_student[course] += [grades]
            else:
                student.grades_dict_student[course] = [grades]
        else:
            print('Ошибка')

student_1= Student('Вася','Пупкин','М')
student_1.courses_in_progress.append('Python')
reviewer_1 = Reviewer ('Иван','Петров') 
reviewer_1.courses_attached.append('Python') 

reviewer_1.add_grades_student(student_1, 'Python', 10)
reviewer_1.add_grades_student(student_1, 'Python', 9)  
reviewer_1.add_grades_student(student_1, 'Python', 10) 

print(student_1.name)
print(student_1.surname)
print(student_1.gender)
print(student_1.courses_in_progress)
print(student_1.grades_dict_student)
print(reviewer_1.name)
print(reviewer_1.surname)
print(reviewer_1.courses_attached)

lecturer_1 = Lecturer('Максим','Середа')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Python-Beckend')

student_2= Student('Кристина','Яземова','Д')
student_2.courses_in_progress.append('Python')
student_3= Student('Элла','Петрова','Д')
student_3.courses_in_progress.append('Python')
student_4= Student('Сергей','Нестеров','М')
student_4.courses_in_progress.append('Python-Beckend')

student_1.add_grades_lecturer(lecturer_1, 'Python', 9)
student_2.add_grades_lecturer(lecturer_1, 'Python', 9)
student_3.add_grades_lecturer(lecturer_1, 'Python', 10)
student_4.add_grades_lecturer(lecturer_1, 'Python-Beckend', 10)

print(lecturer_1.courses_attached)  
print(lecturer_1.grades_dict_lecturer) 