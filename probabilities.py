
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
    carefulnesss = 0.8 # high because high supervision
    exposure = 0.8 # high because lots of students in small space
    return probabiity_of_infection(num_students_in_class, exposure, carefulness)

def probability_of_infection_switching_classes(num_students_in_first_class, num_students_in_second_class):
    carefulnesss = 0.5
    exposure = 0.3
    return probabiity_of_infection(num_students_in_first_class + num_students_in_second_class, exposure, carefulness)

def probability_of_infection_during_lunch_same_grade(num_students_in_grade):
    carefulnesss = 0.2 # low because little supervision
    exposure = 0.3 # low because in contact with few of the people
    return probabiity_of_infection(num_students_in_grade, exposure, carefulness)

def probability_of_infection_during_lunch_different_grade(num_students_on_lunch_break):
    carefulnesss = 0.2 # low because little supervision
    exposure = 0.1 # very low because in contact with very few of the people
    return probabiity_of_infection(num_students_on_lunch_break, exposure, carefulness)

def probability_of_infection_during_extra_curricular(extra_curricular, num_students_in_extra_curricular):
    carefulnessAndExposureOfActivities = {
        "board board club": (0.5, 0.5), # 
        "football": (0.1, 0.1), # exposure low because outside
        "band": (0.5, 0.5), #
        "computer science club": (0.5, 0.5), #
        "video game club": (0.5, 0.5), #
        "soccer": (0.5, 0.5), #
        "basketball": (0.5, 0.5), #
        "badminton": (0.5, 0.5), #
        "baseball": (0.5, 0.5), #
        "drama club": (0.5, 0.5), #
    }
    carefulness, exposure = carefulnessAndExposureOfActivities[extra_curricular]
    return probabiity_of_infection(num_students_in_class, exposure, carefulness)
