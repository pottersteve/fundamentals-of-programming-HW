from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    result = "Error: Division by zero"
                else:
                    result = num1 / num2
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Error: Invalid input"

    return render_template("index_simple_calc.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
