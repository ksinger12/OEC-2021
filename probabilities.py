# r0 is the average number of people that an infected person infects in one interaction.
# However, different interactions have different risks.
r0 = 3

# Additional protection that comes with wearing a mask (~15%), social distancing (~20% - low because we're assuming this can only be maintained to such an extent)
wearing_mask = 1 - 0.15
social_distancing = 1 - 0.2

# On/Off Switch for protection measures
protection_measures = {
    "on": True,
    "off": False
}

# Lenth of exposure (incubation periods)
#   -Regular -> calling this ~100% of exposure - 45 minutes
#   -Transition -> ~11% of exposure compare to regular - 5 minutes -> (5/45) = ~0.11
time_of_period = {
    "Regular": 1,
    "Transition": 0.11
}


# This descirbes the probability that an infected person infects another given person.
# The factors are:
#   -num_people  - the number of people involved in the event
#   -exposure    - the natural risk factor relating to the activity that takes place during the event
#   -carefulness - the safety precautions that the involved individuals take during the event

def probability_of_infection(num_people, exposure, carefulness, mask, distancing):
    probability = exposure * (1 - carefulness) * r0 / num_people

    if mask and distancing:
        return probability*wearing_mask*social_distancing
    elif mask:
        return probability*wearing_mask
    elif distancing:
        return probability*social_distancing

    return probability


def probability_of_infection_in_class(num_students_in_class):
    carefulness = 0.8  # high because high supervision
    exposure = 0.8  # high because lots of students in small space
    return probability_of_infection(num_students_in_class, exposure*time_of_period["Regular"], carefulness, protection_measures["on"], protection_measures["on"])


def probability_of_infection_in_class_teacher_and_ta():
    carefulness = 0.9  # high because staff are careful
    exposure = 0.6  # high because working together directly
    return probability_of_infection(2, exposure*time_of_period["Regular"], carefulness, protection_measures["on"], protection_measures["on"])


def probability_of_infection_in_class_ta_and_student(num_students_in_class):
    carefulness = 0.6  # high because staff are careful
    exposure = 0.5  # medium because the TA will have to move from student to student
    return probability_of_infection(num_students_in_class, exposure*time_of_period["Regular"], carefulness, protection_measures["on"], protection_measures["on"])


def probability_of_infection_in_class_teacher_and_student(num_students_in_class):
    carefulness = 0.7  # high because staff are careful
    exposure = 0.3  # low because in contact with few of the people
    return probability_of_infection(num_students_in_class, exposure*time_of_period["Regular"], carefulness, protection_measures["on"], protection_measures["on"])


def probability_of_infection_switching_classes(num_students_in_first_class, num_students_in_second_class):
    carefulness = 0.3  # all leaving class and entering class at same time
    exposure = 0.3  # less than in class because exposure time is less
    return probability_of_infection(num_students_in_first_class + num_students_in_second_class, exposure*time_of_period["Transition"], carefulness, protection_measures["on"], protection_measures["off"])


def probability_of_infection_during_lunch_staff(num_staff):
    carefulness = 0.7  # high because staff are careful
    exposure = 0.3  # low because in contact with few of the people
    return probability_of_infection(num_staff, exposure*time_of_period["Regular"], carefulness, protection_measures["off"], protection_measures["on"])


def probability_of_infection_during_lunch_same_grade(num_students_in_grade):
    carefulness = 0.2  # low because little supervision
    exposure = 0.4  # low because in contact with only a few people
    return probability_of_infection(num_students_in_grade, exposure*time_of_period["Regular"], carefulness, protection_measures["off"], protection_measures["off"])


def probability_of_infection_during_lunch_different_grade(num_students_on_lunch_break):
    carefulness = 0.2  # low because little supervision
    exposure = 0.1  # very low because in contact with very few of the people
    return probability_of_infection(num_students_on_lunch_break, exposure*time_of_period["Regular"], carefulness, protection_measures["off"], protection_measures["off"])


# Analysis:
# -Boards Game club, students are in a close proximity but are being supervised
# -Football, students are outdoors though will be more relaxed, far apart & are being supervised
# -Band, students in close proximtiy but are being supervised
# -Computer science club, students do not need to be in close proximity, and are being supervised
# -Video game club, in close proximity due to console and are being supervised
# -Soccer, players are mostly spaces, students are supervised
# -Basketball, players are minimally spaces, students are supervised
# -Badminton, players are spaced and are supervised
# -Baseball, players are fairly spaced and outdoor, students are supervised
# -Drama club, members are in somewhat close proximity, students are supervised
# -Choir, members are in somewhat close proximity, students are supervised

def probability_of_infection_during_extra_curricular(extra_curricular, num_students_in_extra_curricular):
    carefulnessAndExposureOfActivities = {
        "Board Game Club": (0.7, 0.7, protection_measures["on"], protection_measures["off"]),
        "Football": (0.7, 0.3, protection_measures["off"], protection_measures["on"]),
        "Band": (0.7, 0.6, protection_measures["on"], protection_measures["off"]),
        "Computer Science Club": (0.8, 0.5, protection_measures["on"], protection_measures["on"]),
        "Video Game Club": (0.7, 0.6, protection_measures["on"], protection_measures["off"]),
        "Soccer": (0.7, 0.3, protection_measures["off"], protection_measures["on"]),
        "Basketball": (0.3, 0.5, protection_measures["off"], protection_measures["off"]),
        "Badminton": (0.7, 0.5, protection_measures["off"], protection_measures["on"]),
        "Baseball": (0.8, 0.4, protection_measures["off"], protection_measures["on"]),
        "Drama Club": (0.7, 0.5, protection_measures["on"], protection_measures["off"]),
        "Choir": (0.7, 0.6, protection_measures["on"], protection_measures["on"])
    }
    carefulness, exposure, mask, distancing = carefulnessAndExposureOfActivities[
        extra_curricular]
    return probability_of_infection(num_students_in_extra_curricular, exposure*time_of_period["Regular"], carefulness, mask, distancing)
