
# r0 is the average number of people that an infected person infects in one interaction.
# However, different interactions have different risks.
r0 = 3

# This descirbes the probability that an infected person infects another given person.
# The factors are:
#   -num_people  - the number of people involved in the event
#   -exposure    - the natural risk factor relating to the activity that takes place during the event
#   -carefulness - the safety precautions that the involved individuals take during the event
def probabiity_of_infection(num_people, exposure, carefulness):
    return exposure * (1 - carefulness) * r0 / num_people

def probability_of_infection_in_class(num_students_in_class):
    carefulnesss = 0.5
    risk = 1 - carefulnesss
    return risk * r0 / num_students_in_class

def probability_of_infection_switching_classes(num_students_in_first_class, num_students_in_second_class):
    carefulness = 0.5
    risk = 0.5 * (1 - carefulnesss) # Less than sitting in class because there is less exposure time
    return risk * (r0 / (num_students_in_first_class + num_students_in_second_class))

def probability_of_infection_during_lunch_same_grade(num_students_in_grade):
    carefulnesss = 0.5
    risk = 1 - carefulnesss
    return risk * r0 / num_students_in_grade

def probability_of_infection_during_extra_curricular(extra_curricular, num_students_in_extra_curricular):
    carefulnessAndExposureOfActivities = {
        "board board club": ()
        "football": 
        "band":
        "computer science club":
        "video game club":
        "soccer":
        "basketball":
        "badminton":
        "baseball":
        "drama club":
        ""
    }
    return risk * r0 / num_students_in_extra_curricular


probabilities = {
    "r0 in class": 3, # This means that 
    "switching classes": 0.05,
    "lunch same grade": 1, # 
    "extra curricular": 1,
    "overlap of teachers": 1,
    "overlap of TAs": 1,
}


p = probabilities
