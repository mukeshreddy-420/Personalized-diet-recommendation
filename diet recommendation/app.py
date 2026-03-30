from flask import Flask, request, jsonify, send_from_directory
import pandas as pd

from backend.bmi import calculate_bmi
from backend.calorie import calorie_goal
from backend.planner import generate_plan
from backend.model import train_model, recommend_food

app = Flask(__name__, static_folder="frontend", static_url_path="")

data = pd.read_csv("dataset/foods.csv")

model, scaler = train_model(data)


@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")


@app.route("/generate", methods=["POST"])
def generate():

    info = request.json

    name = info["name"]
    age = int(info["age"])
    gender = info["gender"]

    height_cm = float(info["height"])
    height = height_cm / 100

    weight = float(info["weight"])

    diet = info["diet"]
    goal = info["goal"]

    bmi, category = calculate_bmi(weight, height)

    calories = calorie_goal(goal, weight, height_cm, age, gender)

    weekly_plan = generate_plan(data, diet)

    recommended_foods = recommend_food(data, model, scaler, calories)

    weekly_plan = weekly_plan.to_dict(orient="records")
    recommended_foods = recommended_foods.to_dict(orient="records")

    return jsonify({
        "bmi": bmi,
        "category": category,
        "calories": calories,
        "weekly_plan": weekly_plan,
        "recommended_foods": recommended_foods
    })


if __name__ == "__main__":
    app.run(debug=True)