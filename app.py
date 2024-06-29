from flask import Flask, request, jsonify
import pandas as pd
import cloudpickle
import joblib

app = Flask(__name__)

# Load the preprocessor using cloudpickle
with open('/kaggle/working/preprocessor.pkl', 'rb') as f:
    preprocessor = cloudpickle.load(f)

# Load the XGBoost model using joblib
final_clf = joblib.load('/kaggle/working/clickthroughmodel.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    
    # Preprocess the data
    X_processed = preprocessor.transform(df)
    
    # Get the prediction
    prediction = final_clf.predict(X_processed)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
import pandas as pd
import cloudpickle
import joblib

app = Flask(__name__)

# Load the preprocessor using cloudpickle
with open('/kaggle/working/preprocessor.pkl', 'rb') as f:
    preprocessor = cloudpickle.load(f)

# Load the XGBoost model using joblib
final_clf = joblib.load('/kaggle/working/clickthroughmodel.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    
    # Preprocess the data
    X_processed = preprocessor.transform(df)
    
    # Get the prediction
    prediction = final_clf.predict(X_processed)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
