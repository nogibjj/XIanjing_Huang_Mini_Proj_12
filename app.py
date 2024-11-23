from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template for the BMI calculator
bmi_template = """
<!DOCTYPE html>
<html>
<head>
    <title>BMI Calculator</title>
</head>
<body>
    <h1>BMI Calculator</h1>
    <form method="POST">
        <label for="weight">Weight (kg):</label>
        <input type="number" name="weight" id="weight" step="any" value="{{ weight or '' }}" required>
        <br><br>
        <label for="height">Height (cm):</label>
        <input type="number" name="height" id="height" step="any" value="{{ height or '' }}" required>
        <br><br>
        <button type="submit">Calculate BMI</button>
    </form>

    {% if bmi is not none %}
        <h2>Your BMI: {{ bmi }}</h2>
        <p>{{ category }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    category = None
    weight = None
    height = None
    if request.method == "POST":
        try:
            # Retrieve input values
            weight = float(request.form["weight"])
            height = float(request.form["height"])  # Height in cm
            height_m = height / 100  # Convert height to meters

            # Calculate BMI
            bmi = round(weight / (height_m ** 2), 2)

            # Determine BMI category
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"
        except ValueError:
            bmi = "Invalid input. Please enter valid numbers."

    # Pass weight and height back to the template
    return render_template_string(bmi_template, bmi=bmi, category=category, weight=weight, height=height)

if __name__ == "__main__":
    app.run(debug=True)
