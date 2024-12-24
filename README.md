<h1 align = center>Employees Burnout Analysis and Prediction</h1>

## Description

- This project aims to develop a predictive model using machine learning techniques to predict burnout rate of a Employee based on various factors. 
- By understanding the factors contributing to burnout and developing prediction models, we aim to identify at-risk employees and provide targeted support
## Dataset
The dataset used in this project includes detailed employee information, such as:

- Number of designations held by the employee.
- Availability of work-from-home options.
- Additional relevant attributes influencing burnout.

The data is stored in both **CSV** and **Excel** formats, allowing easy access and preprocessing.

---

## 🗂️ Project Structure
The project is organized into the following directories and files for better modularity and maintainability:

### 1. **Dataset**
- Contains datasets in CSV and Excel formats.
- This folder serves as the primary source of training and testing data for the machine learning model.

### 2. **Model**
- Houses the trained machine learning model used for predicting employee burnout.
- The model is built using a Linear Regression algorithm and has been fine-tuned with the custom dataset.

### 3. **Images**
- Includes all the images used in the project, such as:
  - Diagrams and charts for data visualization.
  - Graphics for documentation and presentation materials.
  - Visual aids that enhance the understanding of the project.

### 4. **Static**
- Contains static files like stylesheets, JavaScript files, and additional resources used to design and enhance the web application interface.

### 5. **Templates**
- Stores HTML templates used for rendering web pages in the Flask-based web application.
- Templates are designed for a seamless and user-friendly experience.

### 6. **app.py**
- The core application file that drives the web application.
- It handles routes, renders templates, and integrates the machine learning model for predictions.
## How to Run the Project

### 1. **Install Required Libraries**
- Ensure Python (>=3.8) is installed.
- Install all the dependencies by running the following command:
  ```bash
  pip install -r requirements.txt
  ```
### 2. **Run the Application**
- Open the project in Visual Studio Code or any preferred IDE.
- Execute the `app.py` file to start the web application:
  ```bash
  python app.py
  ```
### 3. **Access the Application**
- Open your browser and navigate to `http://127.0.0.1:5000/` to interact with the application.



