from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate")
def calculator():
    try:
        a = float(request.args["a"])
        b = float(request.args["b"])
        op = request.args["op"]
    except:
        return jsonify({"result": "Invalid input"})
    
    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        if b == 0:
            result = "Error: Division by zero"
        else:
            result = a / b
    else:
        result = "Invalid operation"

    print(f"Calculated {a} {op} {b} = {result}")
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)