def calorie_goal(goal, weight, height_cm, age, gender):

    if gender == "Male":
        bmr = 10*weight + 6.25*height_cm - 5*age + 5
    else:
        bmr = 10*weight + 6.25*height_cm - 5*age - 161

    if goal == "Weight Loss":
        calories = bmr - 300
    elif goal == "Weight Gain":
        calories = bmr + 300
    else:
        calories = bmr

    return round(calories)