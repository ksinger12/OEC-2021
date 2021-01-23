from parseData import getData
from probabilities import *
import numpy as np
import enum
import math

times = ['p1', 'p2', 'lunch', 'p3', 'p4', 'extra']
def timeToPeriod(time):
    if time == times[0]:
        return 0
    elif time == times[1]:
        return 1
    elif time == times[3]:
        return 2
    elif time == times[4]:
        return 3
    else:
        return None

#Helper functions
def getAgeMultiplier(person0, person1):
    ageDiff = person1.grade - person0.grade
    return pow(1.5, ageDiff/2)

def getHealthMultiplier(person):
    return 1.0 if person.health == None else 1.7

class PType(enum.Enum):
    Student = 0
    Teacher = 1
    TA = 2

def p_infect(person0, person1, event_infection_risk):
    return person1.infected + getHealthMultiplier(person1)*getAgeMultiplier(person0, person1)*(1-person1.infected)*event_infection_risk*person0.infected

class Person:
    def __init__(self, ptype):
        self.ptype = ptype
        self.classes = [None, None, None, None]
        self.grade = -1
        self.fname = ''
        self.lname = ''
        self.clubs = None
        self.health = None
        self.iden_num = -1
        self.infected = 0
    
    #Expects a row from the dataframe for a given person
    def setData(self, data):
        if self.ptype == PType.Student:
            for i in range(4):
                self.classes[i] = data['Period {} Class'.format(i+1)]
            self.fname = data['First Name']
            self.lname = data['Last Name']
            self.grade = data['Grade']
            self.iden_num = data['Student Number']
            if (type(data['Extracurricular Activities']) == str):
                self.clubs = data['Extracurricular Activities'].split(',')
            if (type(data['Health Conditions']) == str):
                self.health = data['Health Conditions']
        elif self.ptype == PType.Teacher:
            for i in range(4):
                self.classes[i] = data['Class']
            self.fname = data['First Name']
            self.lname = data['Last Name']
            self.iden_num = data['Teacher Number']
        elif self.ptype == PType.TA:
            for i in range(4):
                self.classes[i] = data['Period {} Class'.format(i+1)]
            self.fname = data['First Name']
            self.lname = data['Last Name']
    
    def setInfected(self, infected):
        self.infected = infected
        
    def __str__(self):
        return "Name: {} {}\nRole: {}\nInfected: {}".format(self.fname, self.lname, self.ptype, self.infected)
            
class PeopleQuery:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.tas = []
        self.people = []
        
    def setStudents(self, data):
        self.students = data
    def setTeachers(self, data):
        self.teachers = data
    def setTAs(self, data):
        self.tas = data
    def setPeople(self, data):
        self.people = data
        
    def getInfected(self):
        return [p for p in self.people if p.infected == 1]
    
    def getStudentsInClass(self, className, time):
        period = timeToPeriod(time)
        if (period == None):
            return []
        return [p for p in self.students if p.classes[period] == className]
    
    def getStudentsInClassNext(self, className, time):
        period = timeToPeriod(time)
        if (period == None):
            return []
        if period == 0 or period == 2:
            return [p for p in self.students if p.classes[period+1] == className]
        else:
            return []
    
    def getStudentsInGrade(self, grade):
        return [p for p in self.students if p.grade == grade]
    
    def getTeachersInClass(self, className, time):
        period = timeToPeriod(time)
        if (period == None):
            return []
        return [p for p in self.teachers if p.classes[period] == className]
    
    def getTAsInClass(self, className, time):
        period = timeToPeriod(time)
        if (period == None):
            return []
        return [p for p in self.tas if p.classes[period] == className]
    
    def getTAsInClassNext(self, className, time):
        period = timeToPeriod(time)
        if (period == None):
            return []
        if (period == 0 or period == 2):
            return [p for p in self.tas if p.classes[period] == className]
        else:
            return []
    
    def getWorkersInClass(self, className, time):
        period = timeToPeriod(time)
        if (period == None):
            return []
        return [p for p in self.teachers+self.tas if p.classes[period] == className]
    
    def getWorkersInClassNext(self, className, time):
        period = timeToPeriod(time)
        if (period == None):
            return []
        if (period == 0 or period == 2):
            return [p for p in self.teachers+self.tas if p.classes[period] == className]
        else:
            return []
        
    def getAllInExtraCurricular(self, club):
        return [p for p in self.students if p.clubs != None and club in p.clubs]

def simulate():
    data = getData()
    people = []
    students = []
    teachers = []
    tas = []
    
    infectedStudents = data[3].iloc[:,0].tolist()
    infectedOthers = []
    for i in range(len(infectedStudents)):
        if (math.isnan(infectedStudents[i])):
            infectedOthers.append({'fname': data[3].iloc[i]['First Name'], 'lname': data[3].iloc[i]['Last Name']})
    
    #Setup people objects with input data
    for i in range(len(data[0])):
        newPerson = Person(PType.Student)
        newPerson.setData(data[0].iloc[i])
        for j in infectedStudents:
            if newPerson.iden_num == j:
                newPerson.setInfected(1)
        people.append(newPerson)
        students.append(newPerson)
    for i in range(len(data[1])):
        newPerson = Person(PType.Teacher)
        newPerson.setData(data[1].iloc[i])
        for i in infectedOthers:
            if (i['fname'] == newPerson.fname and i['lname'] == newPerson.lname):
                newPerson.setInfected(1)
        people.append(newPerson)
        teachers.append(newPerson)
    for i in range(len(data[2])):
        newPerson = Person(PType.TA)
        newPerson.setData(data[2].iloc[i])
        for i in infectedOthers:
            if (i['fname'] == newPerson.fname and i['lname'] == newPerson.lname):
                newPerson.setInfected(1)
        people.append(newPerson)
        tas.append(newPerson)
    
    #Set inital infected
    for i in range(len(data[3])):
        cur = data[3].iloc[i]
        for j in students:
            if (j.iden_num == cur['Student ID']):
                pass
    
    #Setup people object for data selection
    pquery = PeopleQuery()
    pquery.setStudents(students)
    pquery.setTeachers(teachers)
    pquery.setTAs(tas)
    pquery.setPeople(people)
    
    classes = data[1]['Class'].unique()
    clubs = []
    for i in data[0]['Extracurricular Activities']:
        if (str(i) != 'nan'):
            cur_clubs = i.split(',')
            for j in cur_clubs:
                if j not in clubs:
                    clubs.append(j)
    
    #Iterate over every time step (the periods, lunch, and clubs after school)
    for t in range(len(times)):
        cur_period = times[t]
        
        if (cur_period in ['p1', 'p2', 'p3', 'p4']): #a class period
            for c in classes:
                classSize = len(pquery.getStudentsInClass(c, cur_period) + pquery.getTeachersInClass(c, cur_period) + pquery.getTAsInClass(c, cur_period))
                
                students = pquery.getStudentsInClass(c, cur_period)
                student_infect_prob = probability_of_infection_in_class(classSize)
                for i in range(len(students)):
                    for j in range(len(students)):
                        if i != j:
                            from_student = students[i]
                            to_student = students[j]
                            to_student.infected = p_infect(from_student, to_student, student_infect_prob)
                
                workers = pquery.getWorkersInClass(c, cur_period)
                ta_teacher_infect_prob = probability_of_infection_in_class_teacher_and_ta(classSize)
                for i in range(len(workers)):
                    for j in range(len(workers)):
                        if (i != j):
                            from_worker = workers[i]
                            to_worker = workers[j]
                            to_worker.infected = p_infect(from_worker, to_worker, ta_teacher_infect_prob)
                
                tas_students = pquery.getTAsInClass(c, cur_period) + students
                ta_student_infect_prob = probability_of_infection_in_class_ta_and_student(classSize)
                for i in range(len(tas_students)):
                    for j in range(len(tas_students)):
                        if (i != j):
                            from_ta_student = tas_students[i]
                            to_ta_student = tas_students[j]
                            to_ta_student.infected = p_infect(from_ta_student, to_ta_student, ta_student_infect_prob)
                
                students_teachers = pquery.getTeachersInClass(c, cur_period) + students
                student_teacher_infect_prob = probability_of_infection_in_class_teacher_and_student(classSize)
                for i in range(len(students_teachers)):
                    for j in range(len(students_teachers)):
                        if (i != j):
                            from_student_teacher = students_teachers[i]
                            to_student_teacher = students_teachers[j]
                            to_student_teacher.infected = p_infect(from_student_teacher, to_student_teacher, student_teacher_infect_prob)
                
                if (cur_period in ['p1', 'p3']):
                    tas_students_next = pquery.getTAsInClassNext(c, cur_period) + pquery.getStudentsInClassNext(c, cur_period)
                    switching_class_infect_prob = probability_of_infection_switching_classes(len(tas_students), len(tas_students_next))
                    for i in range(len(tas_students)):
                        for j in range(len(tas_students_next)):
                            prob_to_next = p_infect(tas_students[i], tas_students_next[j], switching_class_infect_prob)
                            prob_for_cur = p_infect(tas_students_next[j], tas_students[i], switching_class_infect_prob)
                            tas_students[i].infected = prob_for_cur
                            tas_students_next[j].infected = prob_to_next
        elif (cur_period == 'lunch'):
            workers = pquery.teachers + pquery.tas
            staff_lunch_infect_prob = probability_of_infection_during_lunch_staff(len(workers))
            for i in range(len(workers)):
                for j in range(len(workers)):
                    if i != j:
                        from_worker = workers[i]
                        to_worker = workers[j]
                        to_worker.infected = p_infect(from_worker, to_worker, staff_lunch_infect_prob)
            
            grades = []
            for g in range(9, 13):
                grade = pquery.getStudentsInGrade(g)
                grades.append(grade)
                grade_lunch_infect_prob = probability_of_infection_during_lunch_same_grade(len(grade))
                for i in range(len(grade)):
                    for j in range(len(grade)):
                        if i != j:
                            from_student = grade[i]
                            to_student = grade[j]
                            to_student.infected = p_infect(from_student, to_student, grade_lunch_infect_prob)
            
            for g in range(len(grades)):
                cur = grades[g]
                other = []
                for i in range(len(grades)):
                    if i != g:
                        other += grades[i]
                grade_lunch_other_infect_prob = probability_of_infection_during_lunch_different_grade(len(cur+grades))
                for i in range(len(cur)):
                    for j in range(len(other)):
                        from_student = cur[i]
                        to_student = other[j]
                        to_student.infected = p_infect(from_student, to_student, grade_lunch_other_infect_prob)
        elif (cur_period == 'extra'):
            for c in clubs:
                students = pquery.getAllInExtraCurricular(c)
                club_infect_prob = probability_of_infection_during_extra_curricular(c, len(students))
                for i in range(len(students)):
                    for j in range(len(students)):
                        if i != j:
                            from_student = students[i]
                            to_student = students[j]
                            to_student.infected = p_infect(from_student, to_student, club_infect_prob)
        
        return pquery, data
        
def getDataForVisualization(pquery, data):
    classes = data[1]['Class'].unique()
    
    periods = []
    for i in range(4):
        cur_period = 'p{}'.format(i+1)
        period = {}
        for c in classes:
            period[c] = []
        for c in classes:
            people = pquery.getStudentsInClass(c, cur_period) + pquery.getTeachersInClass(c, cur_period) + pquery.getTAsInClass(c, cur_period)
            for p in people:
                period[c].append(p)
        periods.append(period)
    return periods
        
pquery, data = simulate()


#"Unit" Tests

# p = Person(PType.Student)
# data = getData()
# p.setData(data[0].iloc[0])

# p = Person(PType.Teacher)
# data = getData()
# p.setData(data[1].iloc[0])

# p = Person(PType.TA)
# data = getData()
# p.setData(data[2].iloc[0])