from parseData import getData
import numpy as np
import enum
import math

times = ['p1', 'p2', 'lunch', 'p3', 'p4', 'extra']

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
                self.clubs = data['Extracurricular Activities']
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

class Event:
    def __init__(self):
        pass

def simulate():
    data = getData()
    people = []
    
    #Setup people objects
    for i in range(len(data[0])):
        newPerson = Person(PType.Student)
        newPerson.setData(data[0].iloc[i])
        people.append(newPerson)
    for i in range(len(data[1])):
        newPerson = Person(PType.Teacher)
        newPerson.setData(data[1].iloc[i])
        people.append(newPerson)
    for i in range(len(data[2])):
        newPerson = Person(PType.TA)
        newPerson.setData(data[2].iloc[i])
        people.append(newPerson)
        
    #
    
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