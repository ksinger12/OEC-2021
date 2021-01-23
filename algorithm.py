from parseData import getData
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

class PType(enum.Enum):
    Student = 0
    Teacher = 1
    TA = 2

def p_infect(person0, person1, event):
    pass

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
        self.infected = False
    
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
                self.clubs = data['Health Conditions']
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
        return [p for p in self.people if p.infected == True]
    
    def getAllInClass(self, className, time):
        period = timeToPeriod(time)
        if (period == None):
            return []
        return [p for p in self.people if p.classes[period] == className]
    
    def getAllInClassNext(self, className, time):
        period = timeToPeriod(time)
        if (period == None):
            return []
        if period == 0 or period == 2:
            return [p for p in self.people if p.classes[period+1] == className]
        else:
            return []
        
    def getAllInExtraCurricular(self, club):
        return [p for p in self.students if p.clubs != None and club in p.clubs]

class Event:
    def __init__(self):
        pass

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
                newPerson.setInfected(True)
        people.append(newPerson)
        students.append(newPerson)
    for i in range(len(data[1])):
        newPerson = Person(PType.Teacher)
        newPerson.setData(data[1].iloc[i])
        for i in infectedOthers:
            if (i['fname'] == newPerson.fname and i['lname'] == newPerson.lname):
                newPerson.setInfected(True)
        people.append(newPerson)
        teachers.append(newPerson)
    for i in range(len(data[2])):
        newPerson = Person(PType.TA)
        newPerson.setData(data[2].iloc[i])
        for i in infectedOthers:
            if (i['fname'] == newPerson.fname and i['lname'] == newPerson.lname):
                newPerson.setInfected(True)
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
    
    #Iterate over every time step (the periods, lunch, and clubs after school)
    for t in range(len(times)):
        cur_period = times[t]
        
simulate()
    
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