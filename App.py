from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('linear_regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    designation = int(request.form['designation'])
    resource_allocation = float(request.form['resource_allocation'])
    mental_fatigue_score = float(request.form['mental_fatigue_score'])
    company_type = request.form['company_type']
    wfh_setup_available = request.form['wfh_setup_available']
    gender = request.form['gender']
    
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'Designation': [designation],
        'Resource Allocation': [resource_allocation],
        'Mental Fatigue Score': [mental_fatigue_score],
        'Company Type_Service': [company_type],
        'WFH Setup Available_Yes': [wfh_setup_available],
        'Gender_Male': [gender]
    })
    
    # Convert categorical values to binary
    input_data['Company Type_Service'] = 1 if input_data.at[0, 'Company Type_Service'] == 'Service' else 0
    input_data['WFH Setup Available_Yes'] = 1 if input_data.at[0, 'WFH Setup Available_Yes'] == 'Yes' else 0
    input_data['Gender_Male'] = 1 if input_data.at[0, 'Gender_Male'] == 'Male' else 0
    
    # Make a prediction using the model without scaling
    prediction = model.predict(input_data)[0]
    rounded_prediction = round(prediction, 2)
    
    # Return the prediction with styling
    return render_template('index.html', prediction=rounded_prediction)

if __name__ == "__main__":
    app.run(debug=True)
