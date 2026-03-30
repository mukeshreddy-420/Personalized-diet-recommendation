import pandas as pd

days = [
"Monday","Tuesday","Wednesday",
"Thursday","Friday","Saturday","Sunday"
]

def generate_plan(data, diet):

    if diet == "Veg":
        data = data[data["Diet_Type"]=="Veg"]

    elif diet == "Non-Veg":
        data = data[data["Diet_Type"]=="Non-Veg"]

    plan = []

    for day in days:

        breakfast = data[data["Meal_Type"]=="Breakfast"].sample(1)
        lunch = data[data["Meal_Type"]=="Lunch"].sample(1)
        dinner = data[data["Meal_Type"]=="Dinner"].sample(1)

        plan.append({
            "day":day,
            "breakfast":breakfast["Food_Item"].values[0],
            "lunch":lunch["Food_Item"].values[0],
            "dinner":dinner["Food_Item"].values[0]
        })

    return pd.DataFrame(plan)