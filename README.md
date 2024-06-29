# Click-Through Rate Prediction with XGBoost and Flask

This project demonstrates how to deploy a machine learning model using Flask. Specifically, it includes an XGBoost classifier for predicting click-through rates from advertising data. The model is integrated into a Flask web application for real-time predictions.

## Features

- **XGBoost Model**: Trained on advertising data to predict click-through rates.
- **Flask Web Application**: Provides a RESTful API endpoint for making predictions.

## Requirements

- Python 3.x
- Flask
- pandas
- scikit-learn
- XGBoost
- cloudpickle
- joblib

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2. Install dependencies:

    ```bash
   pip install -r requirements.txt

##Usage
1.Run the Flask Application:
  ```bash
  python app.py
```

2. Make Predictions:
   Send a POST request to http://localhost:5000/predict with JSON data containing the features for prediction. Example:
   
  ```bash
  {
    "Daily Time Spent on Site": value1,
    "Age": value2,
    "Area Income": value3,
    "Daily Internet Usage": value4,
    "Ad Topic Line": "value5",
    "City": "value6",
    "Gender": "value7",
    "Country": "value8",
    "Timestamp": "value9"
}
```

3. Response:
   The server will respond with a JSON object containing the prediction:
  ```bash
  {
    "prediction": 1 # 0 or 1
  }
```

Note: Make sure to change directories used in click-through-rate-prediction.ipynb according to your local directories if you want to run it.

app.py: Flask application for serving predictions.

preprocessor.pkl: Preprocessor serialized using cloudpickle.

clickthroughmodel.pkl: XGBoost model serialized using joblib.

requirements.txt: List of Python dependencies.

data.zip: contains the dataset this model was trained on.

link: https://www.kaggle.com/datasets/swekerr/click-through-rate-prediction
