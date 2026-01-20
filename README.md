SALES PREDICTION:
- This project predicts the units of sales (in thousands) using a Linear Regression model trained on advertising data. The model estimates sales based on how much budget is spent on TV, Radio, and Newspaper advertising, and the predictions are served through a clean web interface where users can input budgets and see the estimated units sold along with model performance.

LIVE DEMO:
- https://salespredictionusingpython.onrender.com/

FEATURES:
- Supervised learning with Linear Regression on the classic advertising dataset Advertising.csv.
- Input features: TV Budget, Radio Budget, Newspaper Budget (all in thousands of rupees).
- Output: Predicted units sold (thousands) with an R² score displayed on the UI.
- Jupyter notebook SalesPrediction.ipynb for EDA, model training, and evaluation.
- Saved model artifact sales_prediction_model.pkl and features.pkl for fast inference via the app.

INSTALLATION:
- git clone https://github.com/IshanGain/SalesPredictionUsingPython.git
- cd SalesPredictionUsingPython
- pip install -r requirements.txt

- Ensure Python and all dependencies listed in requirements.txt are installed in your environment.

USAGE (NOTEBOOK):
1. Open SalesPrediction.ipynb in Jupyter or VS Code.
2. Run the cells to:
      - Load Advertising.csv.
      - Explore relationships between ad spend and sales.
      - Train and evaluate the Linear Regression model (check R² and error metrics).
3. (Optional) Regenerate and save sales_prediction_model.pkl and features.pkl after retraining.

WEB APP (python app.py):
- Open the URL shown in the terminal.
- Enter TV Budget, Radio Budget, and Newspaper Budget values in the form, then click Predict Units Sold.
- The app will display predicted units sold (in thousands) and may also show the model’s R² score and other summary info, similar to the dashboard UI in the screenshot.

PROJECT STRUCTURE:
- SalesPredictionUsingPython/
- ├── Advertising.csv          # Dataset
- ├── SalesPrediction.ipynb    # EDA + model training notebook
- ├── app.py                   # Web app for predictions
- ├── features.pkl             # Feature metadata/transformer
- ├── sales_prediction_model.pkl  # Trained Linear Regression model
- ├── templates/               # HTML templates for UI
- ├── requirements.txt         # Dependencies
- └── README.md                # Project documentation
​​
