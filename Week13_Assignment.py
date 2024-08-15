# Used Fake News Prediction pickle model as model.pkl

from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load your pre-trained model
model_path = "model.pkl"
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)


@app.route("/predict", methods=["POST"])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)

    # Convert data into the appropriate format
    input_data = np.array(data["input"]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_data)

    # Return the prediction result
    return jsonify({"prediction": int(prediction[0])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# Create an Azure App Service
'''
az group create --name myResourceGroup --location eastus
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name deploy --runtime "PYTHON:3.12"
'''

# Deployment
'''
az webapp deployment source config-local-git --name deploy --resource-group myResourceGroup
git init
git add .
git commit -m "Initial commit"
git remote add azure <url>
git push azure master
'''