# HUI3 Health Utility Scoring System

constant_1 = 1.371
constant_2 = 0.371

dictCoefficient = {"Vision": [1.00, 0.98, 0.89, 0.84, 0.75, 0.61],
                   "Hearing": [1.00, 0.95, 0.89, 0.80, 0.74, 0.64],
                   "Speech": [1.00, 0.94, 0.89, 0.81, 0.68],
                   "Ambulation": [1.00, 0.93, 0.86, 0.73, 0.65, 0.58],
                   "Dexterity": [1.00, 0.95, 0.88, 0.76, 0.65, 0.56],
                   "Emotion": [1.00, 0.95, 0.85, 0.64, 0.46],
                   "Cognition": [1.00, 0.92, 0.95, 0.83, 0.60, 0.42],
                   "Pain": [1.00, 0.96, 0.90, 0.77, 0.55]

}

def HealthScore (vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    """
    return health score using HUI3

    """
    if not(vision in range(1, 7)):
        raise ValueError('vision level can only take 1, 2, 3, 4, 5, or 6')
    if not (hearing in range(1, 7)):
        raise ValueError('hearing level can only take 1, 2, 3, 4, 5, or 6')
    if not (speech in range(1, 6)):
        raise ValueError('speech level can only take 1, 2, 3, 4, or 5')
    if not (ambulation in range(1, 7)):
        raise ValueError('ambulation level can only take 1, 2, 3, 4, 5, or 6')
    if not (dexterity in range(1, 7)):
        raise ValueError('dexterity level can only take 1, 2, 3, 4, 5, or 6')
    if not (emotion in range(1, 6)):
        raise ValueError('emotion level can only take 1, 2, 3, 4, or 5')
    if not (cognition in range(1, 7)):
        raise ValueError('cognition level can only take 1, 2, 3, 4, 5, or 6')
    if not (pain in range(1, 7)):
        raise ValueError('pain level can only take 1, 2, 3, 4, 5, or 6')

    level_value = dictCoefficient['Vision'][vision - 1] * dictCoefficient['Hearing'][hearing - 1] * dictCoefficient['Speech'][speech - 1] * dictCoefficient['Ambulation'][ambulation - 1] * dictCoefficient['Dexterity'][dexterity - 1] * dictCoefficient['Emotion'][emotion - 1] * dictCoefficient['Cognition'][cognition - 1] * dictCoefficient['Pain'][pain - 1]
    score = constant_1 * level_value - constant_2

    return score



