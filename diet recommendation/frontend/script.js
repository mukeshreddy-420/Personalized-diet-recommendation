function generate(){

let name=document.getElementById("name").value
let age=document.getElementById("age").value
let gender=document.getElementById("gender").value
let height=document.getElementById("height").value
let weight=document.getElementById("weight").value
let diet=document.getElementById("diet").value
let goal=document.getElementById("goal").value

fetch("/generate",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
name:name,
age:age,
gender:gender,
height:height,
weight:weight,
diet:diet,
goal:goal
})

})

.then(res=>res.json())

.then(data=>{

let html=""

html+="<h2>Health Summary</h2>"

html+="BMI: "+data.bmi+"<br>"
html+="Category: "+data.category+"<br>"
html+="Calories: "+data.calories+"<br><br>"

html+="<h2>Weekly Diet Plan</h2>"

html+="<table>"
html+="<tr><th>Day</th><th>Breakfast</th><th>Lunch</th><th>Dinner</th></tr>"

data.weekly_plan.forEach(d=>{

html+="<tr>"
html+="<td>"+d.day+"</td>"
html+="<td>"+d.breakfast+"</td>"
html+="<td>"+d.lunch+"</td>"
html+="<td>"+d.dinner+"</td>"
html+="</tr>"

})

html+="</table>"

document.getElementById("result").innerHTML=html

})

}