def calculate_bmi(weight, height):
  bmi = weight/(height**2)
  return round(bmi,2)
def classify_bmi(bmi):
  if bmi < 18.5:
    return "Underweight"
  elif 18.5 <= bmi <25:
    return "Normal Weight"
  elif 25 <= bmi < 30:
    return "overweight"
  else:
    return "Obese"

try:
  weight = float(input("Enter your weight in kg's :  "))
  height = float(input("Enter your height in meter's :  "))
  bmi = calculate_bmi(weight, height)
  category = classify_bmi(bmi)
  print(f"Your BMI is {bmi} - Your condition is {category}")
except:
  print("Please enter valid numbers.")
