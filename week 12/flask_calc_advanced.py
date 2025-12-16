from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        try:
            # Parse the JSON data from the POST request
            data = request.get_json()
            expression = data.get("expression", "")

            # Evaluate the mathematical expression safely
            result = eval(expression, {"__builtins__": None}, {"math": math})
            return jsonify({"result": result})
        except Exception as e:
            return jsonify({"result": "Error"})

    # Render the HTML page for GET request
    return render_template("index_calc.html")


if __name__ == "__main__":
    app.run(debug=True)
