
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
    carefulness = 0.6  # high because high supervision
    exposure = 0.8  # high because lots of students in small space
    return probabiity_of_infection(num_students_in_class, exposure, carefulness)


def probabiity_of_infection_in_class_teacher_and_ta(num_students_in_grade):
    carefulness = 0.7  # high because staff are careful
    exposure = 0.6  # high because working together directly
    return probabiity_of_infection(num_students_in_grade, exposure, carefulness)


def probabiity_of_infection_in_class_ta_and_student(num_students_in_grade):
    carefulness = 0.6  # high because staff are careful
    exposure = 0.3  # low because in contact with few of the people
    return probabiity_of_infection(num_students_in_grade, exposure, carefulness)


def probabiity_of_infection_in_class_teacher_and_student(num_students_in_grade):
    carefulness = 0.7  # high because staff are careful
    exposure = 0.3  # low because in contact with few of the people
    return probabiity_of_infection(num_students_in_grade, exposure, carefulness)


def probability_of_infection_switching_classes(num_students_in_first_class, num_students_in_second_class):
    carefulness = 0.5
    exposure = 0.3  # less than in class because exposure time is less
    return probabiity_of_infection(num_students_in_first_class + num_students_in_second_class, exposure, carefulness)


def probability_of_infection_during_lunch_staff(num_staff):
    carefulness = 0.7  # high because staff are careful
    exposure = 0.3  # low because in contact with few of the people
    return probabiity_of_infection(num_staff, exposure, carefulness)


def probability_of_infection_during_lunch_same_grade(num_students_in_grade):
    carefulness = 0.2  # low because little supervision
    exposure = 0.3  # low because in contact with few of the people
    return probabiity_of_infection(num_students_in_grade, exposure, carefulness)


def probability_of_infection_during_lunch_different_grade(num_students_on_lunch_break):
    carefulness = 0.2  # low because little supervision
    exposure = 0.1  # very low because in contact with very few of the people
    return probabiity_of_infection(num_students_on_lunch_break, exposure, carefulness)


def probability_of_infection_during_extra_curricular(extra_curricular, num_students_in_extra_curricular):
    carefulnessAndExposureOfActivities = {
        "Board Game Club": (0.5, 0.5),
        "Football": (0.1, 0.1),  # exposure low because outside
        "Band": (0.5, 0.5),
        "Computer Science Club": (0.5, 0.5),
        "Video Game Club": (0.5, 0.5),
        "Soccer": (0.5, 0.5),
        "Basketball": (0.5, 0.5),
        "Badminton": (0.5, 0.5),
        "Baseball": (0.5, 0.5),
        "Drama Club": (0.5, 0.5),
        "Choir": (0.5, 0.5)
    }
    carefulness, exposure = carefulnessAndExposureOfActivities[extra_curricular]
    return probabiity_of_infection(num_students_in_extra_curricular, exposure, carefulness)
