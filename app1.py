from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__)

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "linear.pkl")

# Load the model using the absolute file path
with open(file_path, "rb") as f:
    model = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get variables from the form
        variable1 = float(request.form["variable1"])
        variable2 = float(request.form["variable2"])
        variable3 = float(request.form["variable3"])

        # Predict using the loaded model
        prediction = model.predict([[variable1, variable2, variable3]])

        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

