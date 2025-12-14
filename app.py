from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("sales_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

# Fixed R² score (from evaluation)
R2_SCORE = 0.90  # 90%

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    # Default input values (match HTML defaults)
    tv = 150
    radio = 40
    newspaper = 20

    if request.method == "POST":
        tv = float(request.form.get("tv_spend"))
        radio = float(request.form.get("radio_spend"))
        newspaper = float(request.form.get("newspaper_spend"))

        input_data = np.array([[tv, radio, newspaper]])
        prediction = model.predict(input_data)[0] # The model already returns the predicted value directly
        prediction = round(prediction, 1)  # thousand units

    return render_template(
        "index.html",
        prediction=prediction,
        r2_score=int(R2_SCORE * 100),
        tv=tv,
        radio=radio,
        newspaper=newspaper
    )

if __name__ == "__main__":
    app.run(debug=True)